# convo-ai-agent
An AI-powered chatbot that connects to your Google Calendar, allowing you to check for availability and book appointments using natural language.

This project provides a conversational interface to manage your Google Calendar. Instead of manually navigating through calendar grids, you can simply chat with the assistant. For example, you can ask, "Are you free next Tuesday at 2 PM for a 30-minute meeting?" or "Find a 1-hour slot for me next week for a project sync." The assistant will check your calendar and can even create new events based on your requests.

It uses a powerful combination of a FastAPI backend to handle the AI logic and Google Calendar API integration, and a Streamlit frontend to provide a seamless and interactive user experience.

Key Features:
Natural Language Understanding: Ask questions about your schedule in plain English.

Google Calendar Integration: Securely connects to your Google Calendar to fetch real-time availability.

Check Availability: Quickly find out if you are free at a specific date and time.

Book Appointments: Create new events on your calendar directly through the chat interface.

Session Management: Maintains conversation context for a coherent user experience.

Easy Configuration: A simple sidebar form to set up your Google Calendar API credentials.

Built With
This project is powered by a modern Python stack:

FastAPI: For the high-performance backend API.

Streamlit: For the interactive frontend web app.

LangChain: To orchestrate the language model and tools.

Google Calendar API: For all calendar-related actions.

Uvicorn: As the ASGI server for FastAPI.

Getting Started
To get a local copy up and running, follow these steps.

Prerequisites
You need Python 3.8+ and pip installed. You will also need a Google account and a project set up in the Google Cloud Console.

1. Clone the Repository
git clone [https://github.com/your_username/intelligent-calendar-assistant.git](https://github.com/your_username/intelligent-calendar-assistant.git)
cd intelligent-calendar-assistant

2. Set Up a Virtual Environment and Install Dependencies
It's recommended to use a virtual environment to manage project dependencies.

# Create a virtual environment
python -m venv venv

# Activate it (on Windows)
venv\Scripts\activate
# Or on macOS/Linux
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt

(You will need to create a requirements.txt file containing streamlit, fastapi, uvicorn, requests, langchain, google-api-python-client, google-auth-httplib2, and google-auth-oauthlib)

3. Configure Google Calendar API
To enable the assistant to access your Google Calendar, you need to provide your API credentials.

Go to the Google Cloud Console.

Create a new project or select an existing one.

In the navigation menu, go to APIs & Services > Library and enable the "Google Calendar API".

Go to APIs & Services > OAuth consent screen.

Choose External for the User Type.

Fill in the required application details (app name, user support email, etc.).

On the "Scopes" page, add the .../auth/calendar scope (https://www.googleapis.com/auth/calendar).

On the "Test users" page, add the Google account email you will be using to test the application.

Go to APIs & Services > Credentials.

Click + CREATE CREDENTIALS and select OAuth client ID.

Select Desktop app as the Application type.

Download the JSON file for your credentials. You will get a client_id and client_secret from this file.

Go to the Google OAuth 2.0 Playground.

In the top-right settings cog, check "Use your own OAuth credentials" and paste your Client ID and Client Secret.

In "Step 1", find and enter the Google Calendar API v3 scope: https://www.googleapis.com/auth/calendar and click Authorize APIs.

Follow the prompts to grant permissions with your test Google account.

In "Step 2", click Exchange authorization code for tokens.

Copy the Refresh token that is displayed. This is a long-lived token that the application will use.

4. Run the Application
You need to run the backend and frontend in two separate terminal windows.

Terminal 1: Start the FastAPI Backend

uvicorn main:app --reload

This will start the backend server, usually at http://127.0.0.1:8000.

Terminal 2: Run the Streamlit Frontend

streamlit run frontend.py

This will open the application in your web browser.

5. Final Configuration in the App
Once the app is open, use the sidebar to enter the Refresh Token, Client ID, and Client Secret you obtained earlier.

Click "Configure Google Calendar".

You are now ready to start chatting with your calendar assistant!

Usage
Simply type your requests into the chat input box. Here are a few examples:

"Check my availability for next Monday at 10am."

"Am I free for a 1-hour meeting tomorrow afternoon?"

"Book a 30-minute 'Catch-up with Alex' for this Friday at 4 PM."

"Find a 45-minute slot for a 'Design Review' next week."

Project Structure
.
├── main.py         # FastAPI backend logic, AI agent, and tool definitions
├── frontend.py     # Streamlit frontend UI and chat interface
└── requirements.txt  # Project dependencies

License
Distributed under the MIT License. See LICENSE for more information.
