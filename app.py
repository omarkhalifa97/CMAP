import time
from flask import Flask, render_template,send_from_directory,request,redirect
import os
import csv
import smtplib, ssl
from email.message import EmailMessage

app = Flask(__name__)
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "Anonymous"  # Enter your address
receiver_email = "omarkhalifa426@gmail.com"  # Enter receiver address
password = "knoqmuajdwblggkz"

msg = EmailMessage()

msg['Subject'] = "We found an idiot"
msg['From'] = sender_email
msg['To'] = receiver_email

context = ssl.create_default_context()

# @app.route('/')
# def home():
#     return redirect("https://www.instagram.com/trendyfactory.eg", code=302)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        total = int(data['total'])
        cost = int(data['cost'])
        st = int(data['st'])
        nd = int(data['nd'])
        rd = int(data['rd'])
        direct = st*0.160 + nd*0.178
        indirect = st*0.028 + nd*0.012
        result = (direct +indirect)*total*cost
        print(f"{rd} this is rdddddd")
        return render_template('result.html',result=result)
    else:
        return "You havn't submit the data"



def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

if '__main__' == __name__:
    app.run()



