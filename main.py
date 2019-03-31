import os
import base64

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY').encode()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        total_bill = request.form['total']
        incomes = request.form.getlist['incomes']
        names = request.form.getlist['names']
        return redirect(url_for('result', total=total_bill, income_list=incomes, name_list=names))
        
    return render_template('home.jinja2')


@app.route('/result')
def result(total=0, income_list=[], name_list=[]):
    render_template('result.jinja2')


def process_splits(total, *incomes):
    return [round((k/sum(incomes))*total, 2) for k in incomes]

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
