# 
# Example file for parsing and processing HTML
#
from html.parser import HTMLParser
from typing import List, Tuple, Optional

metacount = 0

class MyHTMLParser(HTMLParser):
  # def handle_comment(self, data):
  def handle_comment(self, data: str) -> None:
    print("Encountered comment: ", data)
    pos = self.getpos()
    print("\t At line: ", pos[0], " position ", pos[1])
    return super().handle_comment(data)

  # def handle_starttag(self, tag, attrs) -> None:
  def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
    global metacount
    if tag == "meta":
      metacount += 1
    print("Encountered tag: ", tag)
    pos = self.getpos()
    print("\t At line: ", pos[0], " position ", pos[1])

    if attrs.__len__() > 0: 
      print("\tAttributes:")
      for a in attrs:
        print("\t", a[0], "=", a[1])

    return super().handle_starttag(tag, attrs)


  def handle_endtag(self, tag: str) -> None:
    print("Encountered tag: ", tag)
    pos = self.getpos()
    print("\tAt line: ", pos[0], " position ", pos[1])
    return super().handle_endtag(tag)


  def handle_data(self, data: str) -> None:
    if data.isspace(): 
      return
    print("Encountered data: ", data)
    pos = self.getpos()
    print("\t At line: ", pos[0], " position ", pos[1])
    return super().handle_data(data)


def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()
  with open('samplehtml.html') as f:
    contents = f.read()
    parser.feed(contents)
  
  print("Total meta tags found:", metacount)


if __name__ == "__main__":
  main();
  