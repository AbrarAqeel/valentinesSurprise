import streamlit as st
import numpy as np
import time

# Set page configuration
st.set_page_config(page_title="Valentine's Maze Game", page_icon="❤️", layout="centered")

# Custom CSS for a more romantic and immersive theme
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #ffcccc, #ff99cc);
        color: white;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-align: center;
    }
    .stMarkdown h1 {
        color: white;
        font-size: 3rem;
        text-shadow: 2px 2px 8px #ff4d4d;
    }
    .maze-container {
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 2rem;
        padding: 10px;
    }
    .button-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: 20px;
    }
    .stButton button {
        background-color: #ff1a1a;
        color: white;
        border-radius: 15px;
        padding: 10px;
        font-size: 1rem;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(255, 0, 0, 0.5);
    }
    .stButton button:hover {
        background-color: #ff4d4d;
    }
    .heart-animation {
        font-size: 3rem;
        animation: heartbeat 1s infinite;
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add background music
st.markdown(
    """
    <audio autoplay loop>
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
    </audio>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1 class='heart-animation'>❤️ Happy Valentine's, My Love! ❤️</h1>", unsafe_allow_html=True)
st.caption("Find your way to my heart in this lovely maze! 💖")

# Maze setup
maze = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 3, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

# Initialize player position
if 'player_pos' not in st.session_state:
    st.session_state.player_pos = [1, 1]

# Function to move player
def move_player(direction):
    x, y = st.session_state.player_pos
    if direction == "Up" and maze[x - 1][y] != 1:
        st.session_state.player_pos[0] -= 1
    elif direction == "Down" and maze[x + 1][y] != 1:
        st.session_state.player_pos[0] += 1
    elif direction == "Left" and maze[x][y - 1] != 1:
        st.session_state.player_pos[1] -= 1
    elif direction == "Right" and maze[x][y + 1] != 1:
        st.session_state.player_pos[1] += 1
    time.sleep(0.1)  # Smooth movement

# Check if the player reached the goal
def check_win():
    x, y = st.session_state.player_pos
    return maze[x][y] == 3

# Display the maze
def display_maze():
    maze_display = maze.copy()
    x, y = st.session_state.player_pos
    maze_display[x][y] = 2
    st.markdown("<div class='maze-container'>", unsafe_allow_html=True)
    for row in maze_display:
        st.write(" ".join(["💗" if cell == 2 else "❤️" if cell == 3 else "⬛" if cell == 1 else "⬜" for cell in row]))
    st.markdown("</div>", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([3, 1])
with col1:
    display_maze()
with col2:
    st.markdown("<h3>Controls</h3>", unsafe_allow_html=True)
    if st.button("⬆️ Up"):
        move_player("Up")
    if st.button("⬅️ Left"):
        move_player("Left")
    if st.button("➡️ Right"):
        move_player("Right")
    if st.button("⬇️ Down"):
        move_player("Down")

# Winning condition
if check_win():
    st.balloons()
    st.success("🎉 You found my heart! I love you endlessly, my sweet angel! 💖")
