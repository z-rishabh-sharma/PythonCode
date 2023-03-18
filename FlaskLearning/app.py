from flask import Flask, render_template
app = Flask(__name__) # providing the current object 

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/about')
def home():
    name = "Rishabh"
    return render_template('about.html', name = name)

app.run(debug=True)