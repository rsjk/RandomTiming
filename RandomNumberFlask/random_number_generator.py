from flask import Flask
import random


app = Flask(__name__)


@app.route('/')
def random_number_generator():
    # generate a number between 1 and 1 million
    num = random.randint(1, 1000000)
    # must return a string
    return str(num)


if __name__ == '__main__':
    app.run()

