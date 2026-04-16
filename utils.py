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

    /* Absolute Immersion: Hide Streamlit Controls */
    #MainMenu, footer, header {visibility: hidden; height: 0;}
    [data-testid="stSidebarNav"] { display: none !important; }
    button[title="View source"] { display: none !important; }

    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Outfit', sans-serif !important;
        scroll-behavior: smooth;
    }

    h1, h2, h3 {
        font-family: 'Syne', sans-serif !important;
        letter-spacing: -1px;
    }

    /* Jaguars Cinematic Deep Background */
    .stApp {
        background: radial-gradient(circle at center, #111111 0%, #050505 100%) !important;
        overflow: hidden;
    }
    
    /* Floating Light Orbs */
    .stApp::before, .stApp::after {
        content: "";
        position: fixed;
        width: 600px; height: 600px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(255,184,0,0.03) 0%, transparent 70%);
        z-index: -1;
        pointer-events: none;
    }
    .stApp::before { top: -100px; left: -100px; animation: drift 20s infinite alternate; }
    .stApp::after { bottom: -100px; right: -100px; animation: drift 25s infinite alternate-reverse; }
    
    @keyframes drift {
        from { transform: translate(0,0) scale(1); opacity: 0.3; }
        to { transform: translate(100px, 50px) scale(1.1); opacity: 0.6; }
    }

    /* Full-screen Login Background with Refinement */
    .login-container {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: linear-gradient(rgba(5, 5, 5, 0.75), rgba(5, 5, 5, 0.85)), url("app/static/login_mascot.png");
        background-size: cover;
        background-position: center;
        z-index: -1;
    }

    /* Status Hub Branding */
    .status-hub {
        position: fixed;
        top: 20px; right: 20px;
        padding: 6px 14px;
        background: rgba(18, 18, 18, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 184, 0, 0.2);
        border-radius: 30px;
        font-size: 10px;
        font-weight: 600;
        color: #FFB800;
        letter-spacing: 1px;
        z-index: 9999;
        display: flex; align-items: center; gap: 8px;
    }
    .status-dot {
        width: 6px; height: 6px;
        background: #FFB800;
        border-radius: 50%;
        box-shadow: 0 0 10px #FFB800;
        animation: pulse 2s infinite;
    }
    @keyframes pulse { 0%, 100% { opacity: 0.4; } 50% { opacity: 1; } }

    /* Message Bubbles with Physics (Spring Animation) */
    .message-row {
        display: flex;
        align-items: flex-end;
        gap: 12px;
        margin-bottom: 2px;
        animation: springIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) both;
    }
    
    @keyframes springIn {
        from { opacity: 0; transform: translateY(20px) scale(0.95); }
        to { opacity: 1; transform: translateY(0) scale(1); }
    }

    .bubble {
        padding: 12px 18px 10px 18px;
        border-radius: 12px;
        position: relative;
        backdrop-filter: blur(25px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    /* Refraction Edge (Light hitting glass) */
    .glass-card, .bubble {
        border-top: 1px solid rgba(255,255,255,0.08);
        border-left: 1px solid rgba(255,255,255,0.03);
    }

    .sent .bubble {
        background: linear-gradient(135deg, #FFB800 0%, #E6A500 100%);
        color: #000;
        border-radius: 18px 0 18px 18px;
    }
    
    .received .bubble {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 184, 0, 0.1);
        border-radius: 0 18px 18px 18px;
        color: #fff;
    }

    /* Modern Custom Scrollbar */
    ::-webkit-scrollbar { width: 5px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: rgba(255, 184, 0, 0.2); border-radius: 10px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(255, 184, 0, 0.5); }

    /* Signature Watermark */
    .watermark {
        position: fixed;
        bottom: 20px; left: 20px;
        font-size: 9px;
        color: rgba(255, 255, 255, 0.15);
        letter-spacing: 2px;
        text-transform: uppercase;
        pointer-events: none;
        z-index: 1000;
    }

    /* Staggered Entry for Login Card */
    .glow-aura { animation: slideUpFade 0.8s cubic-bezier(.16,1,.3,1) both; }
    
    </style>
    
    <div class="status-hub">
        <div class="status-dot"></div>
        JAG-LINK STATUS: ACTIVE
    </div>
    <div class="watermark">Designed by Antigravity x Jaguars Elite</div>
    """, unsafe_allow_html=True)
