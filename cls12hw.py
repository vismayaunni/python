try:
    name = input("Enter your name: ")
    feedback = input("Enter your feedback: ")

    if name.strip() == "" or feedback.strip() == "":
        raise ValueError("Error: Name and feedback cannot be empty.")

    print(f"Thank you, {name}! Your feedback: \"{feedback}\" has been recorded.")

except ValueError as e:
    print(e)

finally:
    print("Feedback process completed.")
