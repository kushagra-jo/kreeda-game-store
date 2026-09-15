import streamlit as st

st.set_page_config(page_title="Kreeda Store", page_icon="🎮", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #eaf6ff 0%, #ffffff 45%, #dcefff 100%);
    color: #172033;
}

header[data-testid="stHeader"] {
    background: #171d25;
}

.block-container {
    padding-top: 1.5rem;
    padding-left: 4rem;
    padding-right: 4rem;
}

.topbar {
    background: #171d25;
    padding: 18px 28px;
    border-radius: 8px;
    margin-bottom: 25px;
}

.logo {
    color: #66c0f4;
    font-size: 30px;
    font-weight: 800;
}

.tagline {
    color: #c7d5e0;
    font-size: 14px;
}

.hero {
    background: linear-gradient(120deg, #1b4f72, #2a82b8);
    padding: 38px;
    border-radius: 10px;
    color: white;
    margin-bottom: 28px;
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 5px;
}

.hero p {
    color: #d9efff;
    font-size: 17px;
}

.game-title {
    color: #1b4f72;
    font-size: 22px;
    font-weight: 700;
}

.game-genre {
    color: #68788a;
    font-size: 14px;
}

.game-price {
    color: #1677b8;
    font-size: 21px;
    font-weight: bold;
}

.section {
    color: #1b4f72;
    font-size: 27px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 15px;
}

div.stButton > button {
    background: #1a9fff;
    color: white;
    border: none;
    border-radius: 4px;
    font-weight: 600;
}

div.stButton > button:hover {
    background: #147dcc;
    color: white;
}

[data-testid="stSidebar"] {
    background: #171d25;
}

[data-testid="stSidebar"] * {
    color: #d6e4ef !important;
}

div[data-baseweb="select"] > div {
    background-color: white;
}
</style>
""", unsafe_allow_html=True)

games = {
    "Counter Strike 2": {"genre": "Action", "price": 0, "tag": "Free to Play", "image": "images/cs2.jpg"},
    "Minecraft": {"genre": "Adventure", "price": 2000, "tag": "Popular", "image": "images/minecraft.jpg"},
    "GTA V": {"genre": "Action", "price": 2600, "tag": "Open World", "image": "images/gta5.jpg"},
    "Elden Ring": {"genre": "RPG", "price": 3000, "tag": "Award Winner", "image": "images/eldenring.jpg"},
    "Red Dead Redemption 2": {"genre": "Adventure", "price": 2300, "tag": "Open World", "image": "images/rdr2.jpg"},
    "FIFA 25": {"genre": "Sports", "price": 2800, "tag": "Sports", "image": "images/fifa25.jpg"}
}

if "cart" not in st.session_state:
    st.session_state.cart = []

st.markdown("""
<div class="topbar">
    <span class="logo">🎮 KREEDA</span>
    <span class="tagline"> &nbsp; Your Gaming Store</span>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio("STORE MENU", ["Store", "Library", "Cart", "About"])

if page == "Store":

    st.markdown("""
    <div class="hero">
        <h1>Welcome to KREEDA</h1>
        <p>Discover your next favourite game.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section">Featured Games</div>', unsafe_allow_html=True)

    search = st.text_input("🔎 Search the store", placeholder="Search for a game...")

    genre = st.selectbox("Genre", ["All", "Action", "Adventure", "RPG", "Sports"])

    filtered = []

    for name, game in games.items():
        if search.lower() in name.lower():
            if genre == "All" or game["genre"] == genre:
                filtered.append((name, game))

    cols = st.columns(3)

    for i, (name, game) in enumerate(filtered):
        with cols[i % 3]:
            st.image(game["image"], use_container_width=True)
            st.markdown(f'<div class="game-title">{name}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="game-genre">{game["genre"]} • {game["tag"]}</div>', unsafe_allow_html=True)
            st.write("")
        
            if game["price"] == 0:
                st.markdown('<div class="game-price">Free to Play</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="game-price">₹{game["price"]}</div>', unsafe_allow_html=True)

            if st.button("Add to Cart", key="add_" + name):
                st.session_state.cart.append(name)
                st.success("Added to cart")

elif page == "Library":

    st.markdown('<div class="section">Your Library</div>', unsafe_allow_html=True)

    if st.session_state.cart:
        st.info("Games currently in your cart:")
        for game in st.session_state.cart:
            st.write("🎮", game)
    else:
        st.info("Your library is empty. Browse the store to find games.")

elif page == "Cart":

    st.markdown('<div class="section">Shopping Cart</div>', unsafe_allow_html=True)

    if not st.session_state.cart:
        st.info("Your cart is empty.")
    else:
        total = 0

        for game in st.session_state.cart:
            price = games[game]["price"]
            total += price
            st.write(f"🎮 **{game}** — ₹{price}")

        st.markdown("---")
        st.subheader(f"Total: ₹{total}")

        if st.button("Purchase"):
            st.success("Purchase successful! The games have been added to your library.")

        if st.button("Clear Cart"):
            st.session_state.cart = []
            st.rerun()

elif page == "About":

    st.markdown('<div class="section">About Kreeda</div>', unsafe_allow_html=True)

    st.write("Kreeda is a simple gaming store application built using Python and Streamlit.")

    st.info("Browse games, search by name, filter by genre and manage your shopping cart.")

    st.write("Built for Python Lab 6-a.")
