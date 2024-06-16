import json

class Flashcard:
    def __init__(self, front, back):
        self.front = front
        self.back = back

class FlashcardTool:
    def __init__(self):
        self.flashcards = []

    def add_flashcard(self, front, back):
        flashcard = Flashcard(front, back)
        self.flashcards.append(flashcard)

    def save_flashcards(self, filename):
        data = [{'front': fc.front, 'back': fc.back} for fc in self.flashcards]
        with open(filename, 'w') as f:
            json.dump(data, f)
        print(f"Saved {len(self.flashcards)} flashcards to {filename}")

    def load_flashcards(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.flashcards = [Flashcard(fc['front'], fc['back']) for fc in data]
            print(f"Loaded {len(self.flashcards)} flashcards from {filename}")
        except FileNotFoundError:
            print(f"No file named {filename} found")

    def study_flashcards(self):
        import random
        random.shuffle(self.flashcards)
        for flashcard in self.flashcards:
            input(f"Front: {flashcard.front}\nPress Enter to see the back...")
            print(f"Back: {flashcard.back}\n")
            input("Press Enter to continue...")

def main():
    tool = FlashcardTool()
    while True:
        print("\nFlashcard Tool")
        print("1. Add a flashcard")
        print("2. Save flashcards")
        print("3. Load flashcards")
        print("4. Study flashcards")
        print("5. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            front = input("Enter the front of the flashcard: ")
            back = input("Enter the back of the flashcard: ")
            tool.add_flashcard(front, back)
        elif choice == '2':
            filename = input("Enter the filename to save to: ")
            tool.save_flashcards(filename)
        elif choice == '3':
            filename = input("Enter the filename to load from: ")
            tool.load_flashcards(filename)
        elif choice == '4':
            tool.study_flashcards()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()