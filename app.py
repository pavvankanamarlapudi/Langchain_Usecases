import tempfile
import streamlit as st
from langchain_experimental.agents import create_csv_agent
from langchain.agents.agent_types import AgentType
from langchain_openai import OpenAI,ChatOpenAI
from langchain_community.vectorstores import FAISS
from streamlit_chat import message

# from streamlit



st.title("Chat with your Uploaded CSV")
user_avatar = "👤" 
bot_avatar = "🤖" 

uploaded_file = st.sidebar.file_uploader("Upload your Data", type="csv")


if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path  = tmp_file.name

    agent_executer = create_csv_agent(ChatOpenAI(temperature=0,
                                     model="gpt-3.5-turbo"),
                                     tmp_file_path,
                                     agent_type=AgentType.OPENAI_FUNCTIONS,
                                     verbose=True)

    def conversational_chat(query):
        
        query = query+" using tool python_repl_ast"
        result = agent_executer.invoke(query)
        st.session_state['history'].append((query, result["output"]))
        return result["output"]
    
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hello ! Ask me anything about " + uploaded_file.name + " 🤗"]

    if 'past' not in st.session_state:
        st.session_state['past'] = ["Hey ! 👋"]
        
    #container for the chat history
    response_container = st.container()


    #container for the user's text input
    container = st.container()
    with container:
        with st.form(key='my_form', clear_on_submit=True):
            
            user_input = st.text_input("Query:", placeholder="Talk to your csv data here (:", key='input')
            submit_button = st.form_submit_button(label='Send')
            
        if submit_button and user_input:
            output = conversational_chat(user_input)
            
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)

    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="personas",seed='Aneka')
                message(st.session_state["generated"][i], key=str(i), avatar_style="bottts")