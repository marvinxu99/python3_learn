'''
With the DOM API, you can:
- access any part of an XML structure at random
- Modify the XML content
- Represents the XML as a hierarchical tree structure

xml.dom.minidom is a lightweight implementation

domtree = xml.dom.mindom.parseString(str)

elem.getElementById(id)
elemt.getELementByTagName(tagname)

elem.getAttribute(attrName)
elem.setAttribute(atteName, val)

newELem = document.createElement(tagName)
newElem = document.createTextNode(strOfText)
elem.appendChild(newELem)

'''
import requests
import xml.dom.minidom


def main():
    # use Requests lib to get XML data from the server
    # remember that Requests auto-decodes our content
    url = "http://httpbin.org/xml"
    result = requests.get(url)
    # print(result.text)

    # parse the returned content into a DOM structure
    domtree = xml.dom.minidom.parseString(result.text)
    rootnode = domtree.documentElement

    # when we are done, prin out some interesting results
    print(f"The root elemt is { rootnode.nodeName }")
    print("Title: {0}".format(rootnode.getAttribute('title')))

    items = domtree.getElementsByTagName('item')
    print(f'There are { items.length } item tags')

    # manipulate the XML content in memorycls
    # Create a new item tag
    newItem = domtree.createElement('item')

    # Add some text to the item
    newItem.appendChild(domtree.createTextNode('this is some text'))

    # add the item to the first slide
    firstSlide = domtree.getElementsByTagName('slide')[0]
    firstSlide.appendChild(newItem)

    # Now count the item tags again
    items = domtree.getElementsByTagName('item')
    print(f'There are { items.length } item tags')

if __name__ == "__main__":
    main()