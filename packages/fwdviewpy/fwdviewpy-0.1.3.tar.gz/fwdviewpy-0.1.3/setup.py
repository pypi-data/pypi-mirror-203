from setuptools import setup

setup(
    name='fwdviewpy',
    version='0.1.3',
    description='Python package developed by FWD View - The Data Transformation Specialists.',
    long_description='Python package developed by FWD View to aid automation of Delphix actions on both the Virtulaization and Continuous Compliance Delphix engines.',
    packages=['fwdviewpy'],
    author='Cameron Bose & Ryan Springett',
    author_email="cameron.bose@fwdview.com",

    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
    ]
)





