# BuildDevEnv

## Purpose
This package has been designed to create easily, with minimalists template files, a development environment in Docker.
Note that is has been tested on Windows 10 only with Docker Desktop.

## Requirements
The following components are required to execute the package:
- Python 3.6 or +
- pip installer
- Docker Desktop

## Install
This package is available from Pypi. In order to install it, execute the following command:
`pip install builddevenv`

## Usage
Before using the libray, the execution policy of PowerShell must be changed to authorized Python to use Docker API. In PowerShell, execute the following command:
`Set-ExecutionPolicy Unrestricted -Force`

Once the Powershell execution policy changed, it is then possible to execute the package using the following command line:
`python -m builddevenv <template file>`

Replace *template-file* by the full name of the file containing the containers configuration.

You can find some samples in the package installation folder, under the directory named *sample*

## Unit tests
In development mode of this package, it is mandatory to implement unit tests when a feature is added.
The unit tests are written in the folder *test*.
In order to run the unit tests, set the current directory to the root folder of the project. Then execute the command:
`python -m pytest`
