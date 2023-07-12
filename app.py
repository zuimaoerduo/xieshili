from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index.html')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/about.html')
def about():  # put application's code here
    return render_template("about.html")

@app.route('/services.html')
def services():  # put application's code here
    return render_template("services.html.")

@app.route('/contact.html')
def contact():  # put application's code here
    return render_template("contact.html.")
if __name__ == '__main__':
    app.run()
