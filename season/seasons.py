import datetime
import sys
import operator
import inflect

def main():
    dob=input("Enter date of birth:")
    checkformat(dob)
    print(convert(dob)+" minutes")

def checkformat(dob):
    try:
        if datetime.datetime.strptime(dob,"%Y-%m-%d").date():
            return True
    except ValueError:
        sys.exit('INVALID DATE')
def convert(dob):
    td=datetime.date.today()
    total_days=operator.sub(td, datetime.datetime.strptime(dob,"%Y-%m-%d").date()).days
    min=total_days*24*60
    return intowords(min)
def intowords(min):
    p=inflect.engine()
    word=p.number_to_words(min).capitalize()
    l=word.split(" and ")
    str=" ".join(l)
    return str


if __name__ == "__main__":
    main()
