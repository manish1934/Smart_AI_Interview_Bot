import random
import re
from question import question_bank

def is_garbage(text):
    # detect random keyboard spam
    garbage_patterns = [
        r"(asdf|qwer|zxcv|lkjh|hjkl)",
        r"(.)\1\1",   # aaa, jjj
    ]
    
    for pattern in garbage_patterns:
        if re.search(pattern, text):
            return True

    # too short random text
    if len(text.strip()) < 4:
        return True

    return False


def start_interview():
    print("\n===== AI MOCK INTERVIEW SYSTEM =====\n")

    name = input("Enter your name: ")
    print(f"\nWelcome {name} 🚀\n")

    fields = list(question_bank.keys())

    print("Available Fields:\n")
    for index, field in enumerate(fields, start=1):
        print(f"{index}. {field}")

    while True:
        try:
            choice = int(input("\nSelect your field (Enter number): "))
            if 1 <= choice <= len(fields):
                selected_field = fields[choice - 1]
                break
            else:
                print("Invalid number. Try again.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"\nYou selected: {selected_field}\n")

    field_questions = question_bank[selected_field]
    selected_questions = random.sample(field_questions, 7)

    print("===== Interview Started =====\n")

    score = 0
    total_marks = 14

    for i, q in enumerate(selected_questions, start=1):
        print(f"Q{i}: {q['question']}")
        user_answer = input("Your Answer: ").lower()
        correct_answer = q['answer'].lower()

        question_score = 0

        # Keyword check
        if any(word in user_answer for word in correct_answer.split()):
            question_score += 2
            print("✅ Keyword matched (+2)")
        else:
            print("❌ No proper keyword match")

        # Garbage detection
        if is_garbage(user_answer):
            question_score -= 1
            print("⚠ Garbage / Illogical content detected (-1)")

        # Avoid negative per question
        if question_score < 0:
            question_score = 0

        score += question_score

        print(f"Correct Answer: {q['answer']}")
        print(f"Marks for this question: {question_score}")
        print("-" * 50)

    print("\n===== FINAL RESULT =====")
    print(f"Candidate: {name}")
    print(f"Field: {selected_field}")
    print(f"Score: {score} / {total_marks}")

    if score >= 8:
        print("\n🎉 STATUS: PASS")
        print("Good Job! You passed the interview 💪")
        print(f"Welcome to our field: {selected_field} 🚀🔥")
    else:
        print("\n❌ STATUS: FAIL")
        print("Better luck for next time 😅 Practice more!")

if __name__ == "__main__":
    start_interview()