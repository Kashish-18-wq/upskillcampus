"""
Python Quiz Application
Name   : Kashish Baranwal
Domain : Python for Data Science
Course : Free Summer Internship in Python - 2026 (upskillCampus / IoT Academy / UCT)

Summary of work incorporated (Weeks 1-4):
  Week 1 - Variables, data types, operators, loops, functions; started Quiz Game
           (question creation, basic answer checking, score calculation)
  Week 2 - Conditional statements (if / if-else / if-elif-else) for answer validation
  Week 3 - NumPy and Pandas for analyzing and summarizing quiz scores
  Week 4 - Modular functions, case-insensitive & invalid-input handling,
           exception handling, cleaner and more maintainable code
"""

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Quiz data (list of dictionaries, each dict = one question)
# ---------------------------------------------------------------------------
QUIZ_QUESTIONS = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. def", "C. function", "D. define"],
        "answer": "B",
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["A. List", "B. Dictionary", "C. Tuple", "D. Set"],
        "answer": "C",
    },
    {
        "question": "What does the 'len()' function do?",
        "options": ["A. Returns type", "B. Returns length", "C. Returns index", "D. Returns value"],
        "answer": "B",
    },
    {
        "question": "Which library is primarily used for numerical arrays in Python?",
        "options": ["A. Pandas", "B. NumPy", "C. Matplotlib", "D. Flask"],
        "answer": "B",
    },
    {
        "question": "Which statement is used for decision making in Python?",
        "options": ["A. loop", "B. if-else", "C. try-except", "D. class"],
        "answer": "B",
    },
]


# ---------------------------------------------------------------------------
# Core functions (Week 1 & Week 4: functions, modular design)
# ---------------------------------------------------------------------------
def get_user_answer(prompt: str) -> str:
    """
    Get and validate a single-letter answer from the user.
    Week 4: input validation + exception handling for invalid input.
    """
    while True:
        try:
            user_input = input(prompt).strip().upper()
            if user_input in ("A", "B", "C", "D"):
                return user_input
            print("Invalid input. Please enter A, B, C, or D.")
        except (KeyboardInterrupt, EOFError):
            print("\nQuiz interrupted by user.")
            raise


def check_answer(user_answer: str, correct_answer: str) -> bool:
    """
    Week 2: conditional statements for answer validation.
    Week 4: case-insensitive comparison.
    """
    if user_answer.strip().upper() == correct_answer.strip().upper():
        return True
    else:
        return False


def run_quiz(questions: list) -> list:
    """
    Week 1: loops driving the quiz flow.
    Runs the quiz and returns a record of results for each question.
    """
    results = []
    score = 0

    print("=" * 55)
    print(" Welcome to the Python Quiz Application")
    print("=" * 55)

    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i}. {q['question']}")
        for option in q["options"]:
            print("   ", option)

        user_answer = get_user_answer("Your answer (A/B/C/D): ")
        is_correct = check_answer(user_answer, q["answer"])

        if is_correct:
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect. Correct answer: {q['answer']}")

        results.append({
            "question_no": i,
            "question": q["question"],
            "your_answer": user_answer,
            "correct_answer": q["answer"],
            "is_correct": is_correct,
        })

    print("\n" + "=" * 55)
    print(f" Quiz Finished! Your Score: {score}/{len(questions)}")
    print("=" * 55)

    return results


# ---------------------------------------------------------------------------
# Week 3: NumPy & Pandas for score analytics / reporting
# ---------------------------------------------------------------------------
def analyze_results(results: list) -> pd.DataFrame:
    """
    Converts quiz results into a Pandas DataFrame and prints
    summary statistics using Pandas/NumPy.
    """
    df = pd.DataFrame(results)

    total_questions = len(df)
    correct_count = int(df["is_correct"].sum())
    accuracy = np.round((correct_count / total_questions) * 100, 2)

    print("\n----- Quiz Result Summary (Pandas/NumPy) -----")
    print(df[["question_no", "your_answer", "correct_answer", "is_correct"]])
    print(f"\nTotal Questions : {total_questions}")
    print(f"Correct Answers : {correct_count}")
    print(f"Accuracy        : {accuracy}%")

    return df


def save_results(df: pd.DataFrame, filename: str = "quiz_results.csv") -> None:
    """Saves quiz results to a CSV file for record-keeping."""
    try:
        df.to_csv(filename, index=False)
        print(f"\nResults saved to '{filename}'")
    except Exception as e:
        print(f"Could not save results: {e}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main():
    try:
        results = run_quiz(QUIZ_QUESTIONS)
        df = analyze_results(results)
        save_results(df)
    except (KeyboardInterrupt, EOFError):
        print("Goodbye!")


if __name__ == "__main__":
    main()
