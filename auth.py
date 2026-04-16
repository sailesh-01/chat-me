import bcrypt
import streamlit as st
import db

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def login_user(username, password):
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
        return False, "Protocol Error: Missing required credentials."
    
    if len(password) < 6:
        return False, "Security Breach: Password must be at least 6 characters."
    
    if not username.isalnum():
        return False, "Identification Error: Usernames must be alphanumeric."
    
    password_hash = hash_password(password)
    if db.create_user(username, password_hash, display_name):
        return True, "Welcome to the Jaguars! Account initialized successfully."
    else:
        return False, "Collision Detected: This JAG ID is already registered."

def logout_user():
    if "user" in st.session_state:
        del st.session_state.user
    st.rerun()
