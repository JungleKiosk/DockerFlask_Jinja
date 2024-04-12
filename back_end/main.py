from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('home/home.html')

@app.route('/items')
def get_items():
    return render_template('home/cosmos/items.html')

@app.route('/item')
def get_item():
    return render_template('home/cosmos/item.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)