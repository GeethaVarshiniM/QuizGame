quiz_data = [
    {
        "question": "1. What does CPU stand for?",
        "options": ["a) Central Processing Unit", "b) Control Processing Unit", "c) Computer Personal Unit", "d) Central Process Unit"],
        "answer": "a"
    },
    {
        "question": "2. Which programming language is primarily used for Android development?",
        "options": ["a) Java", "b) Swift", "c) C++", "d) Python"],
        "answer": "a"
    },
    {
        "question": "3. What is the main component of a computers operating system?",
        "options": ["a) Compiler", "b) Kernel", "c) Motherboard", "d) Processor"],
        "answer": "b"
    },
    {
        "question": "4. HTML is used to create ____?",
        "options": ["a) Database", "b) Web Pages", "c) Applications", "d) Systems"],
        "answer": "b"
    },
    {
        "question": "5. Which of the following is not a programming language?",
        "options": ["a) Python", "b) JavaScript", "c) HTTP", "d) Ruby"],
        "answer": "c"
    },
    {
        "question": "6. What is the purpose of RAM in a computer?",
        "options": ["a) To store files", "b) To process data", "c) To temporarily hold data", "d) To manage graphics"],
        "answer": "c"
    },
    {
        "question": "7. Which company developed the Windows operating system?",
        "options": ["a) Apple", "b) Google", "c) Microsoft", "d) IBM"],
        "answer": "c"
    },
    {
        "question": "8. What does HTTP stand for?",
        "options": ["a) Hyper Text Transfer Protocol", "b) High Transfer Text Protocol", "c) Hyper Text Transport Protocol", "d) High Text Transfer Protocol"],
        "answer": "a"
    },
    {
        "question": "9. Which tool is used to manage version control in software development?",
        "options": ["a) Git", "b) JIRA", "c) Jenkins", "d) Docker"],
        "answer": "a"
    },
    {
        "question": "10. What does SQL stand for?",
        "options": ["a) Structured Question Language", "b) Strong Query Language", "c) Structured Query Language", "d) Strong Question Language"],
        "answer": "c"
    }
]

def run_quiz():
    score = 0
    print("Welcome to the Technical Quiz!")
    print("Answer the following questions by choosing the correct option (a, b, c, or d).\n")

    for item in quiz_data:
        print(item["question"])
        for option in item["options"]:
            print(option)
        
        # Validate input
        while True:
            answer = input("Your answer: ").strip().lower()
            if answer in ['a', 'b', 'c', 'd']:
                break
            else:
                print("Invalid choice. Please choose a, b, c, or d.")

        if answer == item["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {item['answer']}.\n")

    print(f"Quiz completed! Your final score is {score}/{len(quiz_data)}.")
    if score > 7:
        print("Great job! You have strong technical knowledge.")
    elif score > 4:
        print("Good effort! Keep learning.")
    else:
        print("Needs improvement. Study more to improve your technical knowledge.")

# Run the quiz
run_quiz()