from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []   # simple list as database

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        students.append({'name': name, 'email': email})
        return redirect('/')

    return render_template('index.html', students=students)

@app.route('/delete/<int:index>')
def delete(index):
    students.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)