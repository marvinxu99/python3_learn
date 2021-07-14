# working with HTML data via the HTMLParser
from html.parser import HTMLParser
from os import pardir

metacount = 0

# define a class that will handle various parts of an HTML file
# create a subclass of HTMLParser and override the handler methods
class MyHTMLParser(HTMLParser):

    def __init__(self, *, convert_charrefs: bool) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.metacount = 0

    # TODO: handle an opening HTML tag of the form:
    # <tagname attr="value">
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
        pos = self.getpos()
        print('At line:', pos[0], ' and char:', pos[1])
        if len(attrs) > 0:
            print("\tAttributes")
            for a in attrs:
                print("\t\t", a[0], '=', a[1])
        if tag == 'meta':
            self.metacount += 1

    # TODO: function to handle the ending tag, which looks like:
    # </tagname>
    def handle_endtag(self, tag):
        print('Encountered an end tag:', tag)

    # TODO: function to handle character and text data (tag contents)
    # <tag>this data here in the tag</tag>
    def handle_data(self, data):
        if len(data.strip()): 
            print("Encountered some text:", data)

    # TODO: function to handle the processing of HTML comments
    # <!-- which look like this -->
    def handle_comment(self, data):
        if len(data.strip()):
            print("Encountered a comment:", data)


# TODO: create an instance of the parser
parser = MyHTMLParser(convert_charrefs=False)


# open the sample HTML file and read it
f = open("samplehtml.html")
if f.mode == "r":
    contents = f.read()  # read the entire file
    # TODO: pass the content to the parser
    parser.feed(contents)


# TODO: Count the number of <meta> tags in the file
print(f"{parser.metacount} meta tags found.")