import streamlit as st
import time
import oci

## Personalize your Streamlit app by updating the following with your own values:
# 1. Page title
# 2. Sidebar image
# 3. OCI GenAI settings (OCI CLI profile name, Service Endpoint, Agent Endpoint ID)


# Page Title - update this with your own title
st.title("🤖 RAG Chatbot Demo")

# Sidebar Image - update this with your own image
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3398/3398643.png")


## OCI GenAI settings

# OCI CLI profile name - update this with your own profile name
# This is the .oci/config profile you use to connect your local machine via oci cli
config = oci.config.from_file(profile_name="OSAKA") 

# Service Endpoint - update this with the appropriate endpoint for your region
# a list of valid endpoints can be found here - https://docs.oracle.com/en-us/iaas/api/#/en/generative-ai-agents-client/20240531/
service_ep = "https://agent-runtime.generativeai.ap-osaka-1.oci.oraclecloud.com" 

# Agent Endpoint ID - update this with your own agent endpoint OCID
# this can be found within Generative AI Agents > Agents > (Your Agent) > Endpoints > (Your Endpoint) > OCID
agent_ep_id = "ocid1.genaiagentendpoint.oc1.ap-osaka-1.xyz"


# Response Generator
def response_generator(textinput):
   # Initialize service client with default config file
   generative_ai_agent_runtime_client = oci.generative_ai_agent_runtime.GenerativeAiAgentRuntimeClient(config,service_endpoint=service_ep)


   # Create Session
   create_session_response = generative_ai_agent_runtime_client.create_session(
       create_session_details=oci.generative_ai_agent_runtime.models.CreateSessionDetails(
           display_name="USER_Session",
           description="User Session"),
       agent_endpoint_id=agent_ep_id)
   sess_id = create_session_response.data.id
   response = generative_ai_agent_runtime_client.chat(
       agent_endpoint_id=agent_ep_id,
       chat_details=oci.generative_ai_agent_runtime.models.ChatDetails(
           user_message=textinput,
           session_id=sess_id))


   #print(str(response.data))
   response = response.data.message.content.text
   return response


# Initialize chat history
if "messages" not in st.session_state:
   st.session_state.messages = []


# Display chat messages from history on app rerun
for message in st.session_state.messages:
   with st.chat_message(message["role"]):
       st.markdown(message["content"])


# Accept user input
if prompt := st.chat_input("How can I help?"):


   # Add user message to chat history
   st.session_state.messages.append({"role": "user", "content": prompt})


   # Display user message in chat message container
   with st.chat_message("user"):
       st.markdown(prompt)


   # Display assistant response in chat message container
   with st.chat_message("assistant"):
       response = response_generator(prompt)
       write_response = st.write(response)


   # Add assistant response to chat history
   st.session_state.messages.append({"role": "assistant", "content": response})
