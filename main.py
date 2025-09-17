"""
Bright Data Web Unlocker API Demo

This Streamlit app provides a simple frontend to interact with the Bright Data Web Unlocker API.
Users can input their zone and target URL, and view the API response in the browser.

Requirements:
- streamlit
- requests
- python-dotenv

Environment Variables:
- BRIGHT_DATA_API_TOKEN: Your Bright Data API token (set in .env file)
"""

import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the title of the Streamlit app
st.title("Bright Data Web Unlocker API Demo")

# Retrieve API token from environment variables
api_token = os.getenv('BRIGHT_DATA_API_TOKEN')

# Input fields for zone and URL
zone = st.text_input("Zone", "web_unlocker_demo1")
url = st.text_input("URL", "https://geo.brdtest.com/welcome.txt?product=unlocker&method=api")

# When the user clicks the button, send the API request
if st.button("Send Request"):
    # Prepare request headers
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    # Prepare request payload
    data = {
        "zone": zone,
        "url": url,
        "format": "raw"
    }
    try:
        # Send POST request to Bright Data API
        response = requests.post(
            "https://api.brightdata.com/request",
            json=data,
            headers=headers
        )
        # Display the API response in the app
        st.subheader("API Response:")
        st.code(response.text)
    except Exception as e:
        # Display error message if request fails
        st.error(f"Error: {e}")