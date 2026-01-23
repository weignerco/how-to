## Deploy Guide for RAG OCI GenAI Agent Streamlit App

# Note: Create a python virtual environment (venv) to make use of the relevant versions for this demo app. 
# * The initial test was ran without a venv.
# * As a result, it used the locally installed Python version, causing dependency and version conflicts.
# * The issue was resolved by rerunning the test within a properly configured venv

# Prerequisites:
# - Python 3.x installed on your local machine
# - OCI CLI installed and configured with your OCI account credentials
# - Access to an OCI GenAI Agent endpoint

# Step 1: Create a virtual environment
# Step 2: Activate the virtual environment
# Step 3: Install required packages
# Step 4: Run the Streamlit app


# 1: Creates a virtual environment (directory) called venvdemo in your current directory
python3 -m venv venvdemo

# 2: Activate the virtual environment
source venvdemo/bin/activate

# 3. Install required packages inside the virtual environment
pip3 install python==3.9.6
pip3 install streamlit oci

# Verify the versions of the installed packages
python3 --version
streamlit --version

# 4. To run the Streamlit app, use the following command
streamlit run rag-chatbot.py # To stop the app, press Ctrl+C in the terminal

# To deactivate the virtual environment when done, use the following command
deactivate