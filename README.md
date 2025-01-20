# SwagLab Automation

This is an automation testing project for the **Swag Labs** application using Appium, Pytest, and other automation tools.

## Project Structure

The project consists of the following directories:

1. **/Apk**: Contains the APK of the application for Android testing.
2. **/Objects**: Contains object functions and element locators used throughout the project.
3. **/Reports**: Contains the Allure reports generated after test execution.
4. **/Tests**: Contains the actual test suite files that need to be executed.

## Prerequisites

Before running the test suite, ensure that the following dependencies are installed on your system:

1. **Python** (for running the tests)
2. **Appium Server** (for mobile automation)
3. **Pytest**: Install using the command:
       ```bash
       pip install pytest
4. **iOS Dependencies**
     (i) Xcode
     (ii) Carthage by using 'brew install carthage'
     (iii) ideviceinstaller by using 'brew install ideviceinstaller'

**To execute the test suite, navigate to the root directory and run the following command**

SwagLabsAutomation/Tests/test_run.py --alluredir=Report

**After the tests are executed, you can view the generated Allure report by running the following command**

allure serve report
