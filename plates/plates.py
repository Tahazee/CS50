def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    if s[0:2].isalpha() and 1<len(s)<7  and schar(s) and middle(s) and fnum(s) :
        return True
    else:
        return False
def middle(s):
    for i in s:
        if i.isdigit():
            for j in s[s.index(i)+1:]:
                if j.isalpha():
                    return False
    return True
def fnum(s):
    for i in s:
        if i.isdigit():
            if i=="0":
                return False
            else:
                return True
            break
    return True
def schar(s):
    if '.' not in s and ' ' not in s and '"' not in s:
        return True

if __name__ == "__main__":
    main()
