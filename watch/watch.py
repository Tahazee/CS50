

import re
import sys


def main():
    x=parse(input("HTML: "))
    print(x)




def parse(s):
    if re.search(r"<iframe(.)*></iframe>",s):
        search=re.search(r"https?://(www\.)?youtube\.com/embed/([a-z0-9-_]+)",s,re.IGNORECASE)
        if search:
            x=search.group(2)
            return "https://youtu.be/"+ x





if __name__ == "__main__":
    main()
