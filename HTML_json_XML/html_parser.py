from html.parser import HTMLParser
from typing import List, Optional, Tuple


class myHTMLParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        # return super().handle_starttag(tag, attrs)
        print('Start tag:', tag)
        for attr in attrs:
            print('attr:', attr)

    def handle_endtag(self, tag: str) -> None:
        # return super().handle_endtag(tag)
        print('End tag:', tag)

    def handle_comment(self, data: str) -> None:
        print("Comment:", data)

    def handle_data(self, data: str) -> None:
        print("Data:", data)

def main():
    parser = myHTMLParser() 

    html = '''
        <html>
            <head><title>Coder</title></head>
            <body>
                <h1> <!--Hi, I am a coder<!-->
                    test, test
                </h1>
            </body>
        </html>
    '''
    parser.feed(html)

    print('------------------')
    with open("sample_html.html", 'r') as htmlFile:
        s = ""
        for line in htmlFile:
            s += line
        parser.feed(s)


if __name__ == "__main__": 
    main()
