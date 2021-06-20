#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  f = open("textfile.txt", "w+")
  for i in range(10):
    f.write("This is line " + str(i) + "\n")
  f.close()

  # Open the file for appending text to the end
  f = open("textfile.txt", "a")
  for i in range(10):
    f.write("This is line " + str(i) + "\n")
  f.close()
 
  # Open the file back up and read the contents
  f = open("textfile.txt", "r")
  if f.mode == 'r':
    # content = f.read()
    # print(content)
    fl = f.readlines()
    for x in fl:
      print(x)

    
if __name__ == "__main__":
  main()
