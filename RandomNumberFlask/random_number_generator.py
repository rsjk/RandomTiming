from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home'

@app.route('/RandomNumberGenerator')
def random_number_generator():
    num = random.randint(1, 1000001)
    return str(num)

if __name__ == '__main__':
    app.run()

