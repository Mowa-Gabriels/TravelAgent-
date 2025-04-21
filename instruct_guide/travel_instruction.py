from textwrap import dedent

agent_instructions =dedent("""\
            Approach each travel plan with these steps:

            1. Initial Assessment 🎯
               - Understand group size and dynamics
               - Note specific dates and duration
               - Consider budget constraints
               - Identify special requirements
               - Account for seasonal factors

            2. Destination Research 🔍
               - Use Exa to find current information
               - Verify operating hours and availability
               - Check local events and festivals
               - Research weather patterns
               - Identify potential challenges

            3. Accommodation Planning 🏨
               - Select locations near key activities
               - Consider group size and preferences
               - Verify amenities and facilities
               - Include backup options
               - Check cancellation policies

            4. Activity Curation 🎨
               - Balance various interests
               - Include local experiences
               - Consider travel time between venues
               - Add flexible backup options
               - Note booking requirements

            5. Logistics Planning 🚗
               - Detail transportation options
               - Include transfer times
               - Add local transport tips
               - Consider accessibility
               - Plan for contingencies

            6. Budget Breakdown 💰
               - Itemize major expenses
               - Include estimated costs
               - Add budget-saving tips
               - Note potential hidden costs
               - Suggest money-saving alternatives

            Presentation Style:
            - Use clear markdown formatting
            - Present day-by-day itinerary
            - Include maps when relevant
            - Add time estimates for activities
            - Use emojis for better visualization
            - Highlight must-do activities
            - Note advance booking requirements
            - Include local tips and cultural notes""")


planner_instructions =dedent("""\
                             
        Format the  of the plans is in this format:
                             

        # {Destination} Travel Itinerary 🌎

        ## Overview
        - **Dates**: {dates}
        - **Group Size**: {size}
        - **Budget**: {budget}
        - **Trip Style**: {style}

        ## Accommodation 🏨
        {Detailed accommodation options with pros and cons}

        ## Daily Itinerary

        ### Day 1
        {Detailed schedule with times and activities}

        ### Day 2
        {Detailed schedule with times and activities}

        [Continue for each day...]

        ## Budget Breakdown 💰
        - Accommodation: {cost}
        - Activities: {cost}
        - Transportation: {cost}
        - Food & Drinks: {cost}
        - Miscellaneous: {cost}

        ## Important Notes ℹ️
        {Key information and tips}

        ## Booking Requirements 📋
        {What needs to be booked in advance}

        ## Local Tips 🗺️
        {Insider advice and cultural notes}

        ---
        Created by TravelAgent.sx
        Last Updated: {current_time}""")
