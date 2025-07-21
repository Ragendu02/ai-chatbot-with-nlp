import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections


try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


pairs = [
    [
        r"(hi|hello|hey)",
        ["Hello! 👋 How can I help you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"(.*) your name ?",
        ["I’m AI Chatbot 🤖, your virtual assistant!"]
    ],
    [
        r"(.*) help (.*)",
        ["Sure! I’m here to help. What do you need assistance with?"]
    ],
    [
        r"(.*) (location|city)",
        ["I’m based in the cloud ☁️ but I can help you anywhere!"]
    ],
    [
        r"quit",
        ["Bye-bye! 👋 Take care."]
    ],
    [
        r"(.*)",
        ["I’m not sure about that 🤔, but I’ll try to improve!"]
    ]
]

chatbot = Chat(pairs, reflections)


#  Streamlit UI
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

# Title with dark theme hint
st.markdown(
    """
    <style>
    body { background-color: #0e1117; color: #fafafa; }
    .stButton>button {
        background-color: #262730;
        color: white;
        border-radius: 8px;
        border: 1px solid #444;
    }
    .stTextInput>div>div>input {
        background-color: #1e1e1e;
        color: #fafafa;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🤖 AI Chatbot")
st.caption("💡 *Ask me anything!*")

# Maintain session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display previous messages
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# Input box
user_input = st.chat_input("Type your message here...")

if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get chatbot response
    response = chatbot.respond(user_input)

    # Append bot response
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Force rerun to update the interface
    st.rerun()

# Optional reset button
if st.button("🔄 Reset Chat"):
    st.session_state.messages = []
    st.rerun()
