import streamlit as st

st.title("Growth Mindset Challenge")

st.write("Welcome to the Growth Mindset App!")
st.write("Here, you can learn how to develop a growth mindset and achieve your goals.")

name = st.text_input("Enter your name:")

if st.button("Submit"):
    st.write(f"Hello {name}! Let's grow together!")

# Daily Tips Section
st.header("Daily Growth Mindset Tips")
tips = [
    "Embrace challenges as opportunities to learn.",
    "Learn from your mistakes and keep improving.",
    "Believe in your ability to grow and succeed."
]
for tip in tips:
    st.write(f"- {tip}")

# Feedback Section
st.header("Give Us Feedback")
feedback = st.text_area("How can we improve this app?")
if st.button("Submit Feedback"):
    st.write("Thank you for your feedback!")