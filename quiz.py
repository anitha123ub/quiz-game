import random
import time

def get_random_motivation():
    messages = [
        "You're on fire! 🔥",
        "Keep it up! 🚀",
        "Wow, you're crushing it! 🏆",
        "You got this! 💪",
        "Don't give up now! 👏"
    ]
    return random.choice(messages)

def get_random_incorrect():
    messages = [
        "Oof, better luck next time! 😬",
        "Uh-oh! Try again! 😅",
        "Not quite right! 😕",
        "Oops! Keep going! 👀",
        "Almost had it! 🤔"
    ]
    return random.choice(messages)

print("🎉Welcome to 'Learn with Esprit'🎉")

player = input("Do you want to play? ")

if player.lower().strip() != "yes":
    print("Oh, maybe next time! 👋")
    quit()
    
print("Ok let's play!🎮\n")
score = 0
lives = 3

questions = [
    ("How many days do we have in a week?", "seven"),
    ("In which direction does the sun rise?", "east"),
    ("Which is the fastest animal on land?", "cheetah"),
    ("Which is the largest ocean in the world?", "pacific ocean"),
    ("What is the capital of France?", "paris"),
    ("What is the chemical symbol for water?", "h2o"),
    ("Which planet is known as the Red Planet?", "mars"),
    ("Who wrote 'Romeo and Juliet'?", "shakespeare"),
    ("Which is the smallest country in the world?", "vatican city"),
    ("What is the hardest natural substance on Earth?", "diamond"),
    ("How many continents are there?", "seven"),
    ("What is the longest river in the world?", "nile"),
    ("Who was the first person to walk on the moon?", "neil armstrong"),
    ("What is the largest desert in the world?", "sahara"),
    ("Which language is the most spoken worldwide?", "mandarin"),
    ("What is the tallest mountain in the world?", "mount everest")
]

random.shuffle(questions)

def ask_question(question,answer):
    global score,lives
    try:
        print(f"\n⌛ You have 8 seconds to answer!")
        start_time = time.time()
        user_answer = input(question + " ").lower().strip()
        
        if time.time() - start_time > 8:
            print("⏰Time's up!")
            lives -= 1
            print(f"❗You lost a life. Lives remaining: {lives}")
            return
        
        if user_answer == answer:
            print(" ✅Correct! Great job!🎉")
            score +=1
            print(get_random_motivation())
        else:
            print(f"❌ {get_random_incorrect()} ")
            lives -= 1
            print(f"❗You lost a life. Lives remaining: {lives}")
    except Exception as e:
       print(f"An error occured : {e}")
       
for q,a in questions:
    if lives == 0:
        print("\n😔 You have run out of lives! Game over!")
        break
    ask_question(q, a)

if lives > 0:    
    if score == len(questions):
        print(f"\n🏆 Amazing! you got {score}/{len(questions)}! You're a quiz champion!🎉")
    elif score >= len(questions) // 2:
        print(f"\n👍 Good job! you got {score}/{len(questions)}! Keep practicing!")
    else:
        print(f"\n😄You got {score}/{len(questions)}!  Don't worry, try again next time!")
    
print(f"Your final score:  {score}😎" )
print(f"Remaining lives: {lives} 💖")
