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

@app.route("/Euler1")
          def euler1():
          total( num for num in xrange(1000) if not (num % 3 and num % 5) )
          return total

@app.route("/Euler2")
        def euler2():
        
    def fib():
        a,b = 0,1
        while True:
            yield a
            a,b = b, a+b

    def even(seq):
        for number in seq:
            if not number % 2:
                yield number

    def under_a_million(seq):
        for number in seq:
            if number > 1000000:
                break
            yield number   

    return sum(even(under_a_million(fib())))
          
  
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)