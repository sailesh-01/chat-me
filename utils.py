import streamlit as st

def inject_antigravity_styles():
    st.markdown("""
    <style>
    /* Antigravity Star-field Background */
    .stApp {
        background: radial-gradient(circle at center, #1B1B3A 0%, #0A0A12 100%);
        background-attachment: fixed;
    }
    
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: 
            radial-gradient(1px 1px at 20px 30px, #eee, rgba(0,0,0,0)),
            radial-gradient(1px 1px at 40px 70px, #fff, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 50px 160px, #ddd, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 90px 40px, #fff, rgba(0,0,0,0)),
            radial-gradient(1px 1px at 130px 80px, #fff, rgba(0,0,0,0)),
            radial-gradient(1px 1px at 160px 120px, #ddd, rgba(0,0,0,0));
        background-repeat: repeat;
        background-size: 200px 200px;
        opacity: 0.3;
        animation: starsDrift 100s linear infinite;
        z-index: -1;
    }

    @keyframes starsDrift {
        from { transform: translateY(0); }
        to { transform: translateY(-200px); }
    }

    /* Chat Bubble Styles */
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
        padding: 20px;
        max-height: 70vh;
        overflow-y: auto;
        scrollbar-width: thin;
        scrollbar-color: rgba(123, 94, 167, 0.5) transparent;
    }

    .message-row {
        display: flex;
        width: 100%;
        animation: bubbleIn 0.4s ease-out both;
    }

    .message-row.sent {
        justify-content: flex-end;
    }

    .message-row.received {
        justify-content: flex-start;
    }

    @keyframes bubbleIn {
        from { opacity: 0; transform: translateY(12px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .bubble {
        max-width: 70%;
        padding: 10px 16px;
        font-size: 15px;
        line-height: 1.4;
        position: relative;
        backdrop-filter: blur(8px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: transform 0.2s;
        cursor: default;
    }
    
    .bubble:hover {
        transform: scale(1.02);
    }

    .sent .bubble {
        background: #7B5EA7;
        color: white;
        border-radius: 18px 18px 4px 18px;
    }

    .received .bubble {
        background: rgba(255, 255, 255, 0.07);
        color: #E8E8FF;
        border: 1px solid rgba(123, 94, 167, 0.3);
        border-radius: 18px 18px 18px 4px;
    }

    .message-info {
        font-size: 10px;
        margin-top: 4px;
        opacity: 0.6;
        display: none; /* Hide by default, show on hover */
    }
    
    .bubble:hover .message-info {
        display: block;
        animation: fadeIn 0.3s forwards;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    /* Sidebar and Glassmorphism */
    [data-testid="stSidebar"] {
        background-color: rgba(14, 14, 44, 0.8);
        backdrop-filter: blur(12px);
        border-right: 1px solid rgba(123, 94, 167, 0.2);
    }

    .stButton>button {
        border-radius: 20px;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
        transition: all 0.3s;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(123, 94, 167, 0.4);
    }

    /* Input Styling */
    .stChatInputContainer {
        border-radius: 25px !important;
        background: rgba(255,255,255,0.05) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(123, 94, 167, 0.3) !important;
    }
    
    /* Typing Indicator Animation */
    .typing-indicator {
        display: flex;
        gap: 4px;
        padding: 10px;
    }
    .dot {
        width: 6px; height: 6px; background: #7B5EA7; border-radius: 50%;
        animation: float 1s infinite ease-in-out;
    }
    .dot:nth-child(2) { animation-delay: 0.2s; }
    .dot:nth-child(3) { animation-delay: 0.4s; }
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
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
