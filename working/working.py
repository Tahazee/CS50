import re
import sys


def main():
    inp=input("Hours: ").strip()
    print(convert(inp))
def convert(s):
                   search = re.search(r"^(([0-9][0-2]* (AM|PM))|([0-9][0-2]*):[0-5][0-9] (AM|PM)) to (([0-9][0-2]* (AM|PM))|([0-9][0-2]*):[0-5][0-9] (AM|PM))", s)
                   if search:
                          start,end=search.group().strip().split('to')
                          if ":" in start and ":" in end:
                                strh, strm, am = re.search(r"([0-9][0-2]?):([0-5][0-9]) (AM|PM)", start).groups()
                                endh, endm, pm = re.search(r"([0-9][0-2]?):([0-5][0-9]) (AM|PM)", end).groups()

                          elif ":" in start and ":" not in end:
                                 strh, strm, am = re.search(r"([0-9][0-2]?):([0-5][0-9]) (AM|PM)", start).groups()
                                 endh, pm = re.search(r"([0-9][0-2]?) (AM|PM)", end).groups()
                                 endm="00"




                          elif ":" in end and ":" not in start:
                                 strh, am = re.search(r"([0-9][0-2]?) (AM|PM)", start).groups()
                                 endh, endm, pm = re.search(r"([0-9][0-2]?):([0-5][0-9]) (AM|PM)", end).groups()
                                 strm="00"



                          elif ":" not in start and ":" not in end:
                                  strh, am = re.search(r"([0-9][0-2]?) (AM|PM)", start).groups()
                                  endh, pm = re.search(r"([0-9][0-2]?) (AM|PM)", end).groups()
                                  strm=endm="00"


                          return output(am,pm,strh,strm,endh,endm)
                   else:
                          raise  ValueError

def output(am,pm,strh,strm,endh,endm):
            if am=="AM" and pm=="PM":
                if int(strh)==12:
                        strh="00"
                        newf=f"{int(strh):02}:{strm} to {int(endh)}:{endm}"
                elif int(endh)==12:
                        endh="12"
                        newf=f"{int(strh):02}:{strm} to {int(endh)+12}:{endm}"
                else:
                       newf=f"{int(strh):02}:{strm} to {int(endh)+12}:{endm}"


                return newf

            elif am=="PM" and pm=="AM":
                if int(strh)==12:
                        strh="12"
                        newf=f"{int(strh):02}:{strm} to {int(endh)+12}:{endm}"
                elif int(endh)==12:
                        endh="00"
                        newf=f"{int(strh):02}:{strm} to {int(endh)}:{endm}"
                else:
                       newf=f"{int(strh)+12}:{strm} to {int(endh):02}:{endm}"


                return newf



            elif am=="AM" and pm=="AM":
                if int(strh)==12:
                        strh="00"
                        newf=f"{int(strh):02}:{strm} to {int(endh)+12}:{endm}"
                elif int(endh)==12:
                        endh="00"
                        newf=f"{int(strh):02}:{strm} to {int(endh)}:{endm}"
                else:
                       newf=f"{int(strh):02}:{strm} to {int(endh)+12}:{endm}"
                return newf
            else:
                if int(strh)==12:
                        strh="12"
                        newf=f"{int(strh):02}:{strm} to {int(endh)+12}:{endm}"
                elif int(endh)==12:
                        endh="12"
                        newf=f"{int(strh):02}:{strm} to {int(endh)}:{endm}"
                else:
                       newf=f"{int(strh):02}:{strm} to {int(endh)+12}:{endm}"


                return newf







if __name__=="__main__":
        main()
