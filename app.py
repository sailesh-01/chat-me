import streamlit as st
from streamlit_autorefresh import st_autorefresh
import db
import auth
import utils
import time

# Initialize database
db.init_db()

st.set_page_config(page_title="AstroChat", layout="wide", page_icon="🛸")
utils.inject_antigravity_styles()

# Authentication check
if "user" not in st.session_state:
    st.session_state.auth_mode = st.session_state.get("auth_mode", "Login")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h1 style='text-align: center;'>🛸 AstroChat</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; opacity: 0.7;'>Antigravity Real-Time Messaging</p>", unsafe_allow_html=True)
        
        mode = st.radio("Mode", ["Login", "Signup"], label_visibility="collapsed", horizontal=True)
        
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if mode == "Signup":
            display_name = st.text_input("Display Name")
            if st.button("Create Account", use_container_width=True):
                success, msg = auth.signup_user(username, password, display_name)
                if success:
                    st.success(msg)
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error(msg)
        else:
            if st.button("Login", use_container_width=True):
                if auth.login_user(username, password):
                    st.rerun()
                else:
                    st.error("Invalid username or password")
else:
    # Sidebar Navigation
    with st.sidebar:
        st.markdown(f"### Welcome, {st.session_state.user['display_name']}!")
        page = st.selectbox("Navigation", ["Chat", "Settings"])
        
        if st.button("Logout", use_container_width=True):
            auth.logout_user()

    if page == "Settings":
        st.title("🛸 AstroSettings")
        new_name = st.text_input("Display Name", value=st.session_state.user['display_name'])
        new_color = st.color_picker("Avatar Color", value=st.session_state.user['avatar_color'])
        
        if st.button("Save Profile"):
            db.update_user_profile(st.session_state.user['username'], new_name, new_color)
            st.session_state.user['display_name'] = new_name
            st.session_state.user['avatar_color'] = new_color
            st.success("Profile updated!")
            time.sleep(1)
            st.rerun()

    elif page == "Chat":
        # Auto-refresh every 2 seconds
        st_autorefresh(interval=2000, key="chatupdate")
        
        # Sidebar contact list
        users = db.get_all_users(exclude_user=st.session_state.user['username'])
        
        if not users:
            st.info("No other explorers found in this sector yet.")
        else:
            col_list, col_chat = st.columns([1, 3])
            
            with col_list:
                st.markdown("### Universe")
                # Simple contact selector
                contact_names = [u[1] for u in users]
                selected_name = st.radio("Sector", contact_names, label_visibility="collapsed")
                
                # Get selected user object
                selected_user = next(u for u in users if u[1] == selected_name)
                selected_username = selected_user[0]

            with col_chat:
                st.markdown(f"### 🛰️ Chatting with {selected_name}")
                
                # Container for messages with custom scroll CSS
                st.markdown('<div class="chat-container">', unsafe_allow_html=True)
                messages = db.get_messages(st.session_state.user['username'], selected_username)
                
                for msg in messages:
                    sender_username, receiver_username, content, timestamp = msg
                    is_sent = sender_username == st.session_state.user['username']
                    sender_display = st.session_state.user['display_name'] if is_sent else selected_name
                    utils.message_bubble(content, sender_display, is_sent, timestamp)
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Input area
                user_input = st.chat_input(f"Send a message to {selected_name}...")
                if user_input:
                    db.send_message(st.session_state.user['username'], selected_username, user_input)
                    st.rerun()
