def run_chatbot():
    question = input("Enter command: ")

    if question == "What is your name?":
        print("My name is BoorpBazzle9000")
    elif question == "Who is your creator?":
        print("I was created by the great DJS")
    elif question == "What programming language are you written in?":
        print("The greatest of all programming languages, Python!")
    elif question == "Tell me a joke":
        print("Did you hear about the claustrophobic astronaut? He just needed a little space 😂 🤣 😂 🤣") 
    else:
        print("I don't understand that command, sorry...")


while True:
    user_choice = int(input("Do you want to (1) run the chatbot or (2) exit the program? "))
    if user_choice == 1:
        run_chatbot()
    elif user_choice == 2:
        print("Goodbye!")
        break
