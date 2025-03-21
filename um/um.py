import sys
import re

def main():
    x=(input("Text: "))
    y=count(x)
    print(y)

def count(s):
   if s!="":
      search=re.findall(r"\bum\b",s.lower())
      return len(search)








if __name__ == "__main__":
    main()
