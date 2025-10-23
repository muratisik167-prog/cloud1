from flask import Flask  
app = Flask(___name___)

@app.route(/)
def home():
  return "istanbul tripten selam"
