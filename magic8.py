import random

# Step 1: Declare name and question variables
name = "Joe"  # You can change this to any name you want
question = "Will I win the lottery?"  # You can change the question

# Step 2: Declare answer variable
answer = ""

# Step 4: Generate a random number
random_number = random.randint(1, 9)
# Uncomment the line below to see the generated random number
# print(random_number)

# Step 6: Control Flow
if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
else:
    answer = "Error"  # Just in case random number is out of range

# Step 9: Print name and question
if name:
    print(f"{name} asks: {question}")
else:
    print(f"Question: {question}")

# Step 10: Print Magic 8-Ball's answer
print(f"Magic 8-Ball's answer: {answer}")
