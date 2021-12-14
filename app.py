from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def hello():
  return "Hello world"

@app.route("/sham")
def yash():
  return render_template("index.html")
if __name__=="__main__":
  app.run(debug=True)
