from flask import Flask

app = Flask(__name__)

# GET /store
# GET /store/<string:name>
# POST /store data: {name:, items:}
# GET /store/<string:name>/items
# POST /store/<string:name>/item {name:, price:}

@app.route('/')
def home():
    return 'Home'


if __name__ == __name__:
    app.run(port=3000)
