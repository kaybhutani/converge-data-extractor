from flask import Flask, Response, render_template,request,redirect,url_for,send_from_directory,jsonify,abort,send_file
import os
import pymongo
import config
import check
import pandas as pd
import events
import generate
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'GET':
    return render_template("index.html")
  else:
    email = request.form['email']
    password = request.form['password']
    if(check.checkPassword(email, password)):
      if(email == "kbhutani0001@gmail.com"):
        eventsList = list(events.names.keys())
      else:
        eventsList = events.getEventsOfHead(email)
      finalData = events.getDatabase(eventsList)
      generate.generate(finalData)
      return render_template("table.html", events=eventsList, data=finalData)
    else:
      return Response('''
        <h1>Wrong Password, Try again!</h1>
        <button onclick="window.location = '/'">Home</button>
        ''')



if(__name__=='__main__'):
	app.run(debug=True,use_reloader=True)
