import pandas as pd
import plotly.express as px
import streamlit as st


# ---------------- CREATE CHART DATA ---------------- #

def create_chart_data(data):

    chart_data = pd.DataFrame({
        "Difficulty": ["Easy", "Medium", "Hard"],
        "Solved": [
            data.get('easySolved', 0),
            data.get('mediumSolved', 0),
            data.get('hardSolved', 0)
        ]
    })

    return chart_data


# ---------------- PIE CHART ---------------- #

def show_pie_chart(chart_data):

    if chart_data["Solved"].sum() > 0:

        fig = px.pie(
            chart_data,
            names='Difficulty',
            values='Solved',
            title='Difficulty Breakdown',
            hole=0.4
        )

        st.plotly_chart(fig, width='stretch')

    else:

        st.info("No solved problems data available.")


# ---------------- BAR CHART ---------------- #

def show_bar_chart(chart_data):

    if chart_data["Solved"].sum() > 0:

        fig = px.bar(
            chart_data,
            x='Difficulty',
            y='Solved',
            title='Solved Problems'
        )

        st.plotly_chart(fig, use_container_width=True)

    else:

        st.info("Bar chart unavailable.")