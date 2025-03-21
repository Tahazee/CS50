months=[ "January","February","March", "April",  "May",   "June",  "July",
    "August", "September",  "October",
    "November","December"]
inp=input("Date:")
try:
      if "," in inp:
            x=inp.split()
            mo=x[0]
            da=int(x[1][:-1])
            ye=int(x[2])
            if da<32:
                for m in months:
                      if mo.lower()==m.lower():
                        print(f"{ye}-{months.index(m)+1:02}-{da:02}")
            else:
                input("Date: ")

      else:
          M,D,Y=inp.split("/")
          m,d,y=int(M),int(D),int(Y)

          if m<13 and d<32:
           print(f"{y}-{m:02}-{d:02}")

          else:
               input("Date:")


except ValueError:
     input("Date:")













