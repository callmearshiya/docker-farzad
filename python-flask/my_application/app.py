from flask import Flask
from flask import request
import os


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/listfiles")
def listfiles():
    # Get files list in /uploads directory and store them into a list
    direc = os.listdir("./uploads")
    #Convert List to String
    dirs = str(direc)
    # Get rid of the symboles in String
    dirs = dirs.translate(None, "[]',")
    return dirs

@app.route("/euler1")
def euler1():
    # Calculate the sum of all the multiples of 3 or 5 below 1000
    total = sum ( num for num in xrange(1000) if not (num % 3 and num % 5) )
    return total

@app.route("/euler2")
def euler2():
    # Set the starter sum, firstand second number, and calculate next number in serie
    eventsum = 0
    fib1 = 1
    fib2 = 1
    nextnum = fib1 + fib2
    # Check if next number is less than 4000000. If so it sums up else it scapes and swap numbers
    while (nextnum < 4000000):
            if ( nextnum % 2 == 0 ):
                   eventsum = eventsum + nextnum
                   fib1 = fib2
                   fib2 = nextnum
                   nextnum = fib1 + fib2
            else:
                   fib1 = fib2
                   fib2 = nextnum
                   nextnum = fib1 + fib2

    return eventsum
          
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)