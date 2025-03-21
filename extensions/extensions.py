x=input("Enter file name").lower().strip().rpartition(".")
match x[2]:
    case"gif":
        print("image/gif")
    case"jpg"|"jpeg":
        print("image/jpeg")
    case"png":
        print("image/png")
    case"txt":
        print("text/plain")
    case"zip":
        print("application/zip")
    case"pdf":
        print("application/pdf")
    case _:
        print("application/octet-stream")


