import streamlit as st
import random
from datetime import date

# ------------------- Data -------------------

challenges = [
    "Write down 3 things you learned today.",
    "Identify a mistake you made and what you learned from it.",
    "Try something you've been avoiding due to fear of failure.",
    "Give constructive feedback to someone kindly.",
    "Reflect on how you handled a recent challenge.",
    "Compliment someone genuinely.",
    "Replace a negative thought with a positive one.",
    "Write a gratitude journal entry.",
    "Practice a new skill for 30 minutes.",
    "Read or watch something inspiring."
]

quotes = [
    "“It's not that I'm so smart, it's just that I stay with problems longer.” – Albert Einstein",
    "“Failure is not the opposite of success; it's part of success.” – Arianna Huffington",
    "“Challenges are what make life interesting.” – Joshua J. Marine",
    "“Success is the ability to go from one failure to another with no loss of enthusiasm.” – Winston Churchill",
    "“Believe you can and you're halfway there.” – Theodore Roosevelt",
    "“Whether you think you can or you think you can’t, you’re right.” – Henry Ford",
    "“Strive for progress, not perfection.” – Unknown"
]

# ------------------- App UI -------------------

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱")

st.title("🌱 Growth Mindset Challenge")
st.subheader("Empower yourself with small, consistent efforts!")

today = date.today()
st.markdown(f"**Today's Date:** {today.strftime('%A, %d %B %Y')}")

# Show daily challenge
random.seed(today.toordinal())  # Ensures same challenge for the same day
challenge = random.choice(challenges)
st.info(f"**Today's Challenge:**\n{challenge}")

# Show motivational quote
quote = random.choice(quotes)
st.success(f"💬 **Motivational Quote:**\n_{quote}_")

# Progress tracking
st.markdown("---")
st.header("📝 Challenge Tracker")

if "completed_days" not in st.session_state:
    st.session_state.completed_days = []

if st.button("✅ Mark Today's Challenge as Completed"):
    if today not in st.session_state.completed_days:
        st.session_state.completed_days.append(today)
        st.success("Challenge marked as completed! Well done! 🎉")
    else:
        st.warning("You already completed today’s challenge!")

st.markdown("### 📆 Completed Days:")
if st.session_state.completed_days:
    for d in sorted(st.session_state.completed_days):
        st.markdown(f"- {d.strftime('%A, %d %B %Y')}")
else:
    st.markdown("No challenges completed yet.")

# Footer
st.markdown("---")
st.caption("Created with ❤️ using Streamlit")

