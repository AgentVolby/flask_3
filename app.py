from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/faq')
def faq():
    return render_template("faq.html")

@app.route('/secret')
def secret():
    return render_template("secret.html")

@app.route('/support')
def support():
    return render_template("support.html")

if __name__ == "__main__":
    app.run()