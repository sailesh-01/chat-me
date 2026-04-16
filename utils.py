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
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@600;800&family=Outfit:wght@300;400;600&display=swap');

    /* Temporary Restore UI for Stability */
    /* #MainMenu, footer, header {visibility: hidden; height: 0;} */

    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Outfit', sans-serif !important;
    }

    h1, h2, h3 {
        font-family: 'Syne', sans-serif !important;
    }

    /* Jaguars Deep Background */
    .stApp {
        background: radial-gradient(circle at center, #111111 0%, #050505 100%) !important;
    }
    
    /* Full-screen Login Background (Safer Path) */
    .login-container {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: #050505;
        background-image: linear-gradient(rgba(5, 5, 5, 0.75), rgba(5, 5, 5, 0.85)), url("app/static/login_mascot.png"), url("static/login_mascot.png");
        background-size: cover;
        background-position: center;
        z-index: -1;
    }

    /* Status Hub */
    .status-hub {
        position: fixed;
        top: 60px; right: 20px;
        padding: 6px 14px;
        background: rgba(18, 18, 18, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 184, 0, 0.2);
        border-radius: 30px;
        font-size: 10px;
        color: #FFB800;
        z-index: 1000;
    }

    /* Message Bubbles */
    .message-row {
        display: flex;
        align-items: flex-end;
        gap: 12px;
        margin-bottom: 2px;
        animation: slideIn 0.3s ease-out both;
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .bubble {
        padding: 12px 18px 10px 18px;
        border-radius: 12px;
        position: relative;
        backdrop-filter: blur(20px);
    }
    
    .glass-card {
        background: rgba(18, 18, 18, 0.75);
        backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 184, 0, 0.15);
        border-radius: 24px;
        padding: 40px;
        transition: all 0.4s ease;
    }

    .stButton>button {
        border-radius: 12px !important;
        background: rgba(255,184,0,0.1) !important;
        border: 1px solid #FFB800 !important;
        color: #FFB800 !important;
        transition: 0.3s;
    }
    .stButton>button:hover { background: #FFB800 !important; color: #000 !important; }

    </style>
    
    <div class="status-hub">JAG-LINK: ACTIVE</div>
    """, unsafe_allow_html=True)
