from validator_collection import validators, checkers, errors
try:
    a=input("email: ")
    x=validators.email(a)
    print("Valid")
except ValueError:
    print("invalid")
