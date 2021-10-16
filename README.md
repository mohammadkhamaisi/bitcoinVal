# Bitcoin Value Application
Bitcoin Value is an application that prints in a web page the current value of the bitcoin, and it average in last 10 minutes,we collect our data from API:

https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=10


## Running Bitcoin Value python file:
Bitcoin Value is a python application,you can run it manually on cmd using the following commands:

```
git clone https://github.com/mohammadkhamaisi/bitcoinVal.git
cd avgval
pip install -r requirements.txt
python main.py
```

we can see our output in this URL: http://127.0.0.1:5000/

## how to build our application image in docker:
use this commands:

```
$ git clone https://github.com/mohammadkhamaisi/bitcoinVal.git
$ docker build -t bitval  .
```
## Run application image on the container:
```
$ docker run -it -d -p 5000:5000 bitval 
```
the output will be here: http://localhost:5000

## how to push our Docker image in our dockerhub
```
$ docker tag hw-app mohammadkhamaisi/bitval
$ docker push mohammadkhamaisi/bitval
```
