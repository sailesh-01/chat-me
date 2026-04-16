import bcrypt
import streamlit as st
import storage # New Git-based storage
import db

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def login_user(username, password):
    # First, check the Git-Persisted Storage (storage.py)
    if username in storage.USERS:
        user_data = storage.USERS[username]
        if check_password(password, user_data["hash"]):
            st.session_state.user = {
                "username": username,
                "display_name": user_data["name"],
                "avatar_color": user_data["color"]
            }
            return True
    
    # Second, check the Live Session (SQLite) for brand new accounts not yet synced
    user = db.get_user(username)
    if user and check_password(password, user[1]):
        st.session_state.user = {
            "username": user[0],
            "display_name": user[2],
            "avatar_color": user[3]
        }
        return True
        
    return False

def signup_user(username, password, display_name):
    if not username or not password or not display_name:
        return False, "Protocol Error: Missing credentials."
    
    if len(password) < 6:
        return False, "Security Breach: Password must be 6+ chars."
    
    # Check if exists in storage
    if username in storage.USERS:
        return False, "Collision Resolved: This ID is permanently reserved."
        
    password_hash = hash_password(password)
    
    # Add to SQLite for current session use
    if db.create_user(username, password_hash, display_name):
        # Generate the string for manual persistence
        code_snippet = f'"{username}": {{"hash": "{password_hash}", "name": "{display_name}", "color": "#FFB800"}},'
        return True, code_snippet
    else:
        return False, "Collision Detected: This JAG ID exists in session."

def logout_user():
    if "user" in st.session_state:
        del st.session_state.user
    st.rerun()
