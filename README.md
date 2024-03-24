# Python 3.9 Setup and OpenAI API Key Configuration Guide

This guide provides step-by-step instructions on how to set up Python 3.9, generate an OpenAI API key, configure it in your PC's environment variables, and start a Streamlit app.

## Installing Python 3.9

1. Download the Python 3.9 installer from the official Python website: [Python 3.9 Downloads](https://www.python.org/downloads/release/python-390/).
2. Run the installer. Make sure to check the option that says **"Add Python 3.9 to PATH"** during installation.
3. After installation, open a command prompt or terminal and run the following command to check the Python version:
    ```shell
    python --version
    ```
   You should see `Python 3.9.x` indicating that Python 3.9 is successfully installed.

## Generating an OpenAI API Key

1. Go to the [OpenAI API](https://beta.openai.com/signup/) signup page and create an account if you haven't already.
2. Once logged in, navigate to the API keys section of your account.
3. Click on **"Create new key"** to generate a new API key.
4. Copy the generated API key for later use.

## Configuring the OpenAI API Key in Environment Variables (User Level)

1. On your PC, search for and select **"Edit environment variables for your account"** by opening the Start Search and typing `env`.
2. In the Environment Variables window, under the **User Variables** section, click on **New...** to create a new environment variable.
3. Enter `OPENAI_API_KEY` as the variable name and paste your copied OpenAI API key as the variable value.
4. Click OK to close all windows.

## Creating and Activating a Virtual Environment

Before installing the project's dependencies, it's a good practice to create a virtual environment. This keeps your dependencies separate from those of other projects and the system.

1. Open a command prompt or terminal.
2. Navigate to your project directory where you want to set up the virtual environment.
3. Run the following command to create a virtual environment named `venv`:
    ```shell
    python -m venv venv
    ```
   This command creates a new directory named `venv` in your project folder, where the virtual environment files are stored.

4. Activate the virtual environment by running one of the following commands:
    - On Windows:
        ```shell
        .\venv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```shell
        source venv/bin/activate
        ```
   After activation, your command prompt or terminal will usually show the name of the activated virtual environment, indicating that it is currently active.


## Installing Dependencies

Before starting your Streamlit app, you need to install any dependencies it requires. If you have a `requirements.txt` file listing all the needed packages:

1. Open a command prompt or terminal.
2. Navigate to the directory containing your `requirements.txt` file.
3. Run the following command to install the dependencies:
    ```shell
    pip install -r requirements.txt
    ```
## Starting a CSV Chat App

1. With Streamlit installed, and your `app.py` file ready, you can now start your Streamlit app.
2. Open a command prompt or terminal.
3. Navigate to the directory that contains your `app.py` file.
4. Execute the command below to launch the Streamlit app:
    ```shell
    streamlit run app.py
    ```
5. Your default web browser will automatically open to the address where your Streamlit app is running, usually `http://localhost:8501`.
