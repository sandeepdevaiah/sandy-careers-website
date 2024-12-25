from flask import Flask

app = Flask(__name__) #creating an object of the class Flask


@app.route("/")
def hello_world():
  return "Hello, Man!! "

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)