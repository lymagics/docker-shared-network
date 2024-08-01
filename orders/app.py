from flask import Flask

app = Flask(__name__)


@app.get('/orders')
def get_orders():
    return [
        {
            'product': 'Apple',
            'qty': 10,
        },
        {
            'product': 'Tomato',
            'qty': 5,
        },
    ]
