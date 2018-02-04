
def questions():
    answer = raw_input("What is your question")
    return answer


while True:
    question = questions()
    if question == "quit":
        break
    elif "?" not in question:
        print("I'm sorry, I can only answer questions")
