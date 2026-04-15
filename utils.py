import streamlit as st

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

    /* Chat Container */
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 16px;
        padding: 20px;
        max-height: 65vh;
        overflow-y: auto;
        scrollbar-width: thin;
        scrollbar-color: #7B5EA7 transparent;
    }

    .chat-container::-webkit-scrollbar {
        width: 6px;
    }
    .chat-container::-webkit-scrollbar-thumb {
        background: rgba(123, 94, 167, 0.5);
        border-radius: 10px;
    }

    /* Chat Bubbles */
    .message-row {
        display: flex;
        width: 100%;
        animation: bubbleIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) both;
    }

    @keyframes bubbleIn {
        from { opacity: 0; transform: translateY(20px) scale(0.95); }
        to { opacity: 1; transform: translateY(0) scale(1); }
    }

    .bubble {
        max-width: 75%;
        padding: 12px 20px;
        font-size: 15px;
        line-height: 1.5;
        position: relative;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        cursor: default;
    }
    
    .bubble:hover {
        transform: translateY(-2px);
    }

    .sent .bubble {
        background: linear-gradient(135deg, #7B5EA7 0%, #5E448C 100%);
        color: white;
        border-radius: 20px 20px 4px 20px;
        box-shadow: 0 4px 15px rgba(123, 94, 167, 0.3), inset 0 0 10px rgba(255,255,255,0.1);
    }

    .received .bubble {
        background: rgba(255, 255, 255, 0.05);
        color: #E8E8FF;
        border: 1px solid rgba(123, 94, 167, 0.2);
        border-radius: 20px 20px 20px 4px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    .received .bubble:hover {
        border-color: rgba(123, 94, 167, 0.5);
        box-shadow: 0 0 15px rgba(123, 94, 167, 0.2);
    }

    .message-info {
        font-size: 11px;
        margin-top: 6px;
        opacity: 0.5;
        font-weight: 300;
        display: none;
    }
    
    .bubble:hover .message-info {
        display: block;
        animation: fadeIn 0.4s forwards;
    }

    /* Sidebar & Inputs */
    [data-testid="stSidebar"] {
        background: rgba(10, 10, 18, 0.9) !important;
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(123, 94, 167, 0.15) !important;
    }

    .stButton>button {
        border-radius: 12px !important;
        padding: 10px 24px !important;
        background: rgba(123, 94, 167, 0.1) !important;
        border: 1px solid rgba(123, 94, 167, 0.5) !important;
        color: white !important;
        font-weight: 600 !important;
        transition: all 0.3s !important;
    }

    .stButton>button:hover {
        background: rgba(123, 94, 167, 0.8) !important;
        box-shadow: 0 0 20px rgba(123, 94, 167, 0.4) !important;
        transform: translateY(-1px);
    }

    .stChatInputContainer {
        border: 1px solid rgba(123, 94, 167, 0.3) !important;
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 16px !important;
        backdrop-filter: blur(10px);
    }
    </style>
    """, unsafe_allow_html=True)

def message_bubble(content, sender, is_sent, timestamp):
    alignment = "sent" if is_sent else "received"
    time_str = time.strftime("%H:%M", time.localtime(timestamp))
    
    st.markdown(f"""
    <div class="message-row {alignment}">
        <div class="bubble">
            <div>{content}</div>
            <div class="message-info">{sender} • {time_str}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

import time
