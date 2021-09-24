from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = ',34.ml59kw0s;bv/8en'

@app.route('/')
def startPage():

    if 'number' not in session:
        session['number'] = 1
    else:
        session['number'] = session['number'] + 1

    return render_template('index.html')

@app.route('/destroy_session')
def clearSession():
    session.clear()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)