from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home/home.html')

@app.route('/items')
def get_items():
    return render_template('home/cosmos/items.html')

@app.route('/item')
def get_item():
    return render_template('home/cosmos/item.html')

@app.route('/login')
def login():
    return render_template('home/user/login.html')

@app.route('/signup')
def signup():
    return render_template('home/user/signup.html')

#-------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)