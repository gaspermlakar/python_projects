happy_response = "It is great to see you happy!"
nervous_response = "Take a deep breath 3 times."
sad_response = "Cheer up."
excited_response = "Woooohoooo!"
relaxed_response = "Good for you!"


mood = input("What is your mood? ")

if mood == "happy":
    print(happy_response)
elif mood == "nervous":
    print(nervous_response)
elif mood == "sad":
    print(sad_response)
elif mood == "excited":
    print(excited_response)
elif mood == "relaxed":
    print(relaxed_response)
else:
    print("I don't recognize this mood")
