import csv
import os
import traceback

print(f"1. Add flashcard\n2. Study flashcard\n3. View all flashcards\n4. Exit")

flashcards = {}

def add_card():
    question = input("Enter question: ")
    answer = input("Enter answer: ")
    return question, answer

while True:
    try:
        option = int(input("Enter option: "))

        match option:
            case 1:
                question, answer = add_card()
                file_exists = os.path.exists('flashcards.csv')

                with open('flashcards.csv', 'a', newline='') as file:
                    fieldnames = ["Question", "Answer"]
                    writer = csv.DictWriter(file, fieldnames=fieldnames)

                    if not file_exists:
                        writer.writeheader()

                    writer.writerow({
                        "Question" : question,
                        "Answer" : answer
                    })

            case 3:
                file_exists = os.path.exists('flashcards.csv')
                if not file_exists:
                    print("No cards to view")
                    continue
                with open('flashcards.csv', 'r') as file:
                    reader = csv.DictReader(file)

                    try:
                        for row in reader:
                            print(row)
                    
                    except Exception as e:
                        print(e, type(e))
                        traceback.print_exc()

            case 4:
                break
    
    except ValueError:
        print("Please enter an option!!")
        continue