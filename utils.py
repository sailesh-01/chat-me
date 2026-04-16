import streamlit as st
import time

def date_divider(date_str):
    st.markdown(f"""
    <div style="display: flex; align-items: center; margin: 24px 0; opacity: 0.4;">
        <div style="flex-grow: 1; height: 1px; background: rgba(123, 94, 167, 0.3);"></div>
        <div style="padding: 0 15px; font-size: 11px; letter-spacing: 2px; text-transform: uppercase;">{date_str}</div>
        <div style="flex-grow: 1; height: 1px; background: rgba(123, 94, 167, 0.3);"></div>
    </div>
    """, unsafe_allow_html=True)

def message_bubble(content, sender, is_sent, timestamp, avatar_color="#7B5EA7", is_grouped=False):
    alignment = "sent" if is_sent else "received"
    time_str = time.strftime("%H:%M", time.localtime(timestamp))
    initials = "".join([n[0] for n in sender.split()[:2]]).upper()
    
    # Hide avatar and name if grouped
    avatar_html = ""
    if not is_grouped:
        avatar_html = f'<div class="avatar" style="background: {avatar_color};">{initials}</div>'
    
    # Message layout changes based on sender
    msg_layout = ""
    if is_sent:
        msg_layout = f"""
        <div class="message-row sent {'grouped' if is_grouped else ''}">
            <div class="bubble-container">
                <div class="bubble">
                    {content}
                    <div class="message-info">{time_str}</div>
                    <div class="reactions">🛸 ✨ 👍</div>
                </div>
            </div>
            {avatar_html}
        </div>
        """
    else:
        msg_layout = f"""
        <div class="message-row received {'grouped' if is_grouped else ''}">
            {avatar_html}
            <div class="bubble-container">
                <div class="bubble">
                    {content}
                    <div class="message-info">{sender} • {time_str}</div>
                    <div class="reactions">🔭 ❤️ 🌌</div>
                </div>
            </div>
        </div>
        """
    
    st.markdown(msg_layout, unsafe_allow_html=True)

def inject_antigravity_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Outfit', sans-serif !important;
    }

    /* Antigravity Parallax Star-field */
    .stApp {
        background: radial-gradient(circle at center, #1B1B3A 0%, #0A0A12 100%) !important;
    }
    
    .stApp::before, .stApp::after {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 200%; height: 200%;
        background-image: 
            radial-gradient(1.5px 1.5px at 10% 10%, #fff, rgba(0,0,0,0)),
            radial-gradient(1px 1px at 20% 40%, #ddd, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 30% 70%, #fff, rgba(0,0,0,0)),
            radial-gradient(1.5px 1.5px at 50% 20%, #ddd, rgba(0,0,0,0)),
            radial-gradient(2.5px 2.5px at 70% 50%, #fff, rgba(0,0,0,0)),
            radial-gradient(1.5px 1.5px at 90% 80%, #ddd, rgba(0,0,0,0));
        background-repeat: repeat;
        background-size: 400px 400px;
        z-index: -1;
    }

    .stApp::before {
        opacity: 0.2;
        animation: starsDriftSlow 120s linear infinite;
    }

    .stApp::after {
        opacity: 0.1;
        background-size: 600px 600px;
        animation: starsDriftFast 80s linear infinite;
    }

    @keyframes starsDriftSlow {
        from { transform: translate(0, 0); }
        to { transform: translate(-200px, -200px); }
    }

    @keyframes starsDriftFast {
        from { transform: translate(0, 0); }
        to { transform: translate(-300px, -300px); }
    }

    /* Message Interface */
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 4px; /* Default gap for grouping */
        padding: 20px;
        max-height: 65vh;
        overflow-y: auto;
    }

    .message-row {
        display: flex;
        align-items: flex-end;
        gap: 12px;
        margin-bottom: 2px;
        animation: bubbleIn 0.4s ease-out both;
    }

    .message-row.sent {
        justify-content: flex-end;
    }

    .message-row.grouped {
        margin-top: -8px;
    }

    .avatar {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 11px;
        font-weight: 600;
        color: white;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        flex-shrink: 0;
    }

    .bubble-container {
        max-width: 70%;
        position: relative;
    }

    .bubble {
        padding: 10px 16px;
        font-size: 14px;
        line-height: 1.5;
        backdrop-filter: blur(10px);
        transition: all 0.2s ease;
        position: relative;
    }

    .sent .bubble {
        background: linear-gradient(135deg, #7B5EA7 0%, #5E448C 100%);
        color: #fff;
        border-radius: 18px 18px 4px 18px;
        box-shadow: 0 4px 15px rgba(123,94,167,0.2);
    }
    
    .sent.grouped .bubble {
        border-radius: 18px 4px 4px 18px;
    }

    .received .bubble {
        background: rgba(255, 255, 255, 0.05);
        color: #E8E8FF;
        border: 1px solid rgba(123, 94, 167, 0.2);
        border-radius: 18px 18px 18px 4px;
    }

    .received.grouped .bubble {
        border-radius: 4px 18px 18px 4px;
        margin-left: 44px; /* Position without avatar */
    }

    .message-info {
        font-size: 10px;
        margin-top: 4px;
        opacity: 0.5;
        font-weight: 300;
    }

    /* Reactions overlay */
    .reactions {
        position: absolute;
        top: -15px;
        right: 10px;
        background: rgba(14, 14, 44, 0.9);
        backdrop-filter: blur(5px);
        border: 1px solid rgba(123, 94, 167, 0.4);
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 12px;
        display: none;
        cursor: pointer;
        z-index: 10;
        white-space: nowrap;
    }

    .bubble:hover .reactions {
        display: block;
        animation: popUp 0.3s ease-out;
    }

    @keyframes popUp {
        from { opacity: 0; transform: translateY(5px) scale(0.8); }
        to { opacity: 1; transform: translateY(0) scale(1); }
    }

    /* Glass Panels */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(123, 94, 167, 0.2);
        border-radius: 24px;
        padding: 40px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
        margin-bottom: 20px;
    }

    /* Inputs & UI */
    [data-testid="stSidebar"] {
        background: rgba(10, 10, 18, 0.9) !important;
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(123, 94, 167, 0.15) !important;
    }

    .stButton>button {
        border-radius: 12px !important;
        background: rgba(123, 94, 167, 0.1) !important;
        border: 1px solid rgba(123, 94, 167, 0.5) !important;
        transition: all 0.3s !important;
    }

    .stButton>button:hover {
        background: rgba(123, 94, 167, 0.8) !important;
        box-shadow: 0 0 20px rgba(123, 94, 167, 0.4) !important;
    }
    
    .stChatInputContainer {
        border: 1px solid rgba(123, 94, 167, 0.3) !important;
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 16px !important;
    }
    </style>
    """, unsafe_allow_html=True)
