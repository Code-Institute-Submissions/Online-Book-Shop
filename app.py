import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'heroku working and finally and have fun adn fun'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    	port=int(os.environ.get('PORT')),
    	debug=True)
