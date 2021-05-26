from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.secret_key = "Cairocoders-Ednalan"
  
   
# MySQL configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/swift' #'mysql://admin:swift123@mydb.cluster-cbtkdcjv3hxt.us-east-1.rds.amazonaws.com/jtrbSheet1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
 
@app.route('/')
@app.route('/index')
def Index():

    data = Data.query.all()

    return render_template('index.html', employee = data)

 
@app.route('/insert', methods=['POST', 'GET'])
def insert():
    if request.method == 'POST' or request.method == 'GET':

        cusSeg = request.form['cusSeg']
        rmId = request.form['rmId']
        cif = request.form['cif']
        accNum = request.form['accNum']
        name = request.form['name']
        minFeeOTT = request.form['minFeeOTT']
        comPegOTT = request.form['comPegOTT']
        cableFee = request.form['cableFee']
        minFeeITT = request.form['minFeeITT']
        comPegITT = request.form['comPegITT']
        maxFeeITT = request.form['maxFeeITT']
        minDomes = request.form['minDomes']
        comPegTrasfer = request.form['comPegTrasfer']


        my_data = Data(cusSeg, rmId, cif, accNum, name, minFeeOTT, comPegOTT, cableFee, minFeeITT, comPegITT, maxFeeITT, minDomes, comPegTrasfer)
        db.session.add(my_data)
        db.session.commit()
        flash("Employee Inserted Successfully")
        return redirect(url_for('Index'))


 
@app.route('/edit/<accNum>', methods = ['POST', 'GET'])
def get_employee(accNum):

    data = Data.query.filter(Data.accNum == accNum).first()
    return render_template('edit.html', data = data)
 
@app.route('/update/<accNum>', methods=['POST'])
def update_customer(accNum):
    if request.method == 'POST':
        my_data = Data.query.filter(Data.accNum == accNum).first()

        my_data.cusSeg = request.form['cusSeg']
        my_data.rmId = request.form['rmId']
        my_data.cif = request.form['cif']
        my_data.accNum = request.form['accNum']
        my_data.name = request.form['name']
        my_data.minFeeOTT = request.form['minFeeOTT']
        my_data.comPegOTT = request.form['comPegOTT']
        my_data.cableFee = request.form['cableFee']
        my_data.minITT = request.form['minITT']
        my_data.comPegITT = request.form['comPegITT']
        my_data.maxITT = request.form['maxITT']
        my_data.minDomes = request.form['minDomes']
        my_data.comPegTrasfer = request.form['comPegTrasfer']

        db.session.commit()
        flash("Employee Updated Successfully")

        return redirect(url_for('Index'))
 
@app.route('/delete/<accNum>', methods = ['POST','GET'])
def delete_customer(accNum):
    my_data = Data.query.get(accNum)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")

    return redirect(url_for('Index'))



#Creating model table for our CRUD database
class Data(db.Model):
    '''id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))'''

    cusSeg = db.Column(db.String(100))
    rmId = db.Column(db.String(100))
    cif = db.Column(db.String(100))
    accNum = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    minFeeOTT = db.Column(db.Float)
    comPegOTT = db.Column(db.Float)
    cableFee = db.Column(db.Float)
    minFeeITT = db.Column(db.Float)
    comPegITT = db.Column(db.Float)
    maxFeeITT = db.Column(db.Float)  
    minDomes = db.Column(db.Integer)
    comPegTrasfer = db.Column(db.Float)

    def __init__(self, cusSeg, rmId, cif, accNum, name, minFeeOTT, comPegOTT, cableFee, minFeeITT, comPegITT, maxFeeITT, minDomes, comPegTrasfer):
    #def __init__(self, name, email, phone):

        '''self.name = name
        self.email = email
        self.phone = phone'''

        self.cusSeg = cusSeg
        self.rmId = rmId
        self.cif = cif
        self.accNum = accNum
        self.name = name
        self.minFeeOTT = minFeeOTT
        self.comPegOTT = comPegOTT
        self.cableFee = cableFee
        self.minFeeITT = minFeeITT
        self.comPegITT = comPegITT
        self.maxFeeITT = maxFeeITT
        self.minDomes = minDomes
        self.comPegTrasfer = comPegTrasfer


 
# starting the app
if __name__ == "__main__":
    app.run(debug=True)
