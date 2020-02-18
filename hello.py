from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello! My name is Nick! <h1>HELLO</h1>"



if __name__ == "__main__":
    app.run()
