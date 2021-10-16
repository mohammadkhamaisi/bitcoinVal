import requests
from flask import Flask


# This is the HTML Template for the web application
template = """<!DOCTYPE html>
<html>
<head>
<title>
Bitcoin
</title>
</head>
<body>
<h1>
<div class="container my-4">
          <div class="col-md-6 offset-md-4">
          <h1>Bitcoin Value Application</h1>
            <img src="https://cdn.pixabay.com/photo/2019/06/23/19/15/bitcoin-4294492_960_720.png" width="150" height="150">
</h1>
</div>
          <hr>
          <hr>

            <div class="col-md-12 offset-md-1">
            <h3 class="center">Real time price of Bitcoin is: $$replace_this1$$ $</h3>
            </div>
            <hr>
            <div class="col-md-12 offset-md-1">
            <h3 class="center">Average Price for the last 10 minutes is: $$replace_this2$$ $</h3>
            </div>
            <hr>
          <hr>
          <hr>
        </div>
</body>
</html>"""

app = Flask(__name__)

## the URL for the crypto currency API
URL = "https://min-api.cryptocompare.com/data/v2/histominute?fsym={}&tsym={}&limit={}"


# calculate 
def get_price(coin,currency,limit):
    sum = 0
    try:
        response = requests.get(URL.format(coin,currency,limit)).json()
        for i in range(10):
            sum += response['Data']['Data'][i]['close']
     #   data = {'price': response['Data']['Data'][9]['close'], 'average': sum/10}
        return response['Data']['Data'][9]['close'],sum/10
    except:
        return False


#currencyPrice = get_price("BTC","USD","10")
@app.route("/")
def hello_world():
    currentprice,average= get_price("BTC","USD","10")
    html_result = template.replace("$$replace_this1$$", str(currentprice))
    html_result = html_result.replace("$$replace_this2$$",str(average))
    return html_result

if __name__ == "__main__":
    app.run()
