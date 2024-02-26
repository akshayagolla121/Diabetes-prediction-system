#backend of the app
from flask import Flask,render_template,jsonify,request
import pickle
import sqlite3    #to connect the table and queries
app = Flask(__name__)

@app.route('/') #for home url empty /
def home():
    return render_template('home.html')
@app.route('/prediction.html',methods =['GET','POST']) #to know we need to open the prediction.html page
def prediction():
    if request.method == 'POST':
        preg = request.form.get("Pregnancies")
        gluco = request.form.get("Glucose")
        bp = request.form.get("BloodPressure")
        skinthick = request.form.get("SkinThickness")
        insulin = request.form.get("Insulin")
        bmi = request.form.get("BMI")
        DPF = request.form.get("DiabetesPedigreeFunction")
        age = request.form.get("Age")
        print(preg,gluco,bp,skinthick,insulin,bmi,DPF,age)
        with open('model.pkl','rb') as model_file:
            mlmodel=pickle.load(model_file)
        res = mlmodel.predict([[int(preg),int(gluco),int(bp),int(skinthick),int(insulin),float(bmi),float(DPF),int(age)]])
        #jsonify will return to frontend file
        print(res)
        conn = sqlite3.connect('diabetes.db')
        cur = conn.cursor()
        cur.execute(f'''INSERT INTO DIABETES VALUES({preg},{gluco},{bp},{skinthick},{insulin},{bmi},{DPF},{age},{res[0]})''')
        
        conn.commit()
        return render_template("result.html",res=res[0])#res[0] since 1 is getting inb a list 
    else:
        return render_template('prediction.html')
@app.route('/showdata.html',methods =['GET','POST'])
def showdata():
    conn = sqlite3.connect('diabetes.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM DIABETES")
    x=cur.fetchall()
    

    return render_template('showdata.html')    


#to run code in aloop
if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=5050)  #entire project available for public