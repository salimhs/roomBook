This project automates the process of booking study rooms at Carleton University Library. The script logs into the Carleton booking system, selects a study room based on the user's preferences, and reserves it for a specific time slot. This eliminates the need to manually log in every day at midnight to secure a room for the following week.

The automation script is built using Python and Selenium, which allows it to interact with the website just like a human user would—filling in login details, selecting the preferred room, and submitting the booking request. It's designed to be run automatically every day via Windows Task Scheduler, ensuring that the room is booked at the earliest possible moment (typically at 12:00 AM, 7 days in advance).

Key Features:
Automated Booking Process: Automatically logs into the Carleton Library booking system and books a room based on the user's stored preferences.
Floor Selection: Users can choose between the Silent Floors (3rd or 5th) and the Conversational Floors (2nd or 4th).
Room Selection: A list of available rooms is shown based on the chosen floor. The user selects their preferred room.
Time Slot Selection: The user provides the start time for the room booking, and the script automatically books it for a default duration (e.g., 2 hours).
Saved Preferences: Once the script is run for the first time, it saves the user's credentials, floor, room, and time preferences, eliminating the need for input on future runs.
Designed for Automation: The script is intended to be used with Windows Task Scheduler to run automatically at a specified time (e.g., midnight) to ensure timely bookings.
Why This Exists:
Booking a study room at Carleton Library is competitive, especially since rooms can only be reserved exactly seven days in advance. To secure a room, students often have to manually log in at midnight when new rooms become available, which can be inconvenient. This automation script was created to solve that problem by handling the booking process automatically, allowing students to focus on their studies instead of remembering to book a room late at night.

Limitations:
The script is tailored specifically for the Carleton University Library booking system, so it may require adjustment if the website layout or booking process changes.
The program currently supports only single-room bookings, with default booking durations. More customization, like multiple time slots or longer durations, can be added with modifications.
