import streamlit as st
from streamlit_autorefresh import st_autorefresh
import db
import auth
import utils
import time

# Initialize database
db.init_db()

st.set_page_config(page_title="Jaguars", layout="wide", page_icon="🐆")
utils.inject_antigravity_styles()

# Authentication check
if "user" not in st.session_state:
    st.session_state.auth_mode = st.session_state.get("auth_mode", "Login")
    st.session_state.auth_error = st.session_state.get("auth_error", False)
    
    # Background Trigger for Login
    st.markdown('<div class="login-container"></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Dynamic Header
        header_title = "🐆 JAGUARS" if st.session_state.auth_mode == "Login" else "🐆 JOIN THE PRIDE"
        header_subtitle = "ELITE COMM-LINK" if st.session_state.auth_mode == "Login" else "BECOME A HUNTER"
        
        st.markdown(f"""
        <div class="glass-card">
            <h1 style='text-align: center; margin-bottom: 0; color: #FFB800;'>{header_title}</h1>
            <p style='text-align: center; opacity: 0.6; margin-bottom: 30px; letter-spacing: 2px; font-size: 10px;'>{header_subtitle}</p>
        </div>
        """, unsafe_allow_html=True)
        
        mode = st.radio("Mode", ["Login", "Signup"], label_visibility="collapsed", horizontal=True, key="auth_toggle")
        st.session_state.auth_mode = mode
        
        username = st.text_input("Username", placeholder="JAG ID")
        password = st.text_input("Password", type="password", placeholder="Access Key")
        
        if mode == "Signup":
            display_name = st.text_input("Display Name", placeholder="Callsign")
            if st.button("Initialize Account", use_container_width=True):
                with st.spinner("Initializing Jaguar Profile..."):
                    success, result = auth.signup_user(username, password, display_name)
                    if success:
                        st.success("Welcome to the Jaguars! Account initialized for this session.")
                        st.info("⚠️ **Action Required for Persistence:**")
                        st.code(result, language="python")
                        st.caption("To keep this account permanently, paste the line above into `storage.py` and push to GitHub.")
                        st.session_state.auth_error = False
                    else:
                        st.error(result)
                        st.session_state.auth_error = True
        else:
            if st.button("Establish Connection", use_container_width=True):
                with st.spinner("Establishing Secure Comm-Link..."):
                    if auth.login_user(username, password):
                        st.session_state.auth_error = False
                        st.rerun()
                    else:
                        st.session_state.auth_error = True
                        st.error("Protocol Error: Invalid JAG ID or Access Key")
else:
    # Sidebar Navigation
    with st.sidebar:
        # Hunter Profile Card
        st.markdown(f"""
        <div class="profile-card">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
                <div style="width: 40px; height: 40px; border-radius: 50%; background: {st.session_state.user['avatar_color']}; display: flex; align-items: center; justify-content: center; color: #000; font-weight: 800; border: 2px solid rgba(255,184,0,0.5);">
                    {st.session_state.user['display_name'][0].upper()}
                </div>
                <div>
                    <h4>{st.session_state.user['display_name']}</h4>
                    <p style="font-size: 10px; opacity: 0.6; margin: 0;"><span class="status-light"></span>ONLINE</p>
                </div>
            </div>
            <p style="font-size: 9px; opacity: 0.4; letter-spacing: 1px; margin: 0;">JAG-ID: {st.session_state.user['username']}@Sector-7</p>
        </div>
        """, unsafe_allow_html=True)
        
        # AI Core Status Hub (Rotating)
        import random
        statuses = [
            "SATELLITE LINK: 98% STABLE",
            "ATMOSPHERIC INTERFERENCE: MINIMAL",
            "JAG-CORE PULSE: OPTIMAL",
            "ENCRYPTION KEY: ROTATING...",
            "SECTOR SCAN: ACTIVE",
            "BIO-LINK: ESTABLISHED"
        ]
        active_status = statuses[int(time.time() / 10) % len(statuses)]
        st.markdown(f'<div class="status-hub">{active_status}</div>', unsafe_allow_html=True)
        
        st.markdown("### 🗺️ CONTROL")
        page = st.radio("Navigation", ["Chat", "Settings"], label_visibility="collapsed")
        
        st.markdown("---")
        if st.button("TERMINATE CONNECTION", use_container_width=True):
            auth.logout_user()

    if page == "Settings":
        st.markdown("<h1 style='color: #FFB800;'>🐆 JAGUAR CONFIG</h1>", unsafe_allow_html=True)
        new_name = st.text_input("Display Name", value=st.session_state.user['display_name'])
        new_color = st.color_picker("Avatar Color", value=st.session_state.user['avatar_color'])
        
        if st.button("SAVE PROFILE", use_container_width=True):
            db.update_user_profile(st.session_state.user['username'], new_name, new_color)
            st.session_state.user['display_name'] = new_name
            st.session_state.user['avatar_color'] = new_color
            st.success("Profile Updated")
            time.sleep(1)
            st.rerun()

    elif page == "Chat":
        st_autorefresh(interval=2000, key="chatupdate")
        
        users = db.get_all_users(exclude_user=st.session_state.user['username'])
        
        if not users:
            st.info("Searching for other hunters in this sector...")
        else:
            col_list, col_chat = st.columns([1, 3])
            
            with col_list:
                st.markdown("### 🔭 SECTORS")
                contact_names = [u[1] for u in users]
                selected_name = st.radio("Sectors", contact_names, label_visibility="collapsed")
                
                selected_user = next(u for u in users if u[1] == selected_name)
                selected_username = selected_user[0]
                
                # Check for "Hunting..." (Typing) Status
                is_typing = db.get_typing_status(selected_username, st.session_state.user['username'])
                
                # Detect Sector Change for Glitch Effect
                if "last_sector" not in st.session_state:
                    st.session_state.last_sector = selected_username
                
                glitch_class = ""
                if st.session_state.last_sector != selected_username:
                    glitch_class = "sector-scan-active"
                    st.session_state.last_sector = selected_username

                st.markdown(f"""
                <div class="{glitch_class}" style="margin-top: 20px; padding: 10px; border-radius: 10px; background: rgba(255,184,0,0.05); border-left: 3px solid #FFB800;">
                    <p style="font-size: 10px; margin: 0; color: #FFB800; font-weight: 800;">TARGET SECTOR {' - 🐆 HUNTING...' if is_typing else ''}</p>
                    <p style="font-size: 12px; margin: 0; opacity: 0.8;">{selected_username}@Jaguars</p>
                </div>
                """, unsafe_allow_html=True)

            with col_chat:
                st.markdown(f"<h3 style='margin-bottom: 10px;'>🐆 {selected_name.upper()}</h3>", unsafe_allow_html=True)
                
                # Container for messages with custom scroll CSS
                st.markdown('<div class="chat-container">', unsafe_allow_html=True)
                messages = db.get_messages(st.session_state.user['username'], selected_username)
                
                last_sender = None
                last_date = None
                
                for msg in messages:
                    # Date separation logic
                    msg_date = time.strftime("%Y-%m-%d", time.localtime(msg['timestamp']))
                    if msg_date != last_date:
                        date_display = time.strftime("%B %d, %Y", time.localtime(msg['timestamp']))
                        utils.date_divider(f"EARTH DATE: {date_display}")
                        last_date = msg_date
                        last_sender = None
                    
                    is_sent = msg['sender'] == st.session_state.user['username']
                    is_grouped = (msg['sender'] == last_sender)
                    
                    sender_display = st.session_state.user['display_name'] if is_sent else selected_name
                    avatar_color = st.session_state.user['avatar_color'] if is_sent else selected_user[2]
                    
                    utils.message_bubble(
                        msg['content'], 
                        sender_display, 
                        is_sent, 
                        msg['timestamp'], 
                        avatar_color=avatar_color,
                        is_grouped=is_grouped,
                        msg_type=msg['type']
                    )
                    last_sender = msg['sender']
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Input area
                with st.container():
                    col_input, col_file = st.columns([5, 1])
                    with col_input:
                        user_input = st.chat_input(f"Send intel to {selected_name}...")
                        import base64
                        if user_input:
                            db.send_message(st.session_state.user['username'], selected_username, user_input)
                            st.rerun()
                        
                        # Update Typing Status
                        if st.session_state.get('typing_active', False) or user_input:
                            db.update_typing_status(st.session_state.user['username'], selected_username)
                    
                    with col_file:
                        intel_file = st.file_uploader("INTEL", type=['png', 'jpg', 'jpeg'], label_visibility="collapsed")
                        if intel_file:
                            byte_data = intel_file.read()
                            base64_img = f"data:image/png;base64,{base64.b64encode(byte_data).decode()}"
                            db.send_message(st.session_state.user['username'], selected_username, base64_img, msg_type='image')
                            st.rerun()
