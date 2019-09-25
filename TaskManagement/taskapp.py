from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taskapp.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(50))
    department = db.Column(db.String(200))
    password = db.Column(db.String(10))
    roles = db.Column(db.String(10))

    def __init__(self, username, email, department, password,roles):
        self.username = username
        self.email = email
        self.department = department
        self.password = password
        self.roles = roles

class task(db.Model):
    taskid=db.Column(db.Integer, primary_key=True)
    towhom=db.Column(db.String(100))
    date=db.Column(db.String(30))
    status=db.Column(db.String(20))
    taskmsg=db.Column(db.String(100))
    roles = db.Column(db.String(10))
    def __init__(self,towhom,date,status,taskmsg,roles):
        self.towhom = towhom
        self.date = date
        self.status = status
        self.taskmsg = taskmsg
        self.roles = roles


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['email'] or not request.form['department'] or not request.form['password']:
            flash('Please enter all the fields', 'error')
        else:
            user1 = users(username=request.form['username'], email=request.form['email'],
                               department=request.form['department'], password=request.form['password'],roles=request.form['roles'])

            db.session.add(user1)
            db.session.commit()
            flash('User was succesfully registered...!')
            return redirect(url_for('userLogin'))
    return render_template('new.html')

@app.route('/userLogin')
def userLogin():
	return render_template('login.html')


@app.route('/dosuperlogin',methods=['POST'])
def superlogin():
    if not request.form['username'] or not request.form['password']:
        flash('Please enter all the credentials ','error')
    else:
        usersall=users.query.filter_by(username=request.form['username'])
        for user in usersall:
            if request.form['password'] == user.password:
                if request.form['roles'] == 'Superuser':
                    return render_template('superuser.html')
                if request.form['roles'] == 'Manager':
                    return render_template('manager.html')
                if request.form['roles'] == 'Employee':
                    return render_template('manager.html')
            else:
                flash('ERROR')
                return render_template('home.html')

@app.route('/assigntasks',methods=['POST'])
def assigntasks():
    if request.method == 'POST':
        return render_template('superuser.html')
    else:
        if not request.form['towhom'] or not request.form['date'] :
            flash('Please enter all the fields', 'error')
        else:
            task1 = task(towhom=request.form['towhom'], date=request.form['date'],
                               taskmsg=request.form['taskmsg'], status=request.form['status'],roles=request.form['roles'])

            db.session.add(task1)
            db.session.commit()

            flash('task is added succesfully')
            return redirect(url_for('superlogin'))







if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)