def generate_evaluate_chain(inputs):
    # You can write your logic here (example for now)
    quiz = [
        {"question": "What is AI?", "options": ["A", "B", "C", "D"], "answer": "A"},
        {"question": "What is ML?", "options": ["A", "B", "C", "D"], "answer": "B"}
    ]
    return {
        "quiz": quiz,
        "review": "This is a test review."
    }
