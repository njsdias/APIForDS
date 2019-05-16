from flask import Flask                         # import the require libraries
app = Flask(__name__)                           # start the Flask application calling any name

@app.route('/')                                 # when the webserver see this endpoint the flask get the request the def hello_world
def hello_world():
    return "Hello World!"

@app.route('/hithere')
def hi_there_everyone():
    return "I just hit /hithere"

@app.route('/bye')
def bye():
    # Prepare the resposnse for the request than came to /bye
    c = 2*534
    s = str(c)
#    c = 1/0                                   # it will give us a Internal Server Error. Run it with app.run(debug=True)
    return "bye"



if __name__=="__main__":
    app.run()
#   app.run(debug=True)

## To run this file type in the terminal
## export FLASK_APP=app.py
## Press Enter
## Write: flask run (and Press Enter)
## Crtl + Shift + C to copy the http address and past it in your browse to see the end result

## To see the response of each end point type in your browser
## http://127.0.0.1:5000/
## http://127.0.0.1:5000/hi_there
## http://127.0.0.1:5000/bye

## For Web Servers API we usually return JSON files

## for Web Applications always return pages (return index.html or return render_template("index.html"))
