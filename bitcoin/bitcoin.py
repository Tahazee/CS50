import requests
import sys

try:
    if len(sys.argv)==1:
        print("Missing argument")
        sys.exit(1)
    elif len(sys.argv)==2:
                s=sys.argv[1]
                x=float(sys.argv[1])
                response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

                d=response.json()
                us=d["bpi"]["USD"]["rate_float"]
                s=sys.argv[1]
                amount=float(s)*float(us)
                print(f"${float(amount):,.4f}")

except requests.RequestException:
    print("error")
    sys.exit(1)
except ValueError:
      print("error")
      sys.exit(1)

