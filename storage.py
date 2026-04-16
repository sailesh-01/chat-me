# Jaguars Elite Personal Data Storage
# This file is part of your repository and persists on Streamlit Cloud.
# To add users permanently, copy the "Git Entry" from the Signup page and paste it into USERS.

USERS = {
    # Format: "username": {"hash": "...", "name": "...", "color": "#FFB800"}
    "admin": {
        "hash": "$2b$12$Ej68z13o7N3U/e.U6.z7.OZ9u9mJg/6H2y6H.7H.7H.7H.7H.7H.", # Placeholder
        "name": "Head Jaguar",
        "color": "#FFB800"
    }
}

# Add messages here if you want them to be permanently visible in the chat.
LEGACY_CHAT = [
    # Format: ("sender_username", "receiver_username", "content", timestamp)
    ("admin", "any", "Welcome to the Jaguars Permanent Sector. Data integrity established.", 1713290000)
]
