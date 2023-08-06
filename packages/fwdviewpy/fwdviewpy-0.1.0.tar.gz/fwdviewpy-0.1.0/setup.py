from setuptools import setup

setup(
    name='fwdviewpy',
    version='0.1.0',
    description='Python package developed by FWD View to aid automation of Delphix actions on both the Virtulaization and Continuous Compliance Delphix engines.',
    packages=['fwdviewpy'],
    install_requires=[
        'logging',
        'sys',
        'requests',
        'datetime',
        'json'

    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
    ],
)





