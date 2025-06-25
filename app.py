from flask import Flask 
app = Flask(__name__)

@app.route('/')
def home():
	return "<h1>Hello from Flask!</h1><p> Simple web app with CI/CD</p>"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
