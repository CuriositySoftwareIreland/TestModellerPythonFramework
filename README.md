## Python Pytest Selenium Framework for TestModeller 
Open source repository of Java based selenium tests. For use with TestModeller.io

### Environment Setup
1. Global Dependencies
    * Install Python(https://www.python.org/downloads/)

    * Install pip(https://pip.pypa.io/en/stable/installing/) for package installation

2. Project
	* The recommended way to run your tests would be in [virtualenv](https://virtualenv.readthedocs.org/en/latest/). It will isolate the build from other setups you may have running and ensure that the tests run with the specified versions of the modules specified in the requirements.txt file.
	```$ pip install virtualenv```
	* Create a virtual environment in your project folder the environment name is arbitrary.
	```$ virtualenv venv```
	* Activate the environment:
	```$ source venv/bin/activate```
	* Install the required packages:
	```$ pip install -r requirements.txt```

### Integrating Tests:
* Copy generated page objects into the 'pages' directory.
* Copy generated tests into the 'tests' directory.

### Running Tests:
*  Tests in Parallel:
    ```$ py.test -s -n 2 tests```