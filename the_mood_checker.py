happy = "It is great to see you happy!"
nervous = "Take a deep breath 3 times."
sad = "Cheer up."
excited = "Woooohoooo!"
relaxed = "Good for you!"


mood = input("What is your mood? ")

if mood == "happy":
    print(happy)
elif mood == "nervous":
    print(nervous)
elif mood == "sad":
    print(sad)
elif mood == "excited":
    print(excited)
elif mood == "relaxed":
    print(relaxed)
else:
    print("I don't recognize this mood")
