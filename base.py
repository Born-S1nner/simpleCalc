from flask import Flask, request, render_template
from numero import minus, plus

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def system():
    results = ""
    errors = ""
    if request.method == "POST":
        body = request.get_json()
        numberOne = None
        numberTwo = None
        var = None
        try:
            numberOne = float(body.get('numone'))
            print(numberOne)
        except:
            errors += "<p>Number Slot one is not a number</p>"
        try:
            numberTwo = float(body.get('numtwo'))
            print(numberTwo)
        except:
            errors += "<p>Number Slot Two is not a number</p>"
        try:
            var = body.get('var')
            print(var)
        except:
            errors += "<p>Variable isn't present</p>"

        if var == '+':
            print(var)
            plusResult = plus(numberOne, numberTwo)
            print(plusResult)
            return render_template('index.html').format(result=plusResult, errors=errors)
        if var == '-':
            print(var)
            minusResult = minus(numberOne, numberTwo)
            print(minusResult)
            return render_template('index.html').format(result=minusResult, errors=errors)
    return render_template('index.html').format(result=results, errors=errors)    


app.run(debug=True)