from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>murat işık</title>
        </head>
        <body>
            merhaba buluttan selam
        </body>
    </html>
    """
if __name__ == "__main__":
    app.run(debug=True)
