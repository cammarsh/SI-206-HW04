import random
def questions():
  return input("What is your question")
questions = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply haze try again", "Ask again later", "Better not tell you now", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
print(random.choice(questions))
while True:
  question = questions()
  if question == "quit":
    break
  elif "?" not in question:
    print("I'm sorry, I can only answer questions")