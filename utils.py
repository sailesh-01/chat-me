import streamlit as st
import time

def date_divider(date_str):
    st.markdown(f"""
    <div class="sticky-date">
        <div class="date-label">{date_str}</div>
    </div>
    """, unsafe_allow_html=True)

def message_bubble(content, sender, is_sent, timestamp, avatar_color="#7B5EA7", is_grouped=False):
    alignment = "sent" if is_sent else "received"
    time_str = time.strftime("%H:%M", time.localtime(timestamp))
    initials = "".join([n[0] for n in sender.split()[:2]]).upper()
    
    avatar_html = ""
    if not is_grouped:
        avatar_html = f'<div class="avatar" style="background: {avatar_color};">{initials}</div>'
    
    # Message layout logic (WhatsApp-inspired tails and inline time)
    if is_sent:
        msg_html = f"""
        <div class="message-row sent {'grouped' if is_grouped else ''}">
            <div class="bubble-tail-sent">
                <div class="bubble">
                    <div class="bubble-content">{content}</div>
                    <div class="bubble-meta">
                        <span class="time">{time_str}</span>
                        <span class="status">🛸</span>
                    </div>
                    <div class="reactions">🛸 ✨ 👍</div>
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
                    {!is_grouped and f'<div class="sender-name" style="color:{avatar_color}">{sender}</div>' or ''}
                    <div class="bubble-content">{content}</div>
                    <div class="bubble-meta">
                        <span class="time">{time_str}</span>
                    </div>
                    <div class="reactions">🔭 ❤️ 🌌</div>
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

    /* Antigravity Parallax Space Layout */
    .stApp {
        background: radial-gradient(circle at center, #1B1B3A 0%, #0A0A12 100%) !important;
    }
    
    /* Dedicated Chat Wallpaper (WhatsApp style) */
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 2px;
        padding: 20px;
        max-height: 70vh;
        overflow-y: auto;
        background-image: 
            radial-gradient(circle at 20% 30%, rgba(123, 94, 167, 0.05) 0%, transparent 40%),
            radial-gradient(circle at 80% 70%, rgba(123, 94, 167, 0.08) 0%, transparent 50%);
        background-attachment: local;
        border-radius: 20px;
        position: relative;
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
        background: rgba(14, 14, 44, 0.85);
        backdrop-filter: blur(10px);
        padding: 4px 14px;
        border-radius: 12px;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: rgba(255, 255, 255, 0.6);
        border: 1px solid rgba(123, 94, 167, 0.2);
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
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
        font-size: 10px; font-weight: 600; color: white;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        flex-shrink: 0;
    }

    /* Bubble with Tail Implementation */
    .bubble {
        padding: 8px 12px 6px 14px;
        font-size: 14.5px;
        line-height: 1.5;
        position: relative;
        backdrop-filter: blur(12px);
        min-width: 60px;
        max-width: 450px;
    }

    .bubble-tail-sent, .bubble-tail-received { position: relative; }

    /* The Tail */
    .message-row:not(.grouped) .bubble-tail-sent::after {
        content: ""; position: absolute;
        top: 0; right: -8px; width: 0; height: 0;
        border-left: 10px solid #7B5EA7;
        border-bottom: 10px solid transparent;
    }
    .message-row:not(.grouped) .bubble-tail-received::after {
        content: ""; position: absolute;
        top: 0; left: -8px; width: 0; height: 0;
        border-right: 10px solid rgba(255, 255, 255, 0.08);
        border-bottom: 10px solid transparent;
    }

    .sent .bubble {
        background: #7B5EA7;
        color: white;
        border-radius: 12px 0 12px 12px;
        box-shadow: 0 4px 15px rgba(123,94,167,0.2);
    }
    .sent.grouped .bubble { border-radius: 12px; }

    .received .bubble {
        background: rgba(255, 255, 255, 0.08);
        color: #E8E8FF;
        border-radius: 0 12px 12px 12px;
        border: 1px solid rgba(123, 94, 167, 0.1);
    }
    .received.grouped .bubble { border-radius: 12px; margin-left: 38px; }

    .sender-name {
        font-size: 11px; font-weight: 600;
        margin-bottom: 2px; opacity: 0.9;
    }

    /* Inline Metadata (Time + Status) */
    .bubble-meta {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 4px;
        margin-top: 2px;
        font-size: 10px;
        opacity: 0.5;
    }
    .sent .time { color: rgba(255,255,255,0.7); }

    /* Hover Reactions */
    .reactions {
        position: absolute;
        top: -20px; right: 10px;
        background: rgba(14,14,44,0.9);
        border: 1px solid rgba(123,94,167,0.4);
        padding: 2px 8px; border-radius: 20px;
        display: none; z-index: 1000;
    }
    .bubble:hover .reactions { display: flex; gap: 5px; animation: pop 0.2s; }
    @keyframes pop { from { scale: 0.8; opacity: 0; } to { scale: 1; opacity: 1; } }

    /* Inputs & Buttons */
    .stChatInputContainer {
        border-radius: 25px !important;
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(123,94,167,0.3) !important;
    }
    .stButton>button {
        border-radius: 20px !important;
        background: rgba(123,94,167,0.15) !important;
        transition: 0.3s;
    }
    .stButton>button:hover { background: #7B5EA7 !important; color: white !important; }

    </style>
    """, unsafe_allow_html=True)
