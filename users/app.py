from flask import Flask

app = Flask(__name__)


@app.get('/users')
def get_users():
    return [
        {
            'name': 'Alice',
            'id': 1,
        },
        {
            'name': 'Bob',
            'id': 2,
        },
    ]
