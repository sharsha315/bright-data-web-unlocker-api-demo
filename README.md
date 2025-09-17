# Bright Data Web Unlocker API Demo


## Introduction


**About Unlocker API:**

- Simplifies web data collection by handling proxy and unblocking infrastructure for you
- Send a single API request with the target website and receive clean HTML or JSON in response
- Uses intelligent algorithms to manage proxies, headers, fingerprinting, CAPTCHAs, and more
- Emulates real-user behavior to bypass sophisticated detection methods
- Ideal for teams needing scalable scraping solutions without building their own infrastructure
- Pay only for successful requests

This project provides a Streamlit-based frontend to interact with the Bright Data Web Unlocker API.

## Quick Start Guide

To quickly set up and start using Bright Data's Unlocker API:

- **Sign in** to your Bright Data account.
- Go to **My Zones** and select **Unlocker API** > **Get started**.
- **Assign a name** to your Unlocker API zone (note: the name cannot be changed later).
- Click **Add** to create your Unlocker API zone.
- Go to **Account Settings** and select **User Management**, under
**API Keys**, create an API Key.

Once your zone is created, you can use the API token and zone name in this demo app to start collecting data.

## Features
- Input your Bright Data zone and target URL
- Send requests to the Bright Data Web Unlocker API
- View API responses in a user-friendly web interface

## Setup Instructions

1. **Clone the repository**
	```bash
	git clone https://github.com/<your-username>/bright-data-web-unlocker-api-demo.git
	cd bright-data-web-unlocker-api-demo
	```

2. **Create and activate a Python virtual environment**
	```bash
	python3 -m venv venv
	source venv/bin/activate
	```

3. **Install dependencies**
	```bash
	pip install -r requirements.txt
	```

4. **Configure environment variables**
	- Create a `.env` file in the project root:
	  ```env
	  BRIGHT_DATA_API_TOKEN=your_api_token_here
	  ```

5. **Run the Streamlit app**
	```bash
	streamlit run main.py
	```

6. **Usage**
	- Open the provided local URL in your browser
	- Enter your zone and target URL
	- Click "Send Request" to view the API response

## Requirements
- Python 3.7+
- `requests`, `streamlit`, `python-dotenv`

## License
This project is licensed under the MIT License.