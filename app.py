import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from data_fetcher import get_current_weather, get_forecast
from visualiser import plot_temperature_trend, plot_weather_metrics
from dotenv import load_dotenv
import os

#environment variables
load_dotenv() #.env is where my api key is kept, you can add yours if you pulled form my github
API_KEY = os.getenv("OPENWEATHER_API_KEY")

#confiugring Streamlit page
st.set_page_config(page_title="Weather Dashboard", layout="wide", initial_sidebar_state="expanded")


def main():
    st.title("🌦️ Weather Data Visualization Dashboard")
    #sidebar for user inputs
    with st.sidebar:
        st.header("Settings")
        city = st.text_input("Enter City Name", value="London")
        unit = st.selectbox("Temperature Unit", ["Celsius (°C)", "Fahrenheit (°F)"])
        refresh_interval = st.slider("Auto-refresh Interval (minutes)", 1, 60, 5)
        theme = st.selectbox("Theme", ["Light", "Dark"])

        if theme == "Dark":
            st.markdown(
                """
                <style>
                .stApp { background-color: #1e1e1e; color: white; }
                .sidebar .sidebar-content { background-color: #2e2e2e; }
                </style>
                """, unsafe_allow_html=True
            )

        if st.button("Refresh Data"):
            st.cache_data.clear()

    #convert selected unit to API format
    unit_api = "metric" if unit == "Celsius (°C)" else "imperial"
    unit_symbol = "°C" if unit == "Celsius (°C)" else "°F"

    #main content
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader(f"Current Weather in {city}")
        try:
            current_weather = get_current_weather(city, API_KEY, unit_api)
            if current_weather:
                temp = current_weather["main"]["temp"]
                feels_like = current_weather["main"]["feels_like"]
                humidity = current_weather["main"]["humidity"]
                pressure = current_weather["main"]["pressure"]
                wind_speed = current_weather["wind"]["speed"]
                weather_desc = current_weather["weather"][0]["description"]
                sunrise = datetime.fromtimestamp(current_weather["sys"]["sunrise"]).strftime("%H:%M")
                sunset = datetime.fromtimestamp(current_weather["sys"]["sunset"]).strftime("%H:%M")

                # Display current weather
                st.metric("Temperature", f"{temp:.1f} {unit_symbol}", f"Feels like: {feels_like:.1f} {unit_symbol}")
                st.metric("Humidity", f"{humidity}%")
                st.metric("Wind Speed", f"{wind_speed} {'m/s' if unit_api == 'metric' else 'mph'}")
                st.metric("Pressure", f"{pressure} hPa")
                st.write(f"Condition: {weather_desc.capitalize()}")
                st.write(f"Sunrise: {sunrise} | Sunset: {sunset}")

                # Weather icon (using emoji for simplicity)
                icon_map = {"clear": "☀️", "clouds": "☁️", "rain": "🌧️", "snow": "❄️"}
                icon = icon_map.get(current_weather["weather"][0]["main"].lower(), "🌦️")
                st.markdown(f"## {icon}")

            else:
                st.error("City not found. Please check the spelling or try another city.")
        except Exception as e:
            st.error(f"Error fetching weather data: {str(e)}")

    with col2:
        st.subheader("5-Day Forecast")
        try:
            forecast_data = get_forecast(city, API_KEY, unit_api)
            if forecast_data:
                df_forecast = pd.DataFrame([
                    {
                        "Date": datetime.fromtimestamp(item["dt"]).strftime("%Y-%m-%d %H:%M"),
                        "Temperature": item["main"]["temp"],
                        "Humidity": item["main"]["humidity"],
                        "Wind Speed": item["wind"]["speed"],
                    }
                    for item in forecast_data["list"]
                ])

                # Plot temperature trend
                fig_temp = plot_temperature_trend(df_forecast, unit_symbol)
                st.plotly_chart(fig_temp, use_container_width=True)

                # Display forecast table
                if st.checkbox("Show Forecast Table"):
                    st.dataframe(df_forecast.style.format({"Temperature": f"{{:.1f}} {unit_symbol}"}))

                # Export options
                if st.button("Export Forecast as CSV"):
                    csv = df_forecast.to_csv(index=False)
                    st.download_button("Download CSV", csv, f"{city}_forecast.csv", "text/csv")

            else:
                st.error("Unable to fetch forecast data.")
        except Exception as e:
            st.error(f"Error fetching forecast data: {str(e)}")

    #refreshes automatically
    st.write(f"Data will auto-refresh every {refresh_interval} minutes.")
    st.markdown(
        f"""
        <meta http-equiv="refresh" content="{refresh_interval * 60}">
        """, unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()