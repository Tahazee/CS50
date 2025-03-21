def main():
    x=input("Input:")
    y=shorten(x)
    print(y)





def shorten(word):
    nw=""
    for i in word:
        if i not in ["a","e","i","o","u",'A','E','I','O','U']:
           nw+=i
    return(nw)

if __name__ == "__main__":
    main()
