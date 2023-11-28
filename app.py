from flask import Flask,render_template,request
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/subid',methods=["GET","POST"])
def id_teachers():
    if request.method=='POST':
        i=0
        try:
            client = MongoClient()
            uri = "mongodb+srv://madhan22012003:ncMG56zKqFRU69AL@teachermanagement.njy5gmr.mongodb.net/?retryWrites=true&w=majority"
            client = MongoClient(uri, server_api=ServerApi('1'))
            db = client.TeacherDatabase          
            i = list(db.TeachersData.find({'ID':request.form['teacherId']}))
            x=list()
            for j in i:
                del j['_id']
                x.append(j)
            if len(i)==0:
                return render_template('error.html')
            return render_template('show.html',i=x)
        except Exception as e:
            print(e)
            return render_template('show.html',i=x)
    return render_template('addteacher.html')
@app.route('/subname',methods=["GET","POST"])
def numteachers():
    if request.method=='POST':
        i=0
        try:
            client = MongoClient()
            uri = "mongodb+srv://madhan22012003:ncMG56zKqFRU69AL@teachermanagement.njy5gmr.mongodb.net/?retryWrites=true&w=majority"
            client = MongoClient(uri, server_api=ServerApi('1'))
            db = client.TeacherDatabase           
            i = list(db.TeachersData.find({'Name':request.form['teacherName']}))
            x=list()
            for j in i:
                del j['_id']
                x.append(j)
            if len(i)==0:
                return render_template('error.html')
            return render_template('show.html',i=x)
        except Exception as e:
            print(e)
            return render_template('show.html',i=x)
    return render_template('addteacher.html')
@app.route('/subgender',methods=["GET","POST"])
def gd_teachers():
    if request.method=='POST':
        i=0
        try:
            client = MongoClient()
            uri = "mongodb+srv://madhan22012003:ncMG56zKqFRU69AL@teachermanagement.njy5gmr.mongodb.net/?retryWrites=true&w=majority"
            client = MongoClient(uri, server_api=ServerApi('1'))
            db = client.TeacherDatabase
            i = list(db.TeachersData.find({'Gender':request.form['teacherGender']}))
            x=list()
            for j in i:
                del j['_id']
                x.append(j)
            if len(i)==0:
                return render_template('error.html')
            return render_template('show.html',i=x)
        except Exception as e:
            print(e)
            return render_template('show.html',i=x)
    return render_template('addteacher.html')
@app.route('/update',methods=["GET","POST"])
def update_teachers():
    if request.method=='POST':
        i=0
        try:
            client = MongoClient()
            uri = "mongodb+srv://madhan22012003:ncMG56zKqFRU69AL@teachermanagement.njy5gmr.mongodb.net/?retryWrites=true&w=majority"
            client = MongoClient(uri, server_api=ServerApi('1'))
            db = client.TeacherDatabase
            db.TeachersData.update_one({'ID':request.form['teacherId']},{'$set':{request.form['columnName']:request.form['value']}})
            i = list(db.TeachersData.find({}))
            x=list()
            for j in i:
                del j['_id']
                x.append(j)
            if len(i)==0:
                return render_template('error.html')
            return render_template('show.html',i=x)
        except Exception as e:
            print(e)
            return render_template('show.html',i=x)
    return render_template('addteacher.html')
@app.route('/updateteacher')
def updateTeachers():
    return render_template("updateTeacher.html")
@app.route('/subdob',methods=["GET","POST"])
def dob_teachers():
    if request.method=='POST':
        i=0
        try:
            client = MongoClient()
            uri = "mongodb+srv://madhan22012003:ncMG56zKqFRU69AL@teachermanagement.njy5gmr.mongodb.net/?retryWrites=true&w=majority"
            client = MongoClient(uri, server_api=ServerApi('1'))
            db = client.TeacherDatabase
            i = list(db.TeachersData.find({'Date of Birth':request.form['teacherDOB']}))
            x=list()
            for j in i:
                del j['_id']
                x.append(j)
            if len(i)==0:
                return render_template('error.html')
            return render_template('show.html',i=x)
        except Exception as e:
            print(e)
            return render_template('show.html',i=x)
    return render_template('addteacher.html')
@app.route('/submobile',methods=["GET","POST"])
def mob_teachers():
    if request.method=='POST':
        i=0
        try:
            client = MongoClient()
            uri = "mongodb+srv://madhan22012003:ncMG56zKqFRU69AL@teachermanagement.njy5gmr.mongodb.net/?retryWrites=true&w=majority"
            client = MongoClient(uri, server_api=ServerApi('1'))
            db = client.TeacherDatabase           
            i = list(db.TeachersData.find({'Mobile Number':request.form['teacherMobile']}))
            x=list()
            for j in i:
                del j['_id']
                x.append(j)
            if len(i)==0:
                return render_template('error.html')
            return render_template('show.html',i=x)
        except Exception as e:
            print(e)
            return render_template('show.html',i=x)
    return render_template('addteacher.html')
@app.route('/subsub',methods=["GET","POST"])
def Subb_teachers():
    if request.method=='POST':
        i=0
        try:
            client = MongoClient()
            uri = "mongodb+srv://madhan22012003:ncMG56zKqFRU69AL@teachermanagement.njy5gmr.mongodb.net/?retryWrites=true&w=majority"
            client = MongoClient(uri, server_api=ServerApi('1'))
            db = client.TeacherDatabase           
            i = list(db.TeachersData.find({'Subject':request.form['teacherSubject']}))
            x=list()
            for j in i:
                del j['_id']
                x.append(j)
            if len(i)==0:
                return render_template('error.html')
            return render_template('show.html',i=x)
        except Exception as e:
            print(e)
            return render_template('show.html',i=x)
    return render_template('addteacher.html')
@app.route('/subexp',methods=["GET","POST"])
def exp_teachers():
    if request.method=='POST':
        i=0
        try:
            client = MongoClient()
            uri = "mongodb+srv://madhan22012003:ncMG56zKqFRU69AL@teachermanagement.njy5gmr.mongodb.net/?retryWrites=true&w=majority"
            client = MongoClient(uri, server_api=ServerApi('1'))
            db = client.TeacherDatabase           
            i = list(db.TeachersData.find({'Year of Experience':request.form['teacherExperience']}))
            x=list()
            for j in i:
                del j['_id']
                x.append(j)
            if len(i)==0:
                return render_template('error.html')
            return render_template('show.html',i=x)
        except Exception as e:
            print(e)
            return render_template('show.html',i=x)
    return render_template('addteacher.html')
@app.route('/subcls',methods=["GET","POST"])
def cls_teachers():
    if request.method=='POST':
        i=0
        try:
            client = MongoClient()
            uri = "mongodb+srv://madhan22012003:ncMG56zKqFRU69AL@teachermanagement.njy5gmr.mongodb.net/?retryWrites=true&w=majority"
            client = MongoClient(uri, server_api=ServerApi('1'))
            db = client.TeacherDatabase           
            i = list(db.TeachersData.find({'Number of Classes':request.form['teacherClasses']}))
            x=list()
            for j in i:
                del j['_id']
                x.append(j)
            if len(i)==0:
                return render_template('error.html')
            return render_template('show.html',i=x)
        except Exception as e:
            print(e)
            return render_template('show.html',i=x)
    return render_template('addteacher.html')
@app.route('/subsal',methods=["GET","POST"])
def sal_teachers():
    if request.method=='POST':
        i=0
        try:
            client = MongoClient()
            uri = "mongodb+srv://madhan22012003:ncMG56zKqFRU69AL@teachermanagement.njy5gmr.mongodb.net/?retryWrites=true&w=majority"
            client = MongoClient(uri, server_api=ServerApi('1'))
            db = client.TeacherDatabase

            
            i = list(db.TeachersData.find({'salary':request.form['teacherSalary']}))
            x=list()
            for j in i:
                del j['_id']
                x.append(j)
            if len(i)==0:
                return render_template('error.html')
            return render_template('show.html',i=x)
        except Exception as e:
            print(e)
            return render_template('show.html',i=x)
    return render_template('addteacher.html')

@app.route('/delTeacher')
def del_teachers():
    
    return render_template('delteacher.html')
@app.route('/addTeacher')
def add_teachers():
    
    return render_template('addteacher.html')
@app.route('/filterRecord')
def filter_teachers():
    
    return render_template('filterteacher.html')
@app.route('/searchTeacher')
def search_teachers():
    
    return render_template('searchteacher.html')
@app.route('/subm',methods=["GET","POST"])
def addition_teachers():
    if request.method=='POST':
        i=0
        try:
            client = MongoClient()
            uri = "mongodb+srv://madhan22012003:ncMG56zKqFRU69AL@teachermanagement.njy5gmr.mongodb.net/?retryWrites=true&w=majority"
            client = MongoClient(uri, server_api=ServerApi('1'))
            db = client.TeacherDatabase
            i={'ID':request.form['teacherId'],'Name':request.form['teacherName'],'Gender':request.form['teacherGender'],'Date of Birth':request.form['teacherDOB'],'Mobile Number':request.form['teacherMobile'],'Subject':request.form['teacherSubject'],'Year of Experience':request.form['teacherExperience'],'Number of Classes':request.form['teacherClasses'],'salary':request.form['teacherSalary']}
            db.TeachersData.insert_one(i)
            i = list(db.TeachersData.find({}))
            x=list()
            for j in i:
                del j['_id']
                x.append(j)
            if len(i)==0:
                return render_template('error.html')
            return render_template('show.html',i=x)
        except Exception as e:
            print(e)
            return render_template('delteach.html')
@app.route('/sub',methods=["GET","POST"])
def remove_teachers():
    if request.method=='POST':
        i=0
        try:
            client = MongoClient()
            uri = "mongodb+srv://madhan22012003:ncMG56zKqFRU69AL@teachermanagement.njy5gmr.mongodb.net/?retryWrites=true&w=majority"
            client = MongoClient(uri, server_api=ServerApi('1'))
            db = client.TeacherDatabase
            f=request.form['teacherId']
            db.TeachersData.delete_one({'ID':f})
            i = list(db.TeachersData.find({}))
            x=list()
            for j in i:
                del j['_id']
                x.append(j)
            if len(i)==0:
                return render_template('error.html')
            return render_template('show.html',i=x)
        except Exception as e:
            print(e)
            return render_template('delteach.html')
        
    else:
        return render_template('delteach.html')
    


@app.route('/getTeachers')
def get_teachers():
    i=0
    try:
        
        client = MongoClient()
        uri = "mongodb+srv://madhan22012003:ncMG56zKqFRU69AL@teachermanagement.njy5gmr.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client.TeacherDatabase
        i = list(db.TeachersData.find({}))
        for j in i:
            del j['_id']
        if len(i)==0:
                return render_template('error.html')
    except Exception as e:
        print(e)
    return render_template('show.html',i=i)
if __name__ == '__main__':
    app.run(debug=True)