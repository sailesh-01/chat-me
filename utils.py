import streamlit as st
import time

def date_divider(date_str):
    st.markdown(f"""
    <div class="sticky-date">
        <div class="date-label">{date_str}</div>
    </div>
    """, unsafe_allow_html=True)

def message_bubble(content, sender, is_sent, timestamp, avatar_color="#FFB800", is_grouped=False):
    alignment = "sent" if is_sent else "received"
    time_str = time.strftime("%H:%M", time.localtime(timestamp))
    initials = "".join([n[0] for n in sender.split()[:2]]).upper()
    
    avatar_html = ""
    if not is_grouped:
        avatar_html = f'<div class="avatar" style="background: {avatar_color}; color: #000;">{initials}</div>'
    
    if is_sent:
        msg_html = f"""
        <div class="message-row sent {'grouped' if is_grouped else ''}">
            <div class="bubble-tail-sent">
                <div class="bubble">
                    <div class="bubble-content">{content}</div>
                    <div class="bubble-meta">
                        <span class="time">{time_str}</span>
                        <span class="status">🐆</span>
                    </div>
                    <div class="reactions">🐆 ✨ 🔥</div>
                </div>
            </div>
            {avatar_html}
        </div>
        """
    else:
        msg_html = f"""
        <div class="message-row received {'grouped' if is_grouped else ''}">
            {avatar_html}
            <div class="bubble-tail-received">
                <div class="bubble">
                    {f'<div class="sender-name" style="color:{avatar_color}">{sender}</div>' if not is_grouped else ''}
                    <div class="bubble-content">{content}</div>
                    <div class="bubble-meta">
                        <span class="time">{time_str}</span>
                    </div>
                    <div class="reactions">🔍 ✨ 🐆</div>
                </div>
            </div>
        </div>
        """
    
    st.markdown(msg_html, unsafe_allow_html=True)

def inject_antigravity_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Outfit', sans-serif !important;
    }

    /* Cinematic Layout */
    .stApp {
        background: radial-gradient(circle at center, #151515 0%, #080808 100%) !important;
    }

    /* Full-screen Login Background */
    .login-container {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: linear-gradient(rgba(8, 8, 8, 0.7), rgba(8, 8, 8, 0.7)), url("app/static/login_mascot.png");
        background-size: cover;
        background-position: center;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: -1;
    }

    /* Aura Container for Login */
    .glow-aura {
        position: relative;
        padding: 4px;
        border-radius: 28px;
        background: linear-gradient(135deg, rgba(255,184,0,0.1) 0%, transparent 50%, rgba(255,184,0,0.05) 100%);
        animation: pulseAura 4s infinite ease-in-out;
    }
    
    @keyframes pulseAura {
        0%, 100% { box-shadow: 0 0 30px rgba(255,184,0,0.05); }
        50% { box-shadow: 0 0 60px rgba(255,184,0,0.15); }
    }

    /* Error Shake Animation */
    .shake-error {
        animation: shake 0.5s cubic-bezier(.36,.07,.19,.97) both;
        border-color: rgba(255, 69, 58, 0.5) !important;
    }

    @keyframes shake {
        10%, 90% { transform: translate3d(-1px, 0, 0); }
        20%, 80% { transform: translate3d(2px, 0, 0); }
        30%, 50%, 70% { transform: translate3d(-4px, 0, 0); }
        40%, 60% { transform: translate3d(4px, 0, 0); }
    }

    .glass-card {
        background: rgba(18, 18, 18, 0.75);
        backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 184, 0, 0.15);
        border-radius: 24px;
        padding: 40px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6);
        transition: all 0.4s ease;
    }
    .glass-card:hover { border-color: rgba(255, 184, 0, 0.4); }

    /* Input Field Icons via CSS hack */
    .stTextInput input {
        padding-left: 40px !important;
        background-repeat: no-repeat !important;
        background-position: 12px center !important;
        background-size: 18px !important;
        transition: all 0.3s !important;
    }
    
    /* Logic to inject icons into specific placeholders */
    .stTextInput input[placeholder*="ID"] {
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="%23FFB800" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>') !important;
    }
    
    .stTextInput input[placeholder*="Key"] {
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="%23FFB800" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>') !important;
    }

    /* Shimmer Button Effect */
    .stButton>button {
        position: relative;
        overflow: hidden;
        border-radius: 12px !important;
        background: rgba(255,184,0,0.1) !important;
        border: 1px solid #FFB800 !important;
        color: #FFB800 !important;
        font-weight: 600 !important;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        transition: 0.3s;
    }
    
    .stButton>button::after {
        content: "";
        position: absolute;
        top: -50%; left: -60%; width: 25%; height: 200%;
        background: rgba(255,255,255,0.15);
        transform: rotate(30deg);
        animation: shimmer 4s infinite;
    }
    
    @keyframes shimmer {
        0% { left: -60%; }
        20%, 100% { left: 120%; }
    }

    .stButton>button:hover {
        background: #FFB800 !important;
        color: #000 !important;
        box-shadow: 0 0 30px rgba(255,184,0,0.5) !important;
    }

    /* Staggered Entry Animations */
    .stTextInput, .stRadio {
        animation: slideUpFade 0.6s ease-out both;
    }
    .stTextInput:nth-child(2) { animation-delay: 0.1s; }
    .stTextInput:nth-child(3) { animation-delay: 0.2s; }
    
    @keyframes slideUpFade {
        from { opacity: 0; transform: translateY(15px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Custom Spinner Styling */
    .stSpinner > div {
        border-top-color: #FFB800 !important;
    }

    /* Chat Container (Refined) */
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 2px;
        padding: 20px;
        max-height: 70vh;
        overflow-y: auto;
    }
    </style>
    """, unsafe_allow_html=True)
