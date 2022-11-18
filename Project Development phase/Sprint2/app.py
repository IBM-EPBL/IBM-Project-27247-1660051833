from flask import Flask,request,redirect,url_for,render_template
from werkzeug.utils import secure_filename
import os
app=Flask(__name__)
app.config['images']='C:\\Users\\DELL\\Downloads\\AI-BASED-NDA\\Flask\\static\\images'
@app.route('/home',methods=['GET'])
def home():
    return render_template('home.html')
@app.route('/home/intro',methods=['GET'])
def intro():
    return render_template('intro.html')
@app.route("/",methods=["POST","GET"])  
def upload():
    if request.method=="POST":
        print(request.files)
    
        image=request.files['file']
        if image.filename=='':
            print("filename is invalid")
            return redirect(request.url)
        filename=secure_filename(image.filename)
        basedir=os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(basedir,app.config["images"],filename))
        return render_template("upload.html",filename=filename)
    return render_template('upload.html')
@app.route('/display/<filename>')
def display(filename):
    return redirect(url_for('static',filename = '/images/'+filename),code=301)

app.run(port=5000)
