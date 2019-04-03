import os
import base64

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY').encode()

num_peeps = 2

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        total_bill = float(request.form.get('total_bill'))
        incomes = request.form.getlist('incomes')
        incomes = [float(k) for k in incomes]
        names = request.form.getlist('names')
        add_p = request.form.get('addPeeps')
        rem_p = request.form.get('remPeeps')
        print(total_bill)
        print(incomes)
        print(names)
        print(add_p)
        print(rem_p)
        return render_template('home.jinja2',
                               total=total_bill,
                               split_info = all_info(total_bill, names, incomes),
                               n_peeps = num_peeps)
    return render_template('home.jinja2',
                           total=-1,
                           split_info=[],
                           n_peeps=num_peeps)

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.jinja2')

def all_info(total, names, incomes):
    num_peeps = 2
    info = []
    adj_split = [round((k/sum(incomes))*total, 2) for k in incomes]
    reg_split = round(total/len(incomes), 2)
    for index in range(len(incomes)):
        inc = incomes[index]
        adj = adj_split[index]
        info.append((names[index], incomes[index],
                     reg_split, round(reg_split*100/inc, 2),
                     adj, round(adj*100/inc, 2)))
    return info


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
