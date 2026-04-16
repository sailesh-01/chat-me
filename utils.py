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

    /* Aura Container for Login */
    .glow-aura {
        position: relative;
        padding: 4px;
        border-radius: 28px;
        background: linear-gradient(135deg, rgba(255,184,0,0.2) 0%, transparent 50%, rgba(255,184,0,0.1) 100%);
        animation: pulseAura 4s infinite ease-in-out;
        box-shadow: 0 0 50px rgba(0,0,0,0.5);
    }
    
    @keyframes pulseAura {
        0%, 100% { box-shadow: 0 0 30px rgba(255,184,0,0.05); transform: scale(1); }
        50% { box-shadow: 0 0 60px rgba(255,184,0,0.15); transform: scale(1.005); }
    }

    .glass-card {
        background: rgba(18, 18, 18, 0.7);
        backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 184, 0, 0.2);
        border-radius: 24px;
        padding: 40px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6);
        transition: border-color 0.5s;
    }
    .glass-card:hover { border-color: rgba(255, 184, 0, 0.4); }

    /* Shimmer Button Effect */
    .stButton>button {
        position: relative;
        overflow: hidden;
        border-radius: 12px !important;
        background: rgba(255,184,0,0.1) !important;
        border: 1px solid #FFB800 !important;
        color: #FFB800 !important;
        font-weight: 600 !important;
        letter-spacing: 1px;
        text-transform: uppercase;
        transition: 0.3s;
    }
    
    .stButton>button::after {
        content: "";
        position: absolute;
        top: -50%; left: -60%; width: 20%; height: 200%;
        background: rgba(255,255,255,0.1);
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
        animation: slideUpFade 0.7s ease-out both;
    }
    .stTextInput:nth-child(1) { animation-delay: 0.1s; }
    .stTextInput:nth-child(2) { animation-delay: 0.2s; }
    
    @keyframes slideUpFade {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Chat Elements (Same as before but refined) */
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 2px;
        padding: 20px;
        max-height: 70vh;
        overflow-y: auto;
        background-image: radial-gradient(circle at 50% 50%, rgba(255, 184, 0, 0.02) 0%, transparent 80%);
        border-radius: 20px;
    }

    .message-row { display: flex; align-items: flex-end; gap: 8px; margin-bottom: 2px; }
    .message-row.sent { justify-content: flex-end; }
    .bubble {
        padding: 10px 16px;
        border-radius: 12px;
        position: relative;
        backdrop-filter: blur(12px);
    }
    .sent .bubble { background: #FFB800; color: #000; box-shadow: 0 4px 15px rgba(255,184,0,0.2); }
    .received .bubble { background: rgba(255,255,255,0.06); color: #fff; border: 1px solid rgba(255,184,0,0.1); }
    
    .avatar { box-shadow: 0 0 15px rgba(255,184,0,0.2); }
    </style>
    """, unsafe_allow_html=True)
