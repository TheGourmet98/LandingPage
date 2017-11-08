from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninjas.html')

@app.route('/dojo/new')
def dojo():
    return render_template('dojo.html')
app.run(debug=True)



