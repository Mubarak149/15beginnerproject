quiz = [
    {
        "question": "What is the capital of Nigeria?",
        "options": ["A. Kaduna", "B. Lagos", "C. Abuja"],
        "answer": "C",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter"],
        "answer": "B",
    },
    {
        "question": "Who is the current President of the United States (2025)?",
        "options": ["A. Joe Biden", "B. Donald Trump", "C. Kamala Harris"],
        "answer": "B",
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Pacific Ocean", "C. Indian Ocean"],
        "answer": "B",
    },
    {
        "question": "Which programming language is known as the 'language of the web'?",
        "options": ["A. Python", "B. Java", "C. JavaScript"],
        "answer": "C",
    },
    {
        "question": "What is the chemical symbol for Gold?",
        "options": ["A. Go", "B. Au", "C. Ag"],
        "answer": "B",
    },
    {
        "question": "In which year did Nigeria gain independence?",
        "options": ["A. 1960", "B. 1957", "C. 1975"],
        "answer": "A",
    },
    {
        "question": "Which continent is the Sahara Desert located in?",
        "options": ["A. Africa", "B. Asia", "C. Australia"],
        "answer": "A",
    },
    {
        "question": "Who is known as the father of computers?",
        "options": ["A. Charles Babbage", "B. Alan Turing", "C. John von Neumann"],
        "answer": "A",
    },
    {
        "question": "What is the freezing point of water in Celsius?",
        "options": ["A. 0°C", "B. 100°C", "C. -10°C"],
        "answer": "A",
    },
]

score = 0
print("Welcome To the Quiz Game")

for i, q in enumerate(quiz):
    print(f"{i + 1} {q["question"]}")
    for option in q["options"]:
        print(option)
    ans = input("What is your answer: ").lower()
    if ans == q["answer"].lower():
        score += 1
        
print(f" {score} / {len(quiz)}")
        