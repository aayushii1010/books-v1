import streamlit as st
import random

# ----------------------------------
# BOOKSY DATABASE
# ----------------------------------

book_database = {
    "📖 Fiction": {
        "Cozy": [
            "The House in the Cerulean Sea by TJ Klune",
            "Legends & Lattes by Travis Baldree",
            "A Psalm for the Wild-Built by Becky Chambers",
            "Anne of Green Gables by L.M. Montgomery"
        ],
        "Romance": [
            "The Love Hypothesis by Ali Hazelwood",
            "Better Than the Movies by Lynn Painter",
            "Book Lovers by Emily Henry",
            "The Spanish Love Deception by Elena Armas"
        ],
        "Thrilling": [
            "The Silent Patient by Alex Michaelides",
            "Gone Girl by Gillian Flynn",
            "Behind Closed Doors by B.A. Paris",
            "The Girl on the Train by Paula Hawkins"
        ],
        "Fantasy": [
            "Harry Potter and the Sorcerer's Stone by J.K. Rowling",
            "The Hobbit by J.R.R. Tolkien",
            "Fourth Wing by Rebecca Yarros",
            "Six of Crows by Leigh Bardugo"
        ],
        "Sci-Fi": [
            "Project Hail Mary by Andy Weir",
            "Dune by Frank Herbert",
            "The Martian by Andy Weir",
            "Ender's Game by Orson Scott Card"
        ]
    },

    "🧠 Non-Fiction": {
        "Inspiring": [
            "Atomic Habits by James Clear",
            "The Alchemist by Paulo Coelho",
            "Shoe Dog by Phil Knight",
            "Ikigai by Héctor García"
        ],
        "Self-Help": [
            "Think Like a Monk by Jay Shetty",
            "The Mountain Is You by Brianna Wiest",
            "Deep Work by Cal Newport",
            "The Psychology of Money by Morgan Housel"
        ],
        "Business": [
            "Zero to One by Peter Thiel",
            "The Lean Startup by Eric Ries",
            "Rich Dad Poor Dad by Robert Kiyosaki",
            "Good to Great by Jim Collins"
        ]
    }
}
# ----------------------------------
# BOOK COVERS
# ----------------------------------

book_covers = {

    # Cozy
    "The House in the Cerulean Sea by TJ Klune":
        "book_covers/house_cerulean_sea.jpg",

    "Legends & Lattes by Travis Baldree":
        "book_covers/legends_lattes.jpg",

    "A Psalm for the Wild-Built by Becky Chambers":
        "book_covers/psalm_wild_built.jpg",

    "Anne of Green Gables by L.M. Montgomery":
        "book_covers/anne_green_gables.jpg",


    # Romance
    "The Love Hypothesis by Ali Hazelwood":
        "book_covers/love_hypothesis.jpg",

    "Better Than the Movies by Lynn Painter":
        "book_covers/better_than_movies.jpg",

    "Book Lovers by Emily Henry":
        "book_covers/book_lovers.jpg",

    "The Spanish Love Deception by Elena Armas":
        "book_covers/spanish_love_deception.jpg",


    # Thrilling
    "The Silent Patient by Alex Michaelides":
        "book_covers/silent_patient.jpg",

    "Gone Girl by Gillian Flynn":
        "book_covers/gone_girl.jpg",

    "Behind Closed Doors by B.A. Paris":
        "book_covers/behind_closed_doors.jpg",

    "The Girl on the Train by Paula Hawkins":
        "book_covers/girl_on_train.jpg",


    # Fantasy
    "Harry Potter and the Sorcerer's Stone by J.K. Rowling":
        "book_covers/harry_potter.jpg",

    "The Hobbit by J.R.R. Tolkien":
        "book_covers/hobbit.jpg",

    "Fourth Wing by Rebecca Yarros":
        "book_covers/fourth_wing.jpg",

    "Six of Crows by Leigh Bardugo":
        "book_covers/six_of_crows.jpg",


    # Sci-Fi
    "Project Hail Mary by Andy Weir":
        "book_covers/project_hail_mary.jpg",

    "Dune by Frank Herbert":
        "book_covers/dune.jpg",

    "The Martian by Andy Weir":
        "book_covers/martian.jpg",

    "Ender's Game by Orson Scott Card":
        "book_covers/enders_game.jpg",


    # Inspiring
    "Atomic Habits by James Clear":
        "book_covers/atomic_habits.jpg",

    "The Alchemist by Paulo Coelho":
        "book_covers/alchemist.jpg",

    "Shoe Dog by Phil Knight":
        "book_covers/shoe_dog.jpg",

    "Ikigai by Héctor García":
        "book_covers/ikigai.jpg",


    # Self Help
    "Think Like a Monk by Jay Shetty":
        "book_covers/think_like_monk.jpg",

    "The Mountain Is You by Brianna Wiest":
        "book_covers/mountain_is_you.jpg",

    "Deep Work by Cal Newport":
        "book_covers/deep_work.jpg",

    "The Psychology of Money by Morgan Housel":
        "book_covers/psychology_money.jpg",


    # Business
    "Zero to One by Peter Thiel":
        "book_covers/zero_to_one.jpg",

    "The Lean Startup by Eric Ries":
        "book_covers/lean_startup.jpg",

    "Rich Dad Poor Dad by Robert Kiyosaki":
        "book_covers/rich_dad_poor_dad.jpg",

    "Good to Great by Jim Collins":
        "book_covers/good_to_great.jpg"
}

book_descriptions = {

    "The House in the Cerulean Sea by TJ Klune":
    "🌈 A heartwarming magical story about found family and acceptance.",

    "Legends & Lattes by Travis Baldree":
    "☕ Cozy fantasy about an orc opening a coffee shop.",

    "A Psalm for the Wild-Built by Becky Chambers":
    "🤖 A thoughtful journey about purpose, humanity, and friendship.",

    "Anne of Green Gables by L.M. Montgomery":
    "🌸 A charming classic following imaginative Anne through life.",

    "The Love Hypothesis by Ali Hazelwood":
    "💕 Fake dating, academic rivals, and plenty of chemistry.",

    "Better Than the Movies by Lynn Painter":
    "🎬 A sweet rom-com perfect for lovers of happy endings.",

    "Book Lovers by Emily Henry":
    "📚 A witty romance between two people who love books.",

    "The Spanish Love Deception by Elena Armas":
    "💃 Fake dating, slow burn romance, and lots of tension.",

    "The Silent Patient by Alex Michaelides":
    "🔪 A psychological thriller with a shocking twist.",

    "Gone Girl by Gillian Flynn":
    "🕵️ Dark, gripping thriller full of secrets and lies.",

    "Behind Closed Doors by B.A. Paris":
    "🚪 A chilling suspense novel that keeps you guessing.",

    "The Girl on the Train by Paula Hawkins":
    "🚆 Mystery and suspense told through unreliable memories.",

    "Harry Potter and the Sorcerer's Stone by J.K. Rowling":
    "⚡ The magical beginning of Harry's Hogwarts journey.",

    "The Hobbit by J.R.R. Tolkien":
    "🧙 An epic fantasy adventure filled with dragons and treasure.",

    "Fourth Wing by Rebecca Yarros":
    "🐉 Dragons, danger, romance, and thrilling competition.",

    "Six of Crows by Leigh Bardugo":
    "💰 A clever fantasy heist with unforgettable characters.",

    "Project Hail Mary by Andy Weir":
    "🚀 A thrilling space mission to save humanity.",

    "Dune by Frank Herbert":
    "🏜️ Political intrigue, destiny, and epic science fiction.",

    "The Martian by Andy Weir":
    "🌌 Survival, science, and humor on Mars.",

    "Ender's Game by Orson Scott Card":
    "🛰️ A brilliant young strategist prepares for an alien war.",

    "Atomic Habits by James Clear":
    "📈 Learn how tiny habits create remarkable results.",

    "The Alchemist by Paulo Coelho":
    "✨ An inspiring tale about following your dreams.",

    "Shoe Dog by Phil Knight":
    "👟 The fascinating story behind Nike's success.",

    "Ikigai by Héctor García":
    "🌿 Discover the Japanese secret to a meaningful life.",

    "Think Like a Monk by Jay Shetty":
    "🧘 Wisdom and habits inspired by monk life.",

    "The Mountain Is You by Brianna Wiest":
    "⛰️ A guide to overcoming self-sabotage and growing.",

    "Deep Work by Cal Newport":
    "🎯 Master focus and productivity in a distracted world.",

    "The Psychology of Money by Morgan Housel":
    "💰 Timeless lessons about wealth and financial behavior.",

    "Zero to One by Peter Thiel":
    "🚀 Learn how innovative startups create the future.",

    "The Lean Startup by Eric Ries":
    "📊 Build businesses smarter through experimentation.",

    "Rich Dad Poor Dad by Robert Kiyosaki":
    "🏦 Financial lessons that challenge traditional thinking.",

    "Good to Great by Jim Collins":
    "🏆 Discover what makes companies truly exceptional."
}
# ----------------------------------
# QUOTES
# ----------------------------------

quotes = [
"📖 A reader lives a thousand lives before he dies.",
"🌸 Books and coffee make everything better.",
"✨ Reading is dreaming with open eyes.",
"💜 Between the pages of a book is a lovely place to be.",
"🌼 One more chapter never hurt anybody."
]

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="Booksy",
    page_icon="📚",
    layout="centered"
)
# ----------------------------------
# THEME TOGGLE
# ----------------------------------

theme = st.sidebar.toggle(
    "🌙 Dark Academia Mode"
)
if theme:

    # DARK ACADEMIA

    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(
            135deg,
            #0f0b0b,
            #1a1410,
            #2d1f17
        );
    }

    h1 {
        color: #D4AF37 !important;
        text-align: center;
    }

    h2, h3 {
        color: #E6C78B !important;
    }

    p, label {
        color: #F5E6CC !important;
    }

    section[data-testid="stSidebar"] {
        background: #15100d;
    }

    .stButton > button {
        background: #6B4423 !important;
        color: white !important;
        border-radius: 12px !important;
    }

    </style>
    """, unsafe_allow_html=True)

else:

    # PASTEL THEME

    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(
            135deg,
            #FFF8FC 0%,
            #F6EDFF 50%,
            #FFF9D6 100%
        );
    }

    h1 {
        color: #B26CFF !important;
        text-align: center;
    }

    h2, h3 {
        color: #FF7EB6 !important;
    }

    p, label {
        color: #5F4B66 !important;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #FFEAF4,
            #F3E7FF
        );
    }

    .stButton > button {
        background: linear-gradient(
            90deg,
            #FFB7D5,
            #DAB6FF
        ) !important;

        color: #4A3A55 !important;
        border-radius: 12px !important;
    }

    </style>
    """, unsafe_allow_html=True)

# ----------------------------------
# SESSION STATE
# ----------------------------------

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "recommendations" not in st.session_state:
    st.session_state.recommendations = []

# ----------------------------------
# SIDEBAR
# ----------------------------------

st.sidebar.markdown(
    "## 📚🌸 Booksey"
)
st.sidebar.write("Your Personal AI Book Matcher")

st.sidebar.markdown("---")

st.sidebar.info(
    "Choose a category and vibe to discover your next favorite book!"
)

st.sidebar.markdown("---")

st.sidebar.subheader("❤️ Favorites")
st.sidebar.markdown("---")

st.sidebar.markdown("---")

st.sidebar.subheader("📊 Stats")

st.sidebar.metric(
    "❤️ Favorites",
    len(st.session_state.favorites)
)

st.sidebar.metric(
    "📚 Recommendations",
    len(st.session_state.recommendations)
)

st.sidebar.info(
    f"📚 {len(st.session_state.recommendations)} books recommended"
)
if st.session_state.favorites:
    for book in st.session_state.favorites:
        st.sidebar.write(f"📖 {book}")
else:
    st.sidebar.write("No favorites yet.")

# ----------------------------------
# MAIN PAGE
# ----------------------------------

st.markdown(
    "<h1>🌸📚 Booksey 📚🌸</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<center>✨ 🌸 📖 💜 🌼 📚 🌸 ✨</center>",
    unsafe_allow_html=True
)

st.caption(
"🌸 Find your next favorite book in the cutest way possible 💜"
)


st.success(
"💖 Welcome to Booksy! Let's find your perfect read ✨"
)


st.subheader("Your Personal AI Book Matcher")

st.success(random.choice(quotes))

st.write(
    "Discover books based on your mood, interests, and reading preferences."
)
# ----------------------------------
# SEARCH BOOKS
# ----------------------------------

st.markdown("### 🔍 Search Books")

search = st.text_input(
    "Search by title"
)

if search:

    results = []

    for category in book_database:
        for vibe in book_database[category]:
            for book in book_database[category][vibe]:

                if search.lower() in book.lower():
                    results.append(book)

    if results:

        st.success(
            f"Found {len(results)} book(s)"
        )

        for book in results:
            st.write(f"📚 {book}")

    else:
        st.warning("No books found.")
# ----------------------------------
# MOOD
# ----------------------------------

st.markdown("### 🤖 How are you feeling today?")

mood = st.radio(
    "",
    ["😊 Happy", "😌 Relaxed", "🔥 Excited", "🥺 Emotional"]
)

if mood == "😊 Happy":
    st.success("Perfect day for Romance and Cozy reads!")

elif mood == "😌 Relaxed":
    st.success("Cozy books are calling your name!")

elif mood == "🔥 Excited":
    st.success("Thrillers and Fantasy await!")

elif mood == "🥺 Emotional":
    st.success("Romance and Inspiring reads might be perfect.")


# ----------------------------------
# READING COMPANION
# ----------------------------------

st.markdown("### ☕ What's your reading companion?")

drink = st.selectbox(
    "",
    [
        "☕ Coffee",
        "🫖 Tea",
        "🍫 Hot Chocolate",
        "🥤 Iced Drink"
    ]
)
# ----------------------------------
# READING CHALLENGE
# ----------------------------------

st.markdown("### 🎯 Reading Challenge")
books_read = st.slider(
    "Books read this year",
    0,
    50,
    5,
    key="reading_challenge"
)

st.progress(
    books_read / 50
)

st.write(
    f"📚 {books_read}/50 books completed"
)

# ----------------------------------
# CATEGORY
# ----------------------------------

category = st.selectbox(
    "Choose a Category",
    list(book_database.keys())
)

# ----------------------------------
# VIBE
# ----------------------------------

vibe = st.selectbox(
    "Choose a Vibe",
    list(book_database[category].keys())
)
# ----------------------------------
# SURPRISE ME
# ----------------------------------

if st.button("🎲 Surprise Me"):

    all_books = []

    for category in book_database:
        for vibe in book_database[category]:
            all_books.extend(
                book_database[category][vibe]
            )

    surprise_book = random.choice(all_books)

    st.success(
        f"✨ Surprise Pick: {surprise_book}"
    )
# ----------------------------------
# GENERATE RECOMMENDATIONS
# ----------------------------------

if st.button("✨ Find My Books"):

    st.session_state.recommendations = random.sample(
        book_database[category][vibe],
        min(3, len(book_database[category][vibe]))
    )

# ----------------------------------
# DISPLAY RECOMMENDATIONS
# ----------------------------------

    if st.session_state.recommendations:

        st.success("Here are your recommendations!")

        st.caption(
            f"Showing {len(st.session_state.recommendations)} recommendations"
        )

        for book in st.session_state.recommendations:

            st.markdown("---")

            col1, col2 = st.columns([1, 3])

            with col1:
                if book in book_covers:
                    st.image(book_covers[book], width=140)
                
            with col2:

                st.markdown(
                    f"### 📚 {book}"
                )

                if book in book_descriptions:
                    st.caption(book_descriptions[book])

                if st.button(
                    "❤️ Add to Favorites",
                    key=f"fav_{book}"
                ):
                    if book not in st.session_state.favorites:
                        st.session_state.favorites.append(book)

                    st.rerun()

    st.balloons()

# ----------------------------------
# FOOTER
# ----------------------------------

st.markdown("---")

st.markdown(
    "<center>Made with ❤️ by Yushi using Python & Streamlit</center>",
    unsafe_allow_html=True
)