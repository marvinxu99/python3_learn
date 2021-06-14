'''
The Element API:
- foucuses on being simplier and more efficient than DOM
- Elements are treated like lists
- Attributes are treated like dictionaries
- Search for content in XML is straight forward

- python -m pip install lxml

'''
import requests
from lxml import etree

def main():
    
    # retrieve the XML data structure using the requests library
    url = 'http://httpbin.org/xml'
    result = requests.get(url)

    # build a doc structure using the ElementTree API
    doc = etree.fromstring(result.content)
    #print(result.text)

    # access the value of an attribute
    print(doc.tag)
    print(doc.attrib['title'])

    # iterate over tags
    for elem in doc.findall('slide'):
        print(elem.tag)

    slideCount = len(doc.findall('slide'))
    print(f"There are { slideCount } slide elements")

    # create a mew slide
    newSlide = etree.SubElement(doc, 'slide')
    newSlide.text = "This is a new slide"

    # count the numner of slides
    slideCount = len(doc.findall('slide'))
    itemCount = len(doc.findall(".//item"))

    print(f'There are { slideCount } slide elements')
    print(f'There are { itemCount } item elements')


if __name__ == '__main__':
    main()