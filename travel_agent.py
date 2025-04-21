import streamlit as st
from textwrap import dedent
from agno.agent import Agent
# from agno.models.openai import OpenAIChat
from agno.models.google import Gemini
from agno.tools.exa import ExaTools
from instruct_guide.travel_instruction import *

import logging

logging.basicConfig(level=logging.DEBUG)

st.sidebar.header("Configuration")
google_api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")
exa_api_key = st.sidebar.text_input("Enter EXA API Key", type="password")

st.sidebar.markdown("-------")

st.sidebar.markdown(
    """
    **Get API Keys:**
    * [Get Google Gemini API Key](https://aistudio.google.com/apikey)
    * [Get EXA API Key](https://dashboard.exa.ai/api-keys)
    """
)
# Initialize Gemini model (only if API key is provided)
if google_api_key:
    gemini_model = Gemini(id="gemini-2.5-pro-exp-03-25", api_key=google_api_key)
else:
    gemini_model = None

# Initialize the travel agent (only if Gemini model is available)
if gemini_model and exa_api_key:
    travel_agent = Agent(
        name="Travel Agent",
        model=gemini_model,
        tools=[ExaTools(api_key=exa_api_key)],
        markdown=True,
        description=dedent("""\
            You are TravelAgent.sx, an elite travel planning expert with decades of experience! 🌍

            Your expertise encompasses:
            - Luxury and budget travel planning
            - Corporate retreat organization
            - Cultural immersion experiences
            - Adventure trip coordination
            - Local cuisine exploration
            - Transportation logistics
            - Accommodation selection
            - Activity curation
            - Budget optimization
            - Group travel management"""),
        instructions=agent_instructions,
        add_datetime_to_instructions=True,
        show_tool_calls=True,
    )

    # Initialize the travel planner agent (only if Gemini model is available)
    travel_planner = Agent(
        name="Travel Planner",
        description="You are Travel Plan Maestro, a meticulous travel itinerary architect. 🗺️ Your expertise lies in taking initial travel suggestions and transforming them into highly structured, day-by-day itineraries. You excel at adding practical details such as estimated times, transportation options, booking requirements, and local tips to ensure a smooth and well-organized travel experience.",
        model=gemini_model,
        instructions=planner_instructions,
        add_datetime_to_instructions=True,
        show_tool_calls=True,
        markdown=True,
    )
else:
    travel_agent = None
    travel_planner = None
    st.warning("Please enter both Gemini and EXA API keys in the sidebar to use the planner.")

st.title("Travel-Plannr")

location = st.text_input("Where would you like to travel?")
duration_options = ["1 day", "2 days", "3 days", "4 days", "5 days", "7 days", "10 days"]
duration = st.selectbox("How long will your trip be?", duration_options)
travelers_option = st.radio("Number of Travelers:", ["Solo Trip", "More than one"])

num_travelers = 1
if travelers_option == "More than one":
    num_travelers = st.number_input("Enter the number of travelers:", min_value=2, step=1)

if st.button("Generate Travel Plan"):
    if not google_api_key or not exa_api_key:
        st.warning("Please enter both Gemini and EXA API keys in the sidebar.")
    elif not location:
        st.warning("Please enter a location for your trip.")
    elif travel_agent and travel_planner:
        with st.spinner(f"Generating a travel plan for {num_travelers} traveler(s) in {location} for {duration}..."):
            try:
                query = f"Plan a trip to {location} for {num_travelers} people for {duration}. Please suggest options for places to stay, activities, and transportation with a detailed itinerary."
                agent_response = travel_agent.run(query)
                response_content = agent_response.content
                st.subheader("Initial Travel Plan:")
                st.markdown(response_content)

                st.spinner("Now refining the plan with the travel planner...")
                planner_response = travel_planner.run(response_content)
                st.subheader("Refined Travel Plan:")
                st.markdown(planner_response.content)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.info("Please provide the API keys to enable travel plan generation.")

<<<<<<< HEAD
# import streamlit as st
# from textwrap import dedent
# from agno.agent import Agent
# from agno.models.openai import OpenAIChat
# from agno.models.google import Gemini
# from agno.tools.exa import ExaTools
# from instruct_guide.travel_instruction import *

# import logging

# logging.basicConfig(level=logging.DEBUG)

# gemini_model=Gemini(id="gemini-2.0-flash")

# travel_agent = Agent(
#     name="Globe Hopper",
#     model=gemini_model,
#     tools=[ExaTools],
#     markdown=True,
#     description=dedent("""\
#         You are Globe Hopper, an elite travel planning expert with decades of experience! 🌍

#         Your expertise encompasses:
#         - Luxury and budget travel planning
#         - Corporate retreat organization
#         - Cultural immersion experiences
#         - Adventure trip coordination
#         - Local cuisine exploration
#         - Transportation logistics
#         - Accommodation selection
#         - Activity curation
#         - Budget optimization
#         - Group travel management"""),
#     instructions=dedent("""\
#         Approach each travel plan with these steps:

#         1. Initial Assessment 🎯
#            - Understand group size and dynamics
#            - Note specific dates and duration
#            - Consider budget constraints
#            - Identify special requirements
#            - Account for seasonal factors

#         2. Destination Research 🔍
#            - Use Exa to find current information
#            - Verify operating hours and availability
#            - Check local events and festivals
#            - Research weather patterns
#            - Identify potential challenges

#         3. Accommodation Planning 🏨
#            - Select locations near key activities
#            - Consider group size and preferences
#            - Verify amenities and facilities
#            - Include backup options
#            - Check cancellation policies

#         4. Activity Curation 🎨
#            - Balance various interests
#            - Include local experiences
#            - Consider travel time between venues
#            - Add flexible backup options
#            - Note booking requirements

#         5. Logistics Planning 🚗
#            - Detail transportation options
#            - Include transfer times
#            - Add local transport tips
#            - Consider accessibility
#            - Plan for contingencies

#         6. Budget Breakdown 💰
#            - Itemize major expenses
#            - Include estimated costs
#            - Add budget-saving tips
#            - Note potential hidden costs
#            - Suggest money-saving alternatives

#         Presentation Style:
#         - Use clear markdown formatting
#         - Present day-by-day itinerary
#         - Include maps when relevant
#         - Add time estimates for activities
#         - Use emojis for better visualization
#         - Highlight must-do activities
#         - Note advance booking requirements
#         - Include local tips and cultural notes"""),
#     add_datetime_to_instructions=True,
#     show_tool_calls=True,
# )

# travel_planner = Agent(
#                     name="Travel Planner Analyzer",
#                     description="You are Globe Hopper, an elite travel planning expert with decades of experience! 🌍",
#                     model=gemini_model,
#                     instructions=planner_instructions,
#                      add_datetime_to_instructions=True,
#                     show_tool_calls=True,
#                     markdown=True,
#                 )
=======
>>>>>>> dc6f41f476684ec30526bded4af1074ddc686483


