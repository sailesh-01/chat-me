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

    /* Jaguars Deep Black & Gold Layout */
    .stApp {
        background: radial-gradient(circle at center, #151515 0%, #080808 100%) !important;
    }
    
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 2px;
        padding: 20px;
        max-height: 70vh;
        overflow-y: auto;
        background-image: 
            radial-gradient(circle at 20% 30%, rgba(255, 184, 0, 0.03) 0%, transparent 40%),
            radial-gradient(circle at 80% 70%, rgba(255, 184, 0, 0.05) 0%, transparent 50%);
        background-attachment: local;
        border-radius: 20px;
    }

    /* Sticky Date Headers */
    .sticky-date {
        position: sticky;
        top: 0;
        z-index: 100;
        display: flex;
        justify-content: center;
        margin: 10px 0;
    }
    .date-label {
        background: rgba(18, 18, 18, 0.9);
        backdrop-filter: blur(10px);
        padding: 4px 14px;
        border-radius: 12px;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #FFB800;
        border: 1px solid rgba(255, 184, 0, 0.15);
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }

    /* Message Rows */
    .message-row {
        display: flex;
        align-items: flex-end;
        gap: 8px;
        margin-bottom: 2px;
        animation: slideUp 0.3s ease-out;
    }
    .message-row.sent { justify-content: flex-end; }
    .message-row.grouped { margin-top: -6px; }

    @keyframes slideUp {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Avatars */
    .avatar {
        width: 30px; height: 30px;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 10px; font-weight: 600; color: #000;
        box-shadow: 0 0 15px rgba(255, 184, 0, 0.3);
        flex-shrink: 0;
    }

    /* Bubble with Tail */
    .bubble {
        padding: 10px 14px 8px 16px;
        font-size: 14.5px;
        line-height: 1.5;
        position: relative;
        backdrop-filter: blur(12px);
        min-width: 60px;
        max-width: 450px;
        transition: transform 0.2s ease;
    }
    .bubble:hover { transform: scale(1.01); }

    .message-row:not(.grouped) .bubble-tail-sent::after {
        content: ""; position: absolute;
        top: 0; right: -8px; width: 0; height: 0;
        border-left: 10px solid #FFB800;
        border-bottom: 10px solid transparent;
    }
    .message-row:not(.grouped) .bubble-tail-received::after {
        content: ""; position: absolute;
        top: 0; left: -8px; width: 0; height: 0;
        border-right: 10px solid rgba(255, 255, 255, 0.05);
        border-bottom: 10px solid transparent;
    }

    .sent .bubble {
        background: #FFB800;
        color: #000;
        font-weight: 400;
        border-radius: 12px 0 12px 12px;
        box-shadow: 0 4px 20px rgba(255, 184, 0, 0.15), inset 0 0 10px rgba(255,255,255,0.2);
    }
    .sent.grouped .bubble { border-radius: 12px; }

    .received .bubble {
        background: rgba(255, 255, 255, 0.05);
        color: #F5F5F5;
        border-radius: 0 12px 12px 12px;
        border: 1px solid rgba(255, 184, 0, 0.1);
    }
    .received.grouped .bubble { border-radius: 12px; margin-left: 38px; }

    .sender-name {
        font-size: 11px; font-weight: 600;
        margin-bottom: 4px; opacity: 0.9;
    }

    /* Inline Metadata */
    .bubble-meta {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 4px;
        margin-top: 4px;
        font-size: 10px;
        opacity: 0.6;
    }
    .sent .time { color: rgba(0,0,0,0.6); }

    /* Reactions */
    .reactions {
        position: absolute;
        top: -20px; right: 10px;
        background: rgba(18,18,18,0.95);
        border: 1px solid #FFB800;
        padding: 2px 10px; border-radius: 20px;
        display: none; z-index: 1000;
        box-shadow: 0 4px 15px rgba(255,184,0,0.2);
    }
    .bubble:hover .reactions { display: flex; gap: 8px; animation: pop 0.2s; }
    @keyframes pop { from { scale: 0.8; opacity: 0; } to { scale: 1; opacity: 1; } }

    /* Glass Panels */
    .glass-card {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 184, 0, 0.1);
        border-radius: 24px;
        padding: 40px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }

    /* Input & Buttons */
    .stChatInputContainer {
        border-radius: 25px !important;
        background: rgba(255,255,255,0.03) !important;
        border: 1px solid rgba(255,184,0,0.2) !important;
    }
    .stButton>button {
        border-radius: 12px !important;
        background: rgba(255,184,0,0.1) !important;
        border: 1px solid #FFB800 !important;
        color: #FFB800 !important;
        transition: 0.3s;
    }
    .stButton>button:hover { 
        background: #FFB800 !important; 
        color: #000 !important; 
        box-shadow: 0 0 20px rgba(255,184,0,0.4) !important;
    }

    </style>
    """, unsafe_allow_html=True)
