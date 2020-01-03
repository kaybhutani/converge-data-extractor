from flask import Flask, Response, render_template,request,redirect,url_for,send_from_directory,jsonify,abort,send_file
import os
import pymongo
import config
import check
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'GET':
    return render_template("index.html")
  else:
    print("CHECK")
    email = request.form['email']
    password = request.form['password']
    if(check.checkPassword(email, password)):
      print(email, password)
      return "Done"
    else:
      return Response('''
        <h1>Wrong Password, Try again!</h1>
        <button onclick="window.location = '/'">Home</button>
        ''')




if(__name__=='__main__'):
	app.run(debug=True,use_reloader=True)
