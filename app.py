import streamlit as st
import pandas as pd
from pdf_generator import create_roadmap_pdf
from heatmap import generate_heatmap_data
from streamlit_calendar import calendar
from chatbot import ask_ai_mentor
from grok_ai import generate_roadmap

from recommender import recommend_questions

from utils import (
    fetch_user_data,
    fetch_recent_submissions
)

from charts import (
    create_chart_data,
    show_pie_chart,
    show_bar_chart
)

from ai_engine import (
    analyze_user,
    calculate_readiness
)

# ---------------- PAGE STATE ---------------- #

if "page" not in st.session_state:
    st.session_state.page = "dashboard"

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="LeetCode Tracker",
    page_icon="🚀",
    layout="wide"
)

# ---------------- LOAD CSS ---------------- #

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ---------------- SIDEBAR ---------------- #

st.sidebar.markdown("## 🚀 Dashboard Controls")

username = st.sidebar.text_input(
    "Enter LeetCode Username",
    placeholder="e.g. tourist"
)

# =========================================================
# ================= DASHBOARD PAGE ========================
# =========================================================

if st.session_state.page == "dashboard":

    # ---------------- HERO SECTION ---------------- #

    st.title("🚀 LeetCode Tracker Dashboard")

    st.divider()

    st.markdown("""
    <div style='margin-bottom:30px;'>

    <h3 style='color:#60a5fa;'>
    📈 Track • Analyze • Improve
    </h3>

    <p style='font-size:18px;color:#cbd5e1;'>
    A modern AI-powered dashboard for monitoring your LeetCode journey.
    </p>

    </div>
    """, unsafe_allow_html=True)

    # ---------------- FETCH DATA ---------------- #

    if username:

        data = fetch_user_data(username)
        recent_data = fetch_recent_submissions(username)

        if data:

            # ---------------- PROFILE SECTION ---------------- #

            st.subheader("👤 Profile")

            colA, colB = st.columns([1, 4])

            with colA:

                st.image(
                    data.get(
                        "avatar",
                        "https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png"
                    ),
                    width=130
                )

            with colB:

                st.markdown(f"# {username}")

                st.markdown(f"""
🌍 **Global Rank:** {data.get('ranking', 'N/A')}

🔥 **Reputation:** {data.get('reputation', 0)}

🚀 **Total Solved:** {data.get('totalSolved', 0)}
""")

            # ---------------- READINESS SCORE ---------------- #

            st.subheader("🎯 Interview Readiness")

            score = calculate_readiness(data)

            st.progress(score / 100)

            st.markdown(f"## {score}% Ready")

            # ---------------- OVERALL STATISTICS ---------------- #

            st.subheader("📊 Overall Statistics")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Total Solved",
                data.get('totalSolved', 0)
            )

            col2.metric(
                "Easy",
                data.get('easySolved', 0)
            )

            col3.metric(
                "Medium",
                data.get('mediumSolved', 0)
            )

            col4.metric(
                "Hard",
                data.get('hardSolved', 0)
            )

            # ---------------- CHARTS ---------------- #

            chart_data = create_chart_data(data)

            col5, col6 = st.columns(2)

            with col5:
                show_pie_chart(chart_data)

            with col6:
                show_bar_chart(chart_data)

            # ---------------- ACTIVITY HEATMAP ---------------- #

            st.subheader("📅 Coding Activity Heatmap")

            events = generate_heatmap_data()

            calendar(events=events)

            # ---------------- ADDITIONAL INFORMATION ---------------- #

            st.subheader("🏆 Additional Information")

            col7, col8, col9 = st.columns(3)

            col7.metric(
                "Ranking",
                data.get('ranking', "N/A")
            )

            col8.metric(
                "Contribution Points",
                data.get('contributionPoint', "N/A")
            )

            col9.metric(
                "Reputation",
                data.get('reputation', "N/A")
            )

            # ---------------- AI INSIGHTS ---------------- #

            st.subheader("🧠 AI Insights")

            insights = analyze_user(data)

            for insight in insights:

                if insight["type"] == "warning":

                    st.warning(insight["message"])

                elif insight["type"] == "info":

                    st.info(insight["message"])

                else:

                    st.success(insight["message"])

            # ---------------- QUESTION RECOMMENDER ---------------- #

            st.subheader("📚 Recommended Questions")

            questions = recommend_questions(data)

            for q in questions:

                st.markdown(f"✅ {q}")

            # ---------------- AI ROADMAP BUTTON ---------------- #

            st.subheader("🤖 AI Roadmap Generator")

            st.info(
                "Generate a personalized AI-powered roadmap."
            )

            if st.button("🚀 Generate Personalized AI Roadmap"):

                st.session_state.page = "roadmap"

                st.rerun()

            # ---------------- RECENT SUBMISSIONS ---------------- #

            st.subheader("📝 Recent Submissions")

            if recent_data and isinstance(recent_data, list):

                submission_list = []

                for item in recent_data[:10]:

                    submission_list.append({
                        "Title": item.get("title", "N/A"),
                        "Status": "Accepted",
                        "Language": item.get("lang", "N/A"),
                        "Timestamp": item.get("timestamp", "N/A")
                    })

                submission_df = pd.DataFrame(submission_list)

                st.dataframe(
                    submission_df,
                    width='stretch'
                )

            else:

                st.info("No recent submissions found.")

        else:

            st.error("❌ User not found or API unavailable")

# =========================================================
# ================= ROADMAP PAGE ==========================
# =========================================================

elif st.session_state.page == "roadmap":

    st.title("🤖 Personalized AI Roadmap")

    st.divider()

    if username:

        data = fetch_user_data(username)

        if data:

            st.success(f"Profile Loaded: {username}")

            st.markdown(f"""
### 📊 Current Stats

- Total Solved: {data.get('totalSolved', 0)}
- Easy Solved: {data.get('easySolved', 0)}
- Medium Solved: {data.get('mediumSolved', 0)}
- Hard Solved: {data.get('hardSolved', 0)}
""")
            # ---------------- AI CHAT MENTOR ---------------- #

            st.divider()

            st.subheader("💬 AI Mentor Chat")

            question = st.text_input(
                "Ask anything about DSA, interviews, or preparation"
            )

            if st.button("Ask AI Mentor"):
                with st.spinner("Thinking..."):
                    answer = ask_ai_mentor(question)

                st.success("AI Mentor Response")

                st.markdown(answer)
            # ---------------- GENERATE ROADMAP ---------------- #

            with st.spinner("Generating roadmap..."):

                roadmap = generate_roadmap(data)

            st.success("Roadmap Generated Successfully ✅")

            st.markdown("## 📌 Your AI Roadmap")

            st.markdown(roadmap)

            # ---------------- PDF EXPORT ---------------- #

            pdf_file = create_roadmap_pdf(
                username,
                roadmap
            )

            with open(pdf_file, "rb") as pdf:

                st.download_button(
                    label="📄 Download Roadmap PDF",
                    data=pdf,
                    file_name=pdf_file,
                    mime="application/pdf"
                )

            # ---------------- BACK BUTTON ---------------- #

            if st.button("⬅ Back to Dashboard"):
                st.session_state.page = "dashboard"

                st.rerun()

            