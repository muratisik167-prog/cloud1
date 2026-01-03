from flask import Flask  
app = Flask(___name___)

"""
<html>
        <head>
            <title>murat işık</title>
        </head>
"""

@app.route('/')
def home():
  return "merhaba buluttan selam"
