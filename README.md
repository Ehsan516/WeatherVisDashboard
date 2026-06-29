# 🌦Weather Data Visualisation Dashboard

A Streamlit dashboard that displays real-time weather data and 5-day forecasts using the OpenWeatherMap API.

## Features

- Current weather conditions (temperature, humidity, wind speed, pressure)
- 5-day temperature forecast chart
- Celsius / Fahrenheit toggle
- Auto-refresh at a configurable interval
- CSV export for forecast data

## Setup

### 1. Get an API key
Sign up at [openweathermap.org](https://openweathermap.org) and grab a free API key from your account dashboard. Note that new keys can take up to 2 hours to activate.

### 2. Create a `.env` file
In the project root directory, create a file named `.env` with the following:

```
OPENWEATHER_API_KEY=your_api_key_here
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

The dashboard will open automatically at `http://localhost:8501`.

## Notes

- The `.env` file is excluded from version control via `.gitignore` — you will need to create your own with your personal API key.
- The default city is set to London but can be changed in the sidebar.
