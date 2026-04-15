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
        return False, "All fields are required"
    
    hashed = hash_password(password)
    if db.create_user(username, hashed, display_name):
        return True, "Account created successfully"
    else:
        return False, "Username already exists"

def logout_user():
    if "user" in st.session_state:
        del st.session_state.user
    st.rerun()
