# 🧠 Convo AI Agent

An AI-powered chatbot that connects to your Google Calendar, allowing you to check for availability and book appointments using natural language.

This project provides a conversational interface to manage your Google Calendar. Instead of manually navigating through calendar grids, you can simply chat with the assistant.

For example, you can ask:
- "Are you free next Tuesday at 2 PM for a 30-minute meeting?"
- "Find a 1-hour slot for me next week for a project sync."

---

## ✨ Key Features

- **Natural Language Understanding**: Ask questions about your schedule in plain English.
- **Google Calendar Integration**: Securely connects to your Google Calendar to fetch real-time availability.
- **Check Availability**: Quickly find out if you are free at a specific date and time.
- **Book Appointments**: Create new events on your calendar directly through the chat interface.
- **Session Management**: Maintains conversation context for a coherent user experience.
- **Easy Configuration**: A simple sidebar form to set up your Google Calendar API credentials.

---

## 🛠 Built With

This project is powered by a modern Python stack:

- **FastAPI**: For the high-performance backend API.
- **Streamlit**: For the interactive frontend web app.
- **LangChain**: To orchestrate the language model and tools.
- **Google Calendar API**: For all calendar-related actions.
- **Uvicorn**: As the ASGI server for FastAPI.

---

## 🚀 Getting Started

To get a local copy up and running, follow these steps.

### ✅ Prerequisites

You need Python 3.8+ and pip installed. You will also need a Google account and a project set up in the Google Cloud Console.

---

### 📥 1. Clone the Repository

```bash
git clone [https://github.com/your_username/intelligent-calendar-assistant.git](https://github.com/your_username/intelligent-calendar-assistant.git)
cd intelligent-calendar-assistant
```

## Set Up a Virtual Environment and Install Dependencies

It's recommended to use a virtual environment to manage project dependencies.
```
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt
```

## 🔧 3. Configure Google Calendar API

To enable the assistant to access your Google Calendar, you need to provide your API credentials.

1. Go to the Google Cloud Console.
2. Create a new project or select an existing one.
3. In the navigation menu, go to APIs & Services > Library and enable the Google Calendar API.
4. Go to APIs & Services > OAuth consent screen.
5. Choose External for the User Type.
6. Fill in the required application details (app name, user support email, etc.).
7. On the Scopes page, add the following scope: https://www.googleapis.com/auth/calendar
8. On the Test users page, add the Google account email you will be using to test the application.
9. Go to APIs & Services > Credentials.
10. Click + CREATE CREDENTIALS and select OAuth client ID.
11. Select Desktop app as the Application type.
12. Download the JSON file for your credentials. You will get a client_id and client_secret from this file.

## 🔑 4. Get Your Refresh Token

1. Go to the Google OAuth 2.0 Playground.
2. Click the settings (⚙️) icon in the top-right.
3. Check Use your own OAuth credentials.
4. Paste your Client ID and Client Secret from the downloaded JSON file.
5. In Step 1, find and enter the scope: https://www.googleapis.com/auth/calendar
6. Click Authorize APIs.
7. Follow the prompts to grant permissions with your test Google account.
8. In Step 2, click Exchange authorization code for tokens.
9. Copy the Refresh Token that is displayed.
- This token is a long-lived credential that the application will use to access your calendar.

## ▶️ 5. Run the Application

You need to run the backend and frontend in two separate terminal windows.

# Terminal 1: Start the FastAPI Backend
```
uvicorn main:app --reload
```
This will start the backend server, usually at http://127.0.0.1:8000.

# Terminal 2: Run the Streamlit Frontend

```
streamlit run frontend.py
```
This will open the application in your default web browser.

## 6. Final Configuration in the App

Once the app is open, use the sidebar to enter:

- Client ID
- Client Secret
- Refresh Token

Click "Configure Google Calendar".

✅ You are now ready to start chatting with your calendar assistant!

## 💬 Usage
Simply type your requests into the chat input box. Here are a few examples:

- "Check my availability for next Monday at 10am."

- "Am I free for a 1-hour meeting tomorrow afternoon?"

- "Book a 30-minute 'Catch-up with Alex' for this Friday at 4 PM."

- "Find a 45-minute slot for a 'Design Review' next week."

