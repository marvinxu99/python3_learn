'''
XML parsing models:
- SAX - Simple API for XML
- DOM: Document Object Model
'''

'''
SAX Parsing Model
- Read entire document start to finish, sequentially
- Generates events as XML content is encountered
- Your app defines a class to handle content events

'''
import requests
import xml.sax

# Defind the ContentHandler subclass for our content
class MyContentHandler(xml.sax.ContentHandler):
    def __init__(self) -> None:
        super().__init__()
        self.slideCount = 0
        self.itemCount = 0
        self.isInTitle = False

    # Handle startElement
    def startElement(self, name, attrs):
        if name == "slideshow":
            print("Slideshow title: " + attrs['title'])
        elif name == "slide":
            self.slideCount += 1
        elif name == "item":
            self.itemCount += 1
        elif name == "title":
            self.isInTitle = True
        #return super().startElement(name, attrs)

    # handle endElement
    def endElement(self, name):
        if name == "title":
            self.isInTitle = False    
        #return super().endElement(name)

    # handle text data
    def characters(self, content):
        if self.isInTitle:
            print("Title: " + content)
        #return super().characters(content)

    # handle startDocument
    def startDocument(self):
        print("About to start document!")
        #return super().startDocument()

    # handle endDocument
    def endDocument(self):
        print("Finishing up document")
        #return super().endDocument()

def main():
    # Create a new content handler for SAX parser
    handler = MyContentHandler()

    # use Requests lib to get XML data from the server
    # remember that Requests auto-decodes our content
    url = "http://httpbin.org/xml"
    result = requests.get(url)
    # print(result.text)

    # Call the parseString method on the XML text content received
    xml.sax.parseString(result.text, handler)

    # when we are done, prin out some interesting results
    print(f"There are { handler.slideCount } slide elements")
    print(f"There are { handler.itemCount } item elements")


if __name__ == "__main__":
    main()