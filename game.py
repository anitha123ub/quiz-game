import random
import time

print("🎉 Welcome to 'Learn with Esprit' 🎉")

player = input("Do you want to play? ")

if player.lower().strip() != "yes":
    print("Oh, maybe next time! 👋")
    quit()
    
print("Ok, let's play! 🎮")
score = 0

# List of questions and answers
questions = [
    ("How many days do we have in a week?", "seven"),
    ("In which direction does the sun rise?", "east"),
    ("Which is the fastest animal on the land?", "cheetah"),
    ("Which is the largest ocean in the world?", "pacific ocean")
]

# Randomize the order of questions
random.shuffle(questions)

# Function to ask a question with a time limit
def ask_question(question, answer):
    global score
    try:
        print(f"\n⏳ You have 5 seconds to answer!")
        start_time = time.time()
        user_answer = input(question + " ").lower().strip()
        
        # Check if the user took too long
        if time.time() - start_time > 5:
            print("⏰ Time's up!")
            return
        
        if user_answer == answer:
            print("✅ Correct! Great job! 🎉")
            score += 1
        else:
            print("❌ Incorrect! Better luck next time! 😅")
    except Exception as e:
        print(f"An error occurred: {e}")

# Loop through the questions
for q, a in questions:
    ask_question(q, a)

# Final message based on the score
if score == 4:
    print(f"\n🏆 Amazing! You got {score}/4! You're a quiz champion!")
elif score >= 2:
    print(f"\n👏 Good job! You got {score}/4! Keep practicing!")
else:
    print(f"\n😅 You got {score}/4! Don't worry, try again next time!")