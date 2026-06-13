import random

# -------------------------------
# BOOKSY - AI Book Matcher
# -------------------------------

book_database = {
    "fiction": {
        "cozy": [
            "The House in the Cerulean Sea by TJ Klune",
            "Legends & Lattes by Travis Baldree",
            "A Psalm for the Wild-Built by Becky Chambers",
            "Anne of Green Gables by L.M. Montgomery"
        ],

        "romance": [
            "The Love Hypothesis by Ali Hazelwood",
            "Better Than the Movies by Lynn Painter",
            "Book Lovers by Emily Henry",
            "The Spanish Love Deception by Elena Armas"
        ],

        "thrilling": [
            "The Silent Patient by Alex Michaelides",
            "Gone Girl by Gillian Flynn",
            "Behind Closed Doors by B.A. Paris",
            "The Girl on the Train by Paula Hawkins"
        ],

        "fantasy": [
            "Harry Potter and the Sorcerer's Stone by J.K. Rowling",
            "The Hobbit by J.R.R. Tolkien",
            "Fourth Wing by Rebecca Yarros",
            "Six of Crows by Leigh Bardugo"
        ],

        "sci-fi": [
            "Project Hail Mary by Andy Weir",
            "Dune by Frank Herbert",
            "The Martian by Andy Weir",
            "Ender's Game by Orson Scott Card"
        ]
    },

    "non-fiction": {
        "inspiring": [
            "Atomic Habits by James Clear",
            "The Alchemist by Paulo Coelho",
            "Shoe Dog by Phil Knight",
            "Ikigai by Héctor García"
        ],

        "self-help": [
            "Think Like a Monk by Jay Shetty",
            "The Mountain Is You by Brianna Wiest",
            "Deep Work by Cal Newport",
            "The Psychology of Money by Morgan Housel"
        ],

        "business": [
            "Zero to One by Peter Thiel",
            "The Lean Startup by Eric Ries",
            "Rich Dad Poor Dad by Robert Kiyosaki",
            "Good to Great by Jim Collins"
        ]
    }
}

# -------------------------------
# User Recommendation History
# -------------------------------

history = []


# -------------------------------
# Function to Recommend Books
# -------------------------------

def recommend_books():
    print("\n📚 BOOKSY - Your Personal AI Book Matcher")
    print("-" * 50)

    category = input(
        "Choose a category (Fiction / Non-Fiction): "
    ).lower().strip()

    if category not in book_database:
        print("❌ Invalid category selected.")
        return

    print("\nAvailable vibes:")

    for vibe in book_database[category]:
        print(f"• {vibe.title()}")

    user_vibe = input("\nEnter your vibe: ").lower().strip()

    if user_vibe not in book_database[category]:
        print("❌ Vibe not found.")
        return

    books = book_database[category][user_vibe]

    num_books = min(3, len(books))

    recommendations = random.sample(books, num_books)

    print("\n🔍 Scanning library...")
    print("\n✨ Your Booksy Recommendations:\n")

    for i, book in enumerate(recommendations, start=1):
        print(f"{i}. {book}")
        history.append(book)

    print("\nHappy Reading! 📖✨")


# -------------------------------
# Function to View History
# -------------------------------

def view_history():
    print("\n📜 Recommendation History")
    print("-" * 50)

    if not history:
        print("No recommendations yet.")
        return

    for i, book in enumerate(history, start=1):
        print(f"{i}. {book}")


# -------------------------------
# Main Menu
# -------------------------------

while True:

    print("\n" + "=" * 50)
    print("📚 WELCOME TO BOOKSY")
    print("=" * 50)

    print("""
1. Get Book Recommendations
2. View Recommendation History
3. Exit
""")

    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        recommend_books()

    elif choice == "2":
        view_history()

    elif choice == "3":
        print("\n👋 Thank you for using Booksy!")
        print("See you next time, book lover! ❤️📚")
        break

    else:
        print("❌ Invalid choice. Please select 1, 2, or 3.")
