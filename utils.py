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
            <div class="bubble-container">
                <div class="bubble">
                    <div class="bubble-content">{content}</div>
                    <div class="bubble-meta">
                        <span class="time">{time_str}</span>
                        <span class="status">🐆</span>
                    </div>
                </div>
                <svg class="tail-sent" width="10" height="10" viewBox="0 0 10 10"><path d="M0 0 L10 0 L10 10 C5 5 0 0 0 0" fill="#FFB800"/></svg>
            </div>
            {avatar_html}
        </div>
        """
    else:
        msg_html = f"""
        <div class="message-row received {'grouped' if is_grouped else ''}">
            {avatar_html}
            <div class="bubble-container">
                <svg class="tail-received" width="10" height="10" viewBox="0 0 10 10"><path d="M10 0 L0 0 L0 10 C5 5 10 0 10 0" fill="rgba(255,255,255,0.06)"/></svg>
                <div class="bubble">
                    {f'<div class="sender-name" style="color:{avatar_color}">{sender}</div>' if not is_grouped else ''}
                    <div class="bubble-content">{content}</div>
                    <div class="bubble-meta">
                        <span class="time">{time_str}</span>
                    </div>
                </div>
            </div>
        </div>
        """
    
    st.markdown(msg_html, unsafe_allow_html=True)

def inject_antigravity_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@600;800&family=Outfit:wght@300;400;600&display=swap');

    /* Total Immersion 2.0 */
    [data-testid="stHeader"], [data-testid="stFooter"], #MainMenu {
        visibility: hidden !important;
        height: 0 !important;
    }
    [data-testid="stSidebarNav"] { display: none !important; }

    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Outfit', sans-serif !important;
        background: #050505 !important;
    }

    h1, h2, h3 { font-family: 'Syne', sans-serif !important; letter-spacing: -1px; }

    /* Tactical Background */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #111 0%, #050505 100%) !important;
    }
    
    /* Ultimate Background Orbs */
    .stApp::before {
        content: ""; position: fixed; top: -10%; left: -10%; width: 50%; height: 50%;
        background: radial-gradient(circle, rgba(255,184,0,0.04) 0%, transparent 60%);
        animation: rotateOrb 30s infinite linear; z-index: -1;
    }
    @keyframes rotateOrb { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

    /* Login Area */
    .login-container {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background-image: linear-gradient(rgba(5, 5, 5, 0.8), rgba(5, 5, 5, 0.9)), url("app/static/login_mascot.png"), url("static/login_mascot.png");
        background-size: cover; background-position: center; z-index: -1;
    }

    /* Sidebar Refinement */
    [data-testid="stSidebar"] {
        background-color: #080808 !important;
        border-right: 1px solid rgba(255, 184, 0, 0.1) !important;
    }
    
    .profile-card {
        padding: 20px;
        background: rgba(255, 184, 0, 0.03);
        border: 1px solid rgba(255, 184, 0, 0.1);
        border-radius: 20px;
        margin-bottom: 25px;
        backdrop-filter: blur(10px);
    }
    .profile-card h4 { margin: 0; color: #FFB800; font-size: 14px; }
    .status-light {
        display: inline-block; width: 8px; height: 8px;
        background: #FFB800; border-radius: 50%;
        box-shadow: 0 0 10px #FFB800; margin-right: 8px;
        animation: pulseLight 2s infinite;
    }
    @keyframes pulseLight { 0%, 100% { opacity: 0.5; } 50% { opacity: 1; } }

    /* Tactical Radar Nav */
    div[data-testid="stSidebar"] .stRadio > label { display: none; }
    div[data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
        background: rgba(255, 255, 255, 0.02);
        border-radius: 15px;
        padding: 5px;
    }
    div[data-testid="stSidebar"] .stRadio div[data-testid="stMarkdownContainer"] p {
        font-size: 13px; font-weight: 400; color: #888;
    }

    /* Chat Elements 2.0 */
    .message-row {
        display: flex; align-items: flex-end; gap: 10px; margin-bottom: 4px;
        animation: springIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) both;
    }
    @keyframes springIn { from { opacity: 0; transform: translateY(15px) scale(0.98); } to { opacity: 1; transform: translateY(0) scale(1); } }

    .bubble-container { position: relative; display: flex; align-items: flex-end; }
    
    .bubble {
        padding: 10px 15px; border-radius: 12px;
        backdrop-filter: blur(15px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .sent .bubble { background: #FFB800; color: #000; border-bottom-right-radius: 2px; }
    .received .bubble { background: rgba(255,255,255,0.06); color: #fff; border-bottom-left-radius: 2px; border: 1px solid rgba(255,255,255,0.05); }

    .tail-sent { margin-left: -2px; margin-bottom: 2px; }
    .tail-received { margin-right: -2px; margin-bottom: 2px; }

    /* Neon-Pulse Inputs */
    .stTextInput input:focus {
        border-color: #FFB800 !important;
        box-shadow: 0 0 15px rgba(255, 184, 0, 0.3) !important;
        background: rgba(255,184,0,0.05) !important;
    }

    /* Status Hub Refined */
    .status-hub {
        position: fixed; top: 20px; right: 20px; font-size: 9px;
        font-weight: 800; color: #FFB800; letter-spacing: 2px;
        z-index: 9999;
    }

    /* Watermark */
    .watermark {
        position: fixed; bottom: 15px; right: 20px;
        font-size: 8px; color: rgba(255,255,255,0.1);
        text-transform: uppercase; letter-spacing: 3px;
    }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar { width: 4px; }
    ::-webkit-scrollbar-thumb { background: rgba(255,184,0,0.2); border-radius: 10px; }

    </style>
    <div class="status-hub">JAG-LINK: ENCRYPTED</div>
    <div class="watermark">Jaguar Elite Core</div>
    """, unsafe_allow_html=True)
