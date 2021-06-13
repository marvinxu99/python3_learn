from redirectedstdout import RedirectedStdout

with open("hello2.txt", "w") as file:
    with RedirectedStdout(file):
        print("Hello, World!")

print("Back to the standard output...")
