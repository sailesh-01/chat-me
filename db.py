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
    
    # Messages table (Upgraded for Image Support)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT NOT NULL,
        receiver TEXT NOT NULL,
        content TEXT NOT NULL,
        msg_type TEXT DEFAULT 'text',
        timestamp REAL NOT NULL
    )
    """)
    
    # Typing Status table (New for Apex)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS typing_status (
        username TEXT PRIMARY KEY,
        target_username TEXT,
        last_active REAL
    )
    """)
    
    # Migration: Add msg_type if it doesn't exist (for existing DBs)
    try:
        cursor.execute("ALTER TABLE messages ADD COLUMN msg_type TEXT DEFAULT 'text'")
    except sqlite3.OperationalError:
        pass # Column already exists
        
    conn.commit()
    conn.close()

def send_message(sender, receiver, content, msg_type='text'):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (sender, receiver, content, msg_type, timestamp) VALUES (?, ?, ?, ?, ?)",
                 (sender, receiver, content, msg_type, time.time()))
    conn.commit()
    conn.close()

def update_typing_status(username, target_username):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO typing_status (username, target_username, last_active) VALUES (?, ?, ?)",
                 (username, target_username, time.time()))
    conn.commit()
    conn.close()

def get_typing_status(target_username, current_user):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Check if target is typing to current user within the last 5 seconds
    cursor.execute("SELECT last_active FROM typing_status WHERE username=? AND target_username=? AND last_active > ?",
                 (target_username, current_user, time.time() - 5))
    res = cursor.fetchone()
    conn.close()
    return True if res else False

def get_messages(user1, user2, limit=100):
    import storage
    
    # 1. Get Live Session Messages (SQLite)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT sender, receiver, content, timestamp, msg_type FROM messages 
    WHERE (sender=? AND receiver=?) OR (sender=? AND receiver=?)
    ORDER BY timestamp ASC LIMIT ?
    """, (user1, user2, user2, user1, limit))
    rows = cursor.fetchall()
    conn.close()
    
    live_msgs = []
    for row in rows:
        live_msgs.append({
            "sender": row[0],
            "receiver": row[1],
            "content": row[2],
            "timestamp": row[3],
            "type": row[4]
        })
    
    # 2. Get Permanent Legacy Messages (storage.py)
    legacy_msgs = []
    for msg in storage.LEGACY_CHAT:
        s, r, c, t = msg
        if (s == user1 and r == user2) or (s == user2 and r == user1) or (r == "any"):
            legacy_msgs.append({
                "sender": s,
                "receiver": r,
                "content": c,
                "timestamp": t,
                "type": "text"
            })
            
    # 3. Merge and Sort
    all_msgs = live_msgs + legacy_msgs
    all_msgs.sort(key=lambda x: x["timestamp"]) # Sort by timestamp
    
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
