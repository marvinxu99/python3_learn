# working with HTML data via the HTMLParser
from html.parser import HTMLParser

metacount = 0


# define a class that will handle various parts of an HTML file
# create a subclass of HTMLParser and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global metacount
        if tag == "meta":
            metacount += 1

        print("Encountered a start tag:", tag)
        pos = self.getpos()  # returns a tuple indication line and character
        print("\tAt line: ", pos[0], " position ", pos[1])

        if len(attrs) > 0:
            print("\tAttributes:")
            for a in attrs:
                print("\t", a[0], "=", a[1])

    # function to handle the ending tag
    def handle_endtag(self, tag):
        print("Encountered an end tag:", tag)

    # function to handle character and text data (tag contents)
    def handle_data(self, data):
        if (data.isspace()):
            return
        print("Encountered some text data:", data)

    # function to handle the processing of HTML comments
    def handle_comment(self, data):
        print("Encountered comment:", data)


# create an instance of the parser
parser = MyHTMLParser()

# open the sample HTML file and read it
f = open("samplehtml.html")
if f.mode == "r":
    contents = f.read()  # read the entire file
    parser.feed(contents)

print(f"{metacount} meta tags encountered")
