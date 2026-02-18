"""Module providing streamlit to create webapp"""
import streamlit as st
from weather import get_weather

st.set_page_config(
    page_title="Real-time Weather App",
    page_icon="☀️",
    layout="centered"
)

st.title("☀️ Real-time Weather App")
st.write("Live weather data using OpenWeatherMap API")

city = st.text_input("Enter City Name", placeholder="e.g. Mumbai")

if st.button("Get Weather"):
    if not city:
        st.warning("Please enter a city name.")
    else:
        with st.spinner("Fetching live weather data..."):
            data = get_weather(city)
        if not data:
            st.error("Hmm… couldn’t find that city 🌍")
        else:
            st.success(f"Weather in {data['name']}")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("🌡 Temperature (°C)", data["main"]["temp"])
                st.metric("🤔 Feels Like (°C)", data["main"]["feels_like"])
                st.metric("💧 Humidity (%)", data["main"]["humidity"])
            with col2:
                st.metric("🌬 Wind Speed (m/s)", data["wind"]["speed"])
                st.metric(
                    "☁ Condition",
                    data["weather"][0]["description"].title()
                )
