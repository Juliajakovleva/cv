from os import execlp
from flask import Flask, render_template, request, url_for, redirect
from flask.json.tag import PassDict
from file_proc import pievienot, lasitRindinas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/postData', methods = ['POST', 'GET'])
def postData():
    if request.method == 'GET':
        return redirect('/')
    elif request.method == 'POST':
        #print(request.form)
        vards = request.form.get('vards')
        pievienot(vards)
        return redirect('/#contact')
    else:
        return "This method not supported!"

@app.route('/lasitDatus')
def lasitDatus():
    rindinas = lasitRindinas()
    dati = []
    dati2 = []
    for rindina in rindinas:
        ieraksts = rindina.split(',')
        print(rindina)
        print(ieraksts)
        dati.append(ieraksts)

    print(dati)
    return render_template("dati.html", rindinas = dati, rindinas2 = dati2)


if __name__ == "__main__":
    app.run(debug=True)