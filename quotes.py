from flask import Flask ,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://wlwouypsgluzgv:562c3df644ab44047c1d5d48aae673467ed779d62a0c7c60a6928ec98ec73dbe@ec2-34-202-88-122.compute-1.amazonaws.com:5432/d87jj9rh84fi6o'
#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:anee2507@localhost/quotes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Favquotes(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))

@app.route('/')
def index():
	result = Favquotes.query.all()
	return render_template('index.html',result=result)


@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/quotes')
def quotes():
	return render_template('quotes.html')


@app.route('/process',methods = ['POST'])
def process():
	quote = request.form['quote']
	author = request.form['author']
	quotedata =Favquotes(author=author,quote=quote)
	db.session.add(quotedata)
	db.session.commit()
	
	return redirect(url_for('index'))

