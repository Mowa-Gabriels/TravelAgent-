# TravelAgent.sx
AI-powered travel planning agents that take your destination and duration, then generate and refine detailed itineraries, including accommodation, activities, transportation, and budget breakdowns, built with Agno and Gemini model.

## Overview

This project features two powerful AI agents, **Travel Agent** and **Travel Planner**, designed to simplify and enhance your travel planning process.

**Travel Agent** acts as an experienced travel expert, taking your basic travel requirements (destination, duration, number of travellers) and generating an initial, comprehensive travel plan. This includes suggestions for accommodation, activities, transportation options, and a preliminary budget breakdown, leveraging web research capabilities.

**Travel Planner** then steps in as a meticulous itinerary architect. It takes the initial plan from Globe Hopper and refines it into a detailed, day-by-day itinerary. Travel Planner adds crucial practical details such as estimated times for activities, specific transportation methods, booking requirements, local tips, and cultural notes, ensuring a well-organized and enjoyable trip.

It is built using the [Agno framework](https://docs.agno.com/) for agent orchestration and leverages the power of large language models (specifically [Google Gemini](https://ai.google.dev/gemini-api) via Agno) for intelligent planning and content generation. It also utilizes the [EXA API](https://exa.ai/) for real-time web information retrieval. A user-friendly interface is provided through [Streamlit](https://streamlit.io/).

## Features

* **Intuitive Streamlit Interface:** Easily input your travel preferences through a simple web application.
* **Initial Travel Plan Generation (Travel Agent):** Get a broad overview of your potential trip, including:
    * Accommodation suggestions
    * Activity ideas
    * Transportation options
    * Preliminary budget estimates
* **Detailed Itinerary Refinement (Travel Planner):** Transform the initial plan into a structured, day-by-day itinerary with:
    * Estimated time allocations for activities
    * Specific transportation details
    * Booking requirements and recommendations
    * Local tips and cultural insights
* **Web Research Integration:** Utilizes the EXA API to fetch up-to-date information for accurate planning.
* **Powered by Large Language Models:** Uses the intelligence of Google Gemini for creative and comprehensive planning.
* **Agent Orchestration:** Built with the Agno framework for seamless interaction between multiple AI agents.

## Prerequisites

* **Python 3.9 or higher**
* **Streamlit** (`pip install streamlit`)
* **Agno** (`pip install agno`)
* **Google Gemini API Key:** You will need to obtain an API key from the [Google AI Studio]([https://ai.google.dev/](https://aistudio.google.com/apikey)).
* **EXA API Key:** You will need to obtain an API key from [EXA AI](https://exa.ai/).



## Usage


1.  **Run the Streamlit application:**
   * Open your web browser to the address displayed in the terminal (usually `http://localhost:8501`).
   * Enter the API keys directly in the sidebar of the running application.

2.  Enter your desired travel location, select the trip duration, indicate the number of travellers, and click "Generate Travel Plan".




