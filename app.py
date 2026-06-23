"""
Day 4: Streamlit chat interface for our Intent-Based Customer Support Chatbot.

Run this with:  streamlit run app.py
"""
import streamlit as st
from chatbot import chatbot_reply

st.set_page_config(page_title="Customer Support Chatbot", page_icon="💬")

st.title("💬 Customer Support Chatbot")
st.caption("An intent-classification chatbot built with TF-IDF + Logistic Regression")

# --- Session state: this is how Streamlit "remembers" things between interactions ---
# Without this, the chat history would reset every time you send a message,
# because Streamlit re-runs the whole script top-to-bottom on every interaction.
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi there! How can I help you today?"}
    ]

# --- Display all past messages ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# --- Chat input box at the bottom ---
user_input = st.chat_input("Type your message here...")

if user_input:
    # 1. Show the user's message immediately
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # 2. Get the bot's reply using YESTERDAY's chatbot logic
    intent, confidence, reply = chatbot_reply(user_input)

    # 3. Show the bot's reply
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
        # Small debug info - useful while building, you can remove this later
        st.caption(f"Detected intent: `{intent}` | Confidence: {confidence*100:.1f}%")

# --- Sidebar: a little "about" panel, nice touch for a demo ---
with st.sidebar:
    st.header("About this bot")
    st.write(
        "This chatbot classifies customer messages into intents "
        "(order status, refunds, complaints, etc.) using TF-IDF "
        "text vectorization and a Logistic Regression classifier."
    )
    st.write("Supported intents:")
    st.write("- Greeting\n- Order Status\n- Refund Request\n- Complaint\n- Shipping Time\n- Goodbye\n- Fallback")
    if st.button("Clear conversation"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi there! How can I help you today?"}
        ]
        st.rerun()
