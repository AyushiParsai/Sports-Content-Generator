import streamlit as st
from google import genai
import os

# ================= CONFIG =================
API_KEY =
client = genai.Client(api_key=API_KEY)

st.set_page_config(
    page_title="Sports AI Studio",
    page_icon="🏆",
    layout="wide"
)

# ================= CLEAN PROFESSIONAL UI =================
st.markdown("""
<style>

/* Hide default Streamlit elements */
header {visibility:hidden;}
footer {visibility:hidden;}
div[data-testid="stToolbar"] {display:none;}

/* App Background */
.stApp {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    font-family: 'Segoe UI', sans-serif;
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0f172a;
    color: white;
}

/* Floating Sports Icons */
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-15px); }
    100% { transform: translateY(0px); }
}

.sports-animation {
    position: fixed;
    right: 60px;
    top: 120px;
    font-size: 36px;
    opacity: 0.12;
    animation: float 4s ease-in-out infinite;
}

/* Main Layout Wrapper */
.main-wrapper {
    max-width: 1000px;
    margin: auto;
    padding-top: 40px;
}

/* Title */
.title {
    font-size: 38px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    color: #9ca3af;
    margin-bottom: 30px;
}

/* Buttons */
.stButton>button {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    color: white;
    padding: 8px 18px;
    transition: 0.2s;
}

.stButton>button:hover {
    background: rgba(255,255,255,0.15);
}

/* Chat bubbles */
.chat-user {
    background: rgba(255,255,255,0.1);
    padding: 12px 16px;
    border-radius: 10px;
    margin-bottom: 10px;
}

.chat-ai {
    background: rgba(255,255,255,0.05);
    padding: 12px 16px;
    border-radius: 10px;
    margin-bottom: 10px;
}

/* ================= CLEAN STRUCTURED INPUT ================= */

/* Remove outer wrapper background */
div[data-testid="stChatInput"] {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
}

/* Style real input field */
div[data-testid="stChatInput"] textarea {
    background: #111827 !important;
    color: #ffffff !important;
    border-radius: 16px !important;
    border: 1px solid #334155 !important;
    padding: 14px 18px !important;
    font-size: 15px !important;
    caret-color: #ffffff !important;
}

/* Placeholder */
div[data-testid="stChatInput"] textarea::placeholder {
    color: #9ca3af !important;
}

/* Remove red focus border */
div[data-testid="stChatInput"] textarea:focus {
    outline: none !important;
    box-shadow: none !important;
    border: 1px solid #475569 !important;
}

</style>

<div class="sports-animation">⚽🏏🏀</div>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
with st.sidebar:
    st.markdown("## 🏆 Sports AI Studio")
    st.markdown("Generate professional sports content instantly.")
    st.divider()

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.caption("© 2026 Ayushi Parsai")

# ================= MAIN =================
st.markdown("<div class='main-wrapper'>", unsafe_allow_html=True)

st.markdown("<div class='title'>Sports Content AI Studio</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Generate match reports, player insights & sports media content in seconds.</div>", unsafe_allow_html=True)

# Quick Buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Match Report"):
        st.session_state.quick_prompt = "Generate a professional cricket match report."

with col2:
    if st.button("Player Analysis"):
        st.session_state.quick_prompt = "Generate a detailed football player analysis."

with col3:
    if st.button("Breaking News"):
        st.session_state.quick_prompt = "Write a breaking sports news article."

with col4:
    if st.button("Social Caption"):
        st.session_state.quick_prompt = "Create an engaging sports social media caption."

# ================= SESSION =================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "quick_prompt" in st.session_state:
    user_input = st.session_state.quick_prompt
    del st.session_state.quick_prompt
else:
    user_input = None

# ================= CHAT =================
if st.session_state.messages:
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(
                f"<div class='chat-user'><b>You:</b><br>{msg['content']}</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div class='chat-ai'><b>Sports AI:</b><br>{msg['content']}</div>",
                unsafe_allow_html=True
            )

# ================= INPUT =================
typed_input = st.chat_input("Generate match report, player stats, sports news...")

if typed_input:
    user_input = typed_input

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Generating professional sports content..."):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_input
            )
            ai_reply = response.text
        except Exception as e:
            ai_reply = f"❌ Error: {e}"

    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
