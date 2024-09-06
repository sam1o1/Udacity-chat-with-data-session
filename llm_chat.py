
from langchain.agents import AgentType
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key= os.getenv('OPENAI_API_KEY')

def chat_with_data (df):
    
    llm = ChatOpenAI(
        temperature=0, model="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True
    )

    pandas_df_agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        handle_parsing_errors=True,
        allow_dangerous_code=True
    )
    return pandas_df_agent
