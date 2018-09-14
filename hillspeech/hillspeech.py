from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
app = Flask(__name__)
bootstrap.init_app(app)

# Index page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
	app.run(port=5000, debug=True)
