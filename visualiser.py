import plotly.express as px
import pandas as pd


def plot_temperature_trend(df: pd.DataFrame, unit_symbol: str) -> px.line:
    """
    create a line plot for temperature trend over time.

    args:
        df: DataFrame with 'Date' and 'Temperature' columns
        unit_symbol: Temperature unit symbol (°C or °F)

    Returns:
        Plotly line figure
    """
    fig = px.line(
        df,
        x="Date",
        y="Temperature",
        title="Temperature Trend (5-Day Forecast)",
        labels={"Temperature": f"Temperature ({unit_symbol})"}
    )
    fig.update_layout(
        xaxis_title="Date & Time",
        yaxis_title=f"Temperature ({unit_symbol})",
        template="plotly_white"
    )
    return fig


def plot_weather_metrics(df: pd.DataFrame, unit_symbol: str) -> px.bar:
    """
    Create a bar plot for weather metrics (humidity, wind speed).

    Args:
        df: DataFrame with 'Date', 'Humidity', and 'Wind Speed' columns
        unit_symbol: Temperature unit symbol (°C or °F)

    Returns:
        Plotly bar figure
    """
    fig = px.bar(
        df,
        x="Date",
        y=["Humidity", "Wind Speed"],
        title="Humidity and Wind Speed Trends",
        barmode="group"
    )
    fig.update_layout(
        xaxis_title="Date & Time",
        yaxis_title="Value",
        template="plotly_white"
    )
    return fig