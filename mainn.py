import random  # This built-in module lets us pick items randomly

# 1. Our Database
book_database = {
    "cozy": [
        "The House in the Cerulean Sea by TJ Klune",
        "Legends & Lattes by Travis Baldree",
        "A Psalm for the Wild-Built by Becky Chambers"
    ],
    "thrilling": [
        "The Silent Patient by Alex Michaelides",
        "Gone Girl by Gillian Flynn",
        "Behind Closed Doors by B.A. Paris"
    ],
    "inspiring": [
        "Atomic Habits by James Clear",
        "The Alchemist by Paulo Coelho",
        "Shoe Dog by Phil Knight"
    ],
    "sci-fi": [
        "Project Hail Mary by Andy Weir",
        "Dune by Frank Herbert",
        "The Martian by Andy Weir"
    ]
}

print("Welcome to Booksy - Your Personal AI Book Matcher!")
print("-------------------------------------------------")
print("What kind of comfort vibe are you looking for today?")
print("Options: cozy, thrilling, inspiring, sci-fi")

user_choice = input("Enter your vibe: ").lower().strip()

print("\nScanning the library for a surprise match...")
print("-------------------------------------------------")

# 2. Updated Surprise Logic
if user_choice in book_database:
    # random.choice() automatically picks exactly ONE item from the selected list
    surprise_book = random.choice(book_database[user_choice])
    
    print(f"✨ Your Surprise Match for a '{user_choice}' vibe is:")
    print(f"👉 {surprise_book}")
else:
    print("❌ Vibe not found! Please try 'cozy', 'thrilling', 'inspiring', or 'sci-fi'.")

print("-------------------------------------------------")
print("Enjoy your read with Booksy!")
