# frontend.py (Updated with Google Calendar Configuration input)
import streamlit as st
import requests
import uuid
import json

# --- Configuration ---
BACKEND_URL = "http://localhost:8000"

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="AI Calendar Assistant",
    page_icon="🗓️",
    layout="centered"
)

st.title("🗓️ AI Calendar Assistant")
st.markdown("I can help you check availability and book appointments on **Google Calendar**!")

# --- Initialize Session State ---
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
    print(f"New session created: {st.session_state.session_id}")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Google Calendar Configuration Section ---
st.sidebar.header("Google Calendar Setup")
st.sidebar.markdown(
    """
    To enable me to access your Google Calendar, you need to provide your API credentials.
    **Follow these steps to get your `refresh_token`, `client_id`, and `client_secret`:**
    
    1.  Go to [Google Cloud Console](https://console.cloud.google.com/).
    2.  Create/Select a project.
    3.  Enable the "Google Calendar API".
    4.  Go to "APIs & Services" > "OAuth consent screen". Configure it (select "External", fill details, add `https://www.googleapis.com/auth/calendar` scope, add your testing Google account as a "Test user").
    5.  Go to "APIs & Services" > "Credentials". Create "OAuth client ID" (select "Desktop app").
    6.  Download the JSON file for your credentials. Copy `client_id` and `client_secret` from there.
    7.  Go to [Google OAuth 2.0 Playground](https://developers.google.com/oauthplayground).
        * In "Step 1", enter `https://www.googleapis.com/auth/calendar` and click "Authorize APIs".
        * Grant permissions with your test Google account.
        * In "Step 2", click "Exchange authorization code for tokens".
        * **Copy the `Refresh token` displayed.**
    
    Paste these values below:
    """
)

with st.sidebar.form("calendar_config_form"):
    refresh_token = st.text_input("Refresh Token", type="password")
    client_id = st.text_input("Client ID")
    client_secret = st.text_input("Client Secret", type="password")
    
    submitted = st.form_submit_button("Configure Google Calendar")
    
    if submitted:
        if not refresh_token or not client_id or not client_secret:
            st.sidebar.error("All fields are required for Google Calendar configuration.")
        else:
            config_payload = {
                "refresh_token": refresh_token,
                "client_id": client_id,
                "client_secret": client_secret
            }
            try:
                # Use a custom header to pass session_id for configuration endpoint
                headers = {"X-Session-ID": st.session_state.session_id}
                config_response = requests.post(f"{BACKEND_URL}/configure_calendar", json=config_payload, headers=headers)
                config_response.raise_for_status() # Raise an exception for HTTP errors
                
                st.sidebar.success(config_response.json().get("message", "Configuration successful!"))
                st.session_state.google_calendar_configured = True # Set a flag
            except requests.exceptions.RequestException as e:
                error_detail = ""
                if config_response.status_code == 400 and config_response.content:
                    try:
                        error_detail = config_response.json().get("detail", str(e))
                    except json.JSONDecodeError:
                        error_detail = config_response.text
                st.sidebar.error(f"Failed to configure Google Calendar: {error_detail}")
                st.session_state.google_calendar_configured = False
            except Exception as e:
                st.sidebar.error(f"An unexpected error occurred during configuration: {e}")
                st.session_state.google_calendar_configured = False

# --- Display Chat History ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# --- Chat Input ---
if user_input := st.chat_input("How can I help you with your calendar today?"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    payload = {
        "session_id": st.session_state.session_id,
        "message": user_input
    }

    with st.spinner("Thinking..."):
        try:
            response = requests.post(f"{BACKEND_URL}/chat", json=payload)
            response.raise_for_status()
            
            ai_response = response.json()
            ai_reply = ai_response.get("reply", "No reply from AI.")
            
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})
            with st.chat_message("assistant"):
                st.write(ai_reply)

        except requests.exceptions.ConnectionError:
            error_message = "Could not connect to the backend API. Please ensure the FastAPI backend is running at " \
                            f"{BACKEND_URL}. Run `uvicorn main:app --reload` in your terminal."
            st.error(error_message)
            st.session_state.messages.append({"role": "assistant", "content": error_message})
            with st.chat_message("assistant"):
                st.error(error_message)
        except requests.exceptions.RequestException as e:
            error_message_from_backend = f"An error occurred: {e}"
            if response.status_code == 400 and response.content:
                try:
                    backend_error_detail = response.json().get("detail", response.text)
                    error_message_from_backend = f"Backend Error: {backend_error_detail}"
                except json.JSONDecodeError:
                    backend_error_detail = response.text
                    error_message_from_backend = f"Backend Error: {backend_error_detail}"

            st.error(error_message_from_backend)
            st.session_state.messages.append({"role": "assistant", "content": error_message_from_backend})
            with st.chat_message("assistant"):
                st.error(error_message_from_backend)
        except Exception as e:
            error_message = f"An unexpected error occurred: {e}"
            st.error(error_message)
            st.session_state.messages.append({"role": "assistant", "content": error_message})
            with st.chat_message("assistant"):
                st.error(error_message)

# --- Instructions for Running ---
st.sidebar.header("How to Run This App")
st.sidebar.markdown("""
1.  **Complete Google Calendar Setup** (Above section).
2.  **Ensure Backend is Running:**
    Open your terminal, navigate to the directory containing `main.py`, and run:
    ```bash
    uvicorn main:app --reload
    ```
    This will start the FastAPI backend, typically on `http://127.0.0.1:8000`.

3.  **Install Frontend Dependencies:**
    Make sure you have Streamlit, requests, and google API libraries installed. From your terminal:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Streamlit Frontend:**
    Open a **new** terminal window (keep the backend terminal running), navigate to the directory containing `frontend.py`, and run:
    ```bash
    streamlit run frontend.py
    ```
    This will open the Streamlit app in your web browser.
""")

st.sidebar.markdown(f"**Current Session ID:** `{st.session_state.session_id}`")
st.sidebar.markdown("This ID ensures your conversation context is maintained.")
