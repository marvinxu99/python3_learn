# working with HTML data via the HTMLParser
from html.parser import HTMLParser


# define a class that will handle various parts of an HTML file
# create a subclass of HTMLParser and override the handler methods
class MyHTMLParser(HTMLParser):
    # TODO: handle an opening HTML tag of the form:
    # <tagname attr="value">
    def handle_starttag(self, tag, attrs):
        pass

    # TODO: function to handle the ending tag, which looks like:
    # </tagname>
    def handle_endtag(self, tag):
        pass

    # TODO: function to handle character and text data (tag contents)
    # <tag>this data here in the tag</tag>
    def handle_data(self, data):
        pass

    # TODO: function to handle the processing of HTML comments
    # <!-- which look like this -->
    def handle_comment(self, data):
        pass


# TODO: create an instance of the parser


# open the sample HTML file and read it
f = open("samplehtml.html")
if f.mode == "r":
    contents = f.read()  # read the entire file
    # TODO: pass the content to the parser


# TODO: Count the number of <meta> tags in the file
