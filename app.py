import streamlit as st
import numpy as np

# Set page configuration
st.set_page_config(page_title="Valentine's Maze Game", page_icon="❤️", layout="centered")

# Custom CSS for Valentine's theme with Lily flowers
st.markdown(
    """
    <style>
    body {
        background: url('https://images.unsplash.com/photo-1561948955-570b270e7c36') no-repeat center center fixed;
        background-size: cover;
        color: white;
        font-family: 'Arial', sans-serif;
    }
    .stMarkdown h1 {
        color: pink;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 10px;
        animation: heartbeat 2s infinite;
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    .maze-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0 auto;
        padding: 10px;
    }
    .stButton button {
        background-color: pink;
        color: white;
        border-radius: 10px;
        border: 2px solid white;
        padding: 10px;
        font-size: 1rem;
        font-weight: bold;
        width: 100px;
    }
    .stButton button:hover {
        background-color: #ff66b2;
    }
    .lily-border {
        border: 5px solid pink;
        padding: 10px;
        border-radius: 15px;
        background: rgba(255, 255, 255, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.image("flowers.png", width=200)
st.title("❤️ Happy Valentine's, My Love! ❤️")
st.caption("May our love bloom like your favorite lilies! 🌸")

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

if 'player_pos' not in st.session_state:
    st.session_state.player_pos = [1, 1]

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

def check_win():
    x, y = st.session_state.player_pos
    return maze[x][y] == 3

def display_maze():
    maze_display = maze.copy()
    x, y = st.session_state.player_pos
    maze_display[x][y] = 2
    st.markdown("<div class='maze-container lily-border'>", unsafe_allow_html=True)
    for row in maze_display:
        st.write(" ".join(["💕" if cell == 2 else "❤️" if cell == 3 else "🌸" if cell == 0 else "⬛" for cell in row]))
    st.markdown("</div>", unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])
with col1:
    display_maze()
with col2:
    if st.button("⬆️ Up"):
        move_player("Up")
    if st.button("⬅️ Left"):
        move_player("Left")
    if st.button("➡️ Right"):
        move_player("Right")
    if st.button("⬇️ Down"):
        move_player("Down")

if check_win():
    st.balloons()
    st.success("🎉 You found my heart among the lilies! Love you always! 💖")
