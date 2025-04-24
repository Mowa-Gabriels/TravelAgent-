
from textwrap import dedent
import streamlit as st
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.tavily import TavilyTools
from instruct_guide.legal_instructions import *
import os
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.storage.sqlite import SqliteStorage



db_file="tmp/legal_memory.db"


#Sidebar for API Keys and Settings
with st.sidebar:
    st.header("API Keys")
    gemini_api_key = st.text_input("Gemini API Key", type="password", value=os.environ.get("YOUR_GEMINI_API_KEY"))
    tavily_api_key = st.text_input("Tavily API Key", type="password", value=os.environ.get("YOUR_TAVILY_API_KEY"))
    user_email = st.text_input("Enter your Email Address for session tracking:")
    court_level = st.selectbox("Court Level", ["Any", "High Court", "Court of Appeal", "Supreme Court"])
    
st.sidebar.markdown("-------")
st.sidebar.markdown(
    """
    **Get API Keys:**
    * [Get Google Gemini API Key](https://aistudio.google.com/apikey)
    * [Get Tavily API Key](https://app.tavily.com/home)
    """
)


legal_memory = Memory(
    
    model=Gemini(id="gemini-2.0-flash", api_key=gemini_api_key),
    db=SqliteMemoryDb(table_name="legal_memory", db_file=db_file),
)

storage = SqliteStorage(table_name="legal_agent_sessions", db_file=db_file)

#Main Application
st.title("D-Law: Nigerian Legal Research & Argument Strategist")
st.subheader("Powered by Agno Agents")

query = st.text_area("Enter your Legal Query:", height=200,placeholder="My client has been charged with bribery under Section 98 of the Criminal Code Act. The prosecution's main evidence is a series of text messages. I need to argue that these text messages are insufficient to establish the necessary intent for bribery. Please find relevant Nigerian case law on the issue of intent in bribery cases, particularly where the evidence is circumstantial, and provide a potential argument framework I can use in my submission to the High Court of Lagos State.")

if st.button("Generate Legal Analysis"):
    if not gemini_api_key or not tavily_api_key:
        st.error("Please enter both Gemini and Tavily API keys in the sidebar.")
    elif not query:
        st.warning("Please enter your legal query.")
    else:
        # Initialize Agents with API Keys
        legal_scout = Agent(
            name="Legal Scout",
            model=Gemini(id="gemini-2.0-flash", api_key=gemini_api_key),
            tools=[TavilyTools(api_key=tavily_api_key)],
            markdown=True,
            description=dedent("""\
                You are Legal Scout, an expert AI legal researcher specializing in efficiently locating relevant Nigerian legal resources.
                Your primary goal is to find pertinent case law, statutes, and regulations based on user queries related to Nigerian law.
                You are highly skilled in crafting effective search queries and filtering results for relevance, considering the specified court level.
            """),
            instructions=scout_instructions,
            show_tool_calls=True,
            memory=legal_memory,  # Add memory
            enable_agentic_memory=True, # Enable agentic 
            enable_user_memories=True,
            storage=storage,
            add_history_to_messages=True,
            num_history_runs=5,
        )

        legal_examiner = Agent(
            name="Legal Examiner",
            model=Gemini(id="gemini-2.0-flash", api_key=gemini_api_key),
            markdown=True,
            description=dedent("""\
                You are Legal Examiner, an expert AI legal analyst specializing in the in-depth examination of Nigerian case law.
                Your primary goal is to analyze legal texts, extract key information, and identify the core legal principles and reasoning within judgments.
            """),
            instructions=examiner_instructions,
            show_tool_calls=True,
            memory=legal_memory,  # Add memory
            enable_agentic_memory=True, # Enable agentic memory
            enable_user_memories=True,
            storage=storage,
            add_history_to_messages=True,
            num_history_runs=5,
        )

        legal_strategist = Agent(
            name="Legal Strategist",
            model=Gemini(id="gemini-2.0-flash", api_key=gemini_api_key),
            markdown=True,
            description=dedent("""\
                You are Legal Strategist, an expert AI legal strategist specializing in constructing persuasive legal arguments for Nigerian courts.
                Your primary goal is to develop argument frameworks based on legal analysis and precedent.
            """),
            instructions=strategist_instructions,
            show_tool_calls=True,
            memory=legal_memory,  # Add memory
            enable_agentic_memory=True, # Enable agentic memory
            enable_user_memories=True,
            storage=storage,
            add_history_to_messages=True,
            num_history_runs=5,
        )

        legal_scribe = Agent(
            name="Legal Scribe",
            team=[legal_scout, legal_examiner, legal_strategist],
            model=Gemini(id="gemini-2.0-flash", api_key=gemini_api_key),
            markdown=True,
            description=dedent("""\
                You are Legal Scribe, an expert AI legal writer specializing in formatting legal research and arguments for clarity and readability.
                Your primary goal is to present the findings and arguments generated by the other agents in a well-structured and user-friendly format.
            """),

            instructions=scribe_instructions,
            show_tool_calls=True,
            memory=legal_memory,  # Add memory
            enable_agentic_memory=True, # Enable agentic memory
            enable_user_memories=True,
            storage=storage,
            add_history_to_messages=True,
            num_history_runs=5,
        )


        st.subheader("Legal Analysis and Argument:")
        with st.spinner("Generating analysis..."):
            response = legal_scribe.run(query,user_id=user_email,stream=False)
            st.markdown(response.content,)
        if user_email:
            st.subheader(f"Memories for {user_email}:")
            memories = legal_memory.get_user_memories(user_id=user_email)
            if memories:
                for i, memory_item in enumerate(memories):
                    with st.expander(f"Memory: {memory_item.memory[:20]}..."): 
                        st.write(memory_item.memory)
            else:
                st.info("No memories found for this email address.")
        else:
            st.info("Enter an email address to view memories.")
           
          