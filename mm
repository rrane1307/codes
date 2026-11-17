def intelligent_agent():
    low = 1
    high = 100
    attempts = 0

    print("Think of a number between 1 and 100.")

    while low <= high:
        guess = (low + high) // 2
        attempts += 1

        print("My guess is:", guess)
        feedback = input("Enter higher, lower or correct: ").lower()

        if feedback == "higher":
            low = guess + 1
        elif feedback == "lower":
            high = guess - 1
        elif feedback == "correct":
            print("Number guessed successfully!")
            print("Attempts:", attempts)
            break
        else:
            print("Invalid input! Try again.")

    if low > high:
        print("Your feedback was incorrect!")


intelligent_agent()