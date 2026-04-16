import sqlite3
import time

DB_FILE = "chat.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password_hash TEXT NOT NULL,
        display_name TEXT,
        avatar_color TEXT DEFAULT '#7B5EA7'
    )
    """)
    
    # Messages table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT NOT NULL,
        receiver TEXT NOT NULL,
        content TEXT NOT NULL,
        timestamp REAL NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def send_message(sender, receiver, content):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (sender, receiver, content, timestamp) VALUES (?, ?, ?, ?)",
                 (sender, receiver, content, time.time()))
    conn.commit()
    conn.close()

def get_messages(user1, user2, limit=100):
    import storage
    
    # 1. Get Live Session Messages (SQLite)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT sender, receiver, content, timestamp FROM messages 
    WHERE (sender=? AND receiver=?) OR (sender=? AND receiver=?)
    ORDER BY timestamp ASC LIMIT ?
    """, (user1, user2, user2, user1, limit))
    live_msgs = cursor.fetchall()
    conn.close()
    
    # 2. Get Permanent Legacy Messages (storage.py)
    legacy_msgs = []
    for msg in storage.LEGACY_CHAT:
        s, r, c, t = msg
        if (s == user1 and r == user2) or (s == user2 and r == user1) or (r == "any"):
            legacy_msgs.append(msg)
            
    # 3. Merge and Sort
    all_msgs = list(live_msgs) + legacy_msgs
    all_msgs.sort(key=lambda x: x[3]) # Sort by timestamp
    
    return all_msgs[-limit:] # Return the latest entries

def get_all_users(exclude_user=None):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    if exclude_user:
        cursor.execute("SELECT username, display_name, avatar_color FROM users WHERE username != ?", (exclude_user,))
    else:
        cursor.execute("SELECT username, display_name, avatar_color FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

def update_user_profile(username, display_name, avatar_color):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET display_name=?, avatar_color=? WHERE username=?",
                 (display_name, avatar_color, username))
    conn.commit()
    conn.close()

def get_user(username):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT username, password_hash, display_name, avatar_color FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def create_user(username, password_hash, display_name):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password_hash, display_name) VALUES (?, ?, ?)",
                     (username, password_hash, display_name))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()
