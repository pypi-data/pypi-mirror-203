import logging
import sys
import requests
import time
from datetime import datetime 
import json

class VirtualisationEngineSessionManager:

    def __init__(self, address, username, password, major, minor, micro):
        # SETTING UP LOG FILE
        logging.basicConfig(filename='VirtualisationEngineSessionManager.log',
                            level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s', filemode='w')
        logging.info(30 * '=' + '| RUN BEGINS |' + 30 * '=')

        self.address = address
        self.username = username
        self.password = password
        self.major = major
        self.minor = minor
        self.micro = micro

    def __str__(self):
        return f'Virtualisation Engine Session Manager: {self.address}'

    # POTENTIALLY ADD A REFRESH FUNCTION RATHER THAN USING THE LOGIN TO REFRESH DATA

    def login(self):
        """This function logs into the Virtualisation Engine
        """
        # establishing session
        session = requests.session()
        session_url = f"http://{self.address}/resources/json/delphix/session"
        data = {
            "type": "APISession",
            "version": {
                "type": "APIVersion",
                "major": self.major,
                "minor": self.minor,
                "micro": self.micro
            }
        }
        response = session.post(session_url, json=data)
        print(response.text)
        if response.ok:
            logging.debug(f"Session established on {self.address}")
        else:
            logging.error(f"Session NOT established on {self.address}")
            sys.exit()
        # this logs in and grabs all information from engine - works as a refresh
        url = f"http://{self.address}/resources/json/delphix/login"
        data = {
            "type": "LoginRequest",
            "username": self.username,
            "password": self.password
        }

        response = session.post(url, json=data)
        print(response.text)
        if response.ok:
            logging.debug(
                f"login SUCCEEDED - Response: {response.status_code}")
            # self.datasets = self.get_datasets_info()
            # self.bookmarks = self.get_bookmarks_info()
            # self.snapshots = self.get_snapshots_info()
            # self.sources = self.get_sources_info()
            # self.replications = self.get_replications_info()
            # self.environments = self.get_environments_info()
        else:
            logging.error(f"login FAILED - Response: {response.status_code}")
            sys.exit()
        return session

    def createBookmark(self, containerName, bookmarkName):
        # Set up the session object
        containerReference, containerBranch = self.getTemplateBranch(containerName)
        # Send a POST request to the bookmark endpoint with cookies set from the session
        bookmark_url = f"http://{self.address}/resources/json/delphix/selfservice/bookmark"
        data = {
            "type": "JSBookmarkCreateParameters",
            "bookmark": {
                "type": "JSBookmark",
                "name": bookmarkName,
                "branch": containerBranch
            },
            "timelinePointParameters": {
                "type": "JSTimelinePointLatestTimeInput",
                "sourceDataLayout": containerReference
            }
        }
        session = self.login()
        response = session.post(bookmark_url, json=data)
        action = response.json()['action']
        self.checkActionLoop(action)
        # print(response.json())
        session.close()
        return str(f"Bookmark: {bookmarkName}\nDate and Time: {datetime.now()}\nOutput: {response.json()}\n{'=' * 30}\n")

    def checkActionLoop(self, action): 
        while True:
            if self.checkAction(action):
                print("It has Completed!")
                break
            elif self.checkAction(action) == "FAILED":
                current_time = datetime.datetime.now()
                current_time_formatted = current_time.strftime("%Y-%m-%d %H:%M:%S")
                print("Action has failed, check engine logs.")
                """ sendEmailAlert(bookmarkName, current_time_formatted, "Virtualisation Engine") """
                sys.exit()
            else:
                print("Not yet Completed, check again in 30 seconds")
                time.sleep(30)

    def checkAction(self, action):
        session = self.login()
        action_url = f"http://{self.address}/resources/json/delphix/action"
        APIQuery = session.get(action_url)
        for actions in APIQuery.json()["result"]:
            if actions['reference'] == action:
                state = actions['state']
                print(state)
                if state == "COMPLETED":
                    session.close()
                    return True
                elif state == "FAILED":
                    state = "FAILED"
                    session.close()
                    return state
                else:
                    return False
    
    def getTemplateBranch(self, containerName):
        # Log in and obtain the session object
        session = self.login() 


        # Send a GET request to the selfservice/template endpoint with cookies set from the session
        template_url = f"http://{self.address}/resources/json/delphix/selfservice/container"
        response = session.get(template_url)

        # Extract the template reference and active branch from the API response
        container_reference = None
        container_branch = None
        for container in response.json()["result"]:
            if container['name'] == containerName:
                container_reference = container["reference"]
                container_branch = container["activeBranch"]
                break

        print(
            f"container reference: {container_reference} & Template branch: {container_branch}")

        # Close the session
        session.close()

        return container_reference, container_branch 
    
class MaskingEngineSessionManager: 
    def __init__(self, address, username, password, major, minor, micro): 
        self.address = address 
        self.username = username 
        self.password = password
        self.major = major 
        self.minor = minor
        self.micro = micro 

    
    def login(self): 
        url = f"http://{self.address}/masking/api/v5.1.14/login"

        payload = json.dumps({"username": self.username, "password": self.password})
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        responseDict = response.json()
        authKey = responseDict['Authorization']
        print(authKey)
        return authKey
    
    def runMaskingJob(self, environment, maskingRule, connectorName):
        authKey = self.login()
        envID = self.getEnvironment(authKey, environment)
        ruleID = self.getJobId(authKey, maskingRule, envID)
        targetConnectorID = self.getTargetConnectorID(authKey, connectorName, envID)
        executejob = self.execute_job(authKey, ruleID, targetConnectorID)
        print(executejob)
        executionID = self.getExecutionID(authKey, ruleID)
        jobStatus = self.checkStatus(executionID) 
        
        if jobStatus == "SUCCEEDED":
            print("Moving on to the next step.")
            return str(f"Masking Job: \nDate and Time: {datetime.now()}\nOutput: {jobStatus}\n{'=' * 30}\n")

        else:
            current_time = datetime.datetime.now()
            current_time_formatted = current_time.strftime("%Y-%m-%d %H:%M:%S")
            print(
                f"Please check error logs for masking job: {maskingRule} @ {current_time_formatted}")

            sys.exit()
    
    def getEnvironment(self, authKey, envName):
        response = self.getRequest(authKey, "environments")
        response = json.loads(response)
        for env in response["responseList"]:
            if env["environmentName"] == envName:
                envID = env["environmentId"]
        return envID
    

    def getRequest(self, authKey, endPoint):
        url = f"http://{self.address}/masking/api/v5.1.14/{endPoint}"
        payload = {}
        headers = {
            'Authorization': authKey
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        response = response.text
        return response

    def getJobId(self, authKey, jobName, envID):
        endPoint = f"masking-jobs?environment_id={envID}"
        response = self.getRequest(authKey, endPoint)
        response = json.loads(response)
        for job in response["responseList"]:
            if job["jobName"] == jobName:
                jobID = job['maskingJobId']
        return jobID

    def getTargetConnectorID(self, authKey, connectorName, environmentId):
        response = self.getRequest(authKey, "database-connectors")
        response = json.loads(response)
        for connectors in response["responseList"]:
            if connectors["connectorName"] == connectorName and connectors["environmentId"] == environmentId:
                targetConnectorID = connectors["databaseConnectorId"]
        return targetConnectorID
     
    def execute_job(self, auth_key, job_id, targetConnectorID):
        url = f"http://{self.address}/masking/api/v5.1.14/executions"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': auth_key
        }
        data = {
            'jobId': job_id, 
            'targetConnectorId': targetConnectorID
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))

        return response.text

    def checkStatus(self, executionID):
        authKey = self.login()
        while True:
            status = self.getStatus(authKey, executionID)
            if status == "RUNNING":
                time.sleep(300)
                print("Job is still running, check again in 5 minutes.")
            else:
                print(f"Job has finished running. Job Status is: {status}")
                return status
                break

 
