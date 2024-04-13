from flask import Flask
from os import environ
#from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://user:password@postgres/db'
#db = SQLAlchemy(app)


@app.route('/')
def home():
    return 'hello!'



#-------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=environ.get('PORT'),
            debug=environ.get('DEBUG'))