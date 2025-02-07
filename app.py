import streamlit as st
import numpy as np

# Set page configuration
st.set_page_config(page_title="Valentine's Maze Game", page_icon="❤️", layout="centered")

# Custom CSS for Valentine's theme
st.markdown(
    """
    <style>
    /* Gradient background */
    body {
        background: linear-gradient(135deg, #ff6b6b, #ff4d4d, #ff1a1a);
        color: white;
        font-family: 'Arial', sans-serif;
    }
    /* Title styling */
    .stMarkdown h1 {
        color: white;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 10px;
    }
    /* Caption styling */
    .stMarkdown p {
        color: white;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 20px;
    }
    /* Maze container */
    .maze-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0 auto;
        padding: 10px;
    }
    /* Legend styling */
    .legend {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
        margin: 20px 0;
    }
    .legend-item {
        display: flex;
        align-items: center;
        margin: 5px 0;
        font-size: 1rem;
        color: white;
    }
    /* Button styling */
    .stButton button {
        background-color: #ff1a1a;
        color: white;
        border-radius: 10px;
        border: 2px solid white;
        padding: 8px 16px; /* Smaller buttons */
        font-size: 0.9rem; /* Smaller font */
        font-weight: bold;
        margin: 5px;
        width: 80px; /* Fixed width for buttons */
    }
    .stButton button:hover {
        background-color: #ff4d4d;
        color: white;
    }
    /* Button container */
    .button-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and romantic caption
st.title("❤️ Valentine's Maze Game ❤️")
st.caption("Find your way to my heart, my love! 💖")

# Maze layout (0 = empty, 1 = wall/obstacle, 2 = player, 3 = goal)
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

# Function to move the player
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
    st.experimental_rerun()  # Force rerun to update the maze immediately

# Check if the player reached the goal
def check_win():
    x, y = st.session_state.player_pos
    return maze[x][y] == 3

# Display the maze
def display_maze():
    maze_display = maze.copy()
    x, y = st.session_state.player_pos
    maze_display[x][y] = 2  # Player position
    st.markdown("<div class='maze-container'>", unsafe_allow_html=True)
    for row in maze_display:
        st.write(" ".join(["💗" if cell == 2 else "❤️" if cell == 3 else "⬛" if cell == 1 else "⬜" for cell in row]))
    st.markdown("</div>", unsafe_allow_html=True)

# Display the legend
def display_legend():
    st.markdown("<div class='legend'>", unsafe_allow_html=True)
    st.markdown("<div class='legend-item'>💗 Player</div>", unsafe_allow_html=True)
    st.markdown("<div class='legend-item'>❤️ Goal</div>", unsafe_allow_html=True)
    st.markdown("<div class='legend-item'>⬛ Wall</div>", unsafe_allow_html=True)
    st.markdown("<div class='legend-item'>⬜ Empty</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Layout for mobile-friendly design
col1, col2 = st.columns([1, 1])
with col1:
    display_maze()
with col2:
    display_legend()

# Buttons for movement (placed below the maze and legend)
st.markdown("<div class='button-container'>", unsafe_allow_html=True)
col_left, col_mid, col_right = st.columns([1, 1, 1])
with col_left:
    if st.button("⬆️ Up"):
        move_player("Up")
with col_mid:
    if st.button("⬅️ Left"):
        move_player("Left")
    if st.button("➡️ Right"):
        move_player("Right")
with col_right:
    if st.button("⬇️ Down"):
        move_player("Down")
st.markdown("</div>", unsafe_allow_html=True)

# Check if the player won
if check_win():
    st.balloons()
    st.success("🎉 You found my heart! I love you! 💖")
