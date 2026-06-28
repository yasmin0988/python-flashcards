import csv
import os
import traceback
from random import shuffle

print(f"1. Add flashcard\n2. Study flashcards\n3. View all flashcards\n4. Delete a flashcard\n5. Exit")

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

            case 2:
                file_exists = os.path.exists('flashcards.csv')
                if not file_exists:
                        print("No cards to study")
                        continue
                
                with open('flashcards.csv', 'r', newline='') as file:
                    reader = csv.DictReader(file)

                    try:
                        score = 0
                        total = 0
                        report = {}
                        cards = list(reader)
                        shuffle(cards)
                        item = 0

                        for item in cards:
                            print(item["Question"])
                            answer = input("What's the answer? ") 

                            if answer.strip().lower() == item['Answer'].strip().lower():
                                print("Correct")
                                score += 1
                                total += 1
                                report[f"Question {total}"] = "Correct"

                            else:
                                print("Incorrect")
                                total += 1
                                report[f"Question {total}"] = "Incorrect"

                        for i in range(len(report)):
                            print(f"\n\nQuestion {i+1}: {report[f"Question {i+1}"]}")
                        print(f"\nScore: {score}/{total}")
                        
                    except Exception as e:
                        print(e, type(e))
                        traceback.print_exc()

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
                file_exists = os.path.exists('flashcards.csv')
                if not file_exists:
                    print("No cards available")
                    continue
                with open('flashcards.csv', 'r') as file:
                    reader = csv.DictReader(file)

                    try:
                        cards = list(reader)
                        i = 0
                        for card in cards:
                            print(f"{i+1}. {card}")
                            i +=1

                        choice = int(input("Which card to delete?"))
                        cards.remove(cards[choice-1])
                        
                        with open('flashcards.csv', 'w') as file:
                            fieldnames = ["Question", "Answer"]
                            writer = csv.DictWriter(file, fieldnames=fieldnames)

                            writer.writeheader()
                            for card in cards:
                                writer.writerow(card)

                        print("Done")

                    except Exception as e:
                        print(e, type(e))
                        traceback.print_exc()

            case 5:
                break
    
    except ValueError:
        print("Please enter an option!!")
        continue