# Safely open the file
file = open("hello.txt", "w")

try:
    file.write("Hello, World!")

except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

finally:
    # Make sure to close the file after using it
    file.close()
