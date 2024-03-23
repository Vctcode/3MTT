from flask import Flask
helloworld = Flask(__name__)
@helloworld.route("/")
def run():
	return "This is a python app running on my vagrant machine"

if __name__ == "__main__":
	helloworld.run(host="0.0.0.0", port=int("8000"), debug=True)
