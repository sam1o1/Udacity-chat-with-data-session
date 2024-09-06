import streamlit as st
import pandas as pd
from llm_chat import chat_with_data
# # Sidebar for password input
st.sidebar.title("🗝️ Authentication")
password = st.sidebar.text_input("Enter Password", type="password")

# # # # # Check if the correct password is entered
if password == "start":
    st.sidebar.success("Password accepted!")
else:
    st.sidebar.error("Incorrect password. Please try again.")
    st.stop()

st.title("chat with data using Genai 💬")
# # # # st.title("CSV File Upload and Chat")

# # # # # CSV file upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# # # # # Check if a file is uploaded
if uploaded_file is not None:
    # Read and display the CSV file
    df = pd.read_csv(uploaded_file)
    st.write("Preview of the uploaded CSV file:")
    st.write(df.head())
else:
    st.warning("Please upload a CSV file to proceed.")
    st.stop()

# # # # # Simple chat implementation
if uploaded_file is not None:

# # #     # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

# # #     # Display chat messages from history
    for message in st.session_state.chat_history:
        st.chat_message(message["role"]).markdown(message["content"])

# # #     # User input for chat
    user_input = st.chat_input("Enter your message here:")

    if user_input:
        # Add user message to history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
# #         # Respond with "hello"
        # response = "hello"
        st.chat_message("user",avatar="logo.jpg").markdown(user_input)
        pandas_df_agent=chat_with_data(df)
  
        with st.spinner("The Agent is generating answers!"):
            response = pandas_df_agent.run(user_input)
            st.session_state.chat_history.append({"role": "assistant", "content": response})

            st.chat_message("assistant",avatar="🤖").markdown(response)
