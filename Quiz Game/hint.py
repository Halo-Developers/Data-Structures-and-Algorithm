"""Quiz Game using Dictionary"""

"""
Stpes:
    1. Create a dictionary containing questions and answers
    2. Loop through diction
    3. 
"""

quiz = {
    1 : {
        "question" : "What is the highest mountain in Uganda",
        "answer" : "Rwenzori"
    },
    2 :{
        "question" : "Who owned the iron hammar in the Avengers",
        "answer" : "Thor"
    },
    3 :{
        "question" : "Who had a shield in Avengers movie",
        "answer" : "Captain America"
    }
}

for question in quiz:
    print(quiz[question]["question"])
    guess = input("Enter your guess: ")

    if guess == quiz[question]["answer"]:
        print("Correct")
    else:
        print("Wrong")
