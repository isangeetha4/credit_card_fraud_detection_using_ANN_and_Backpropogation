import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Load user credentials from users.json
with open('data/users.json', 'r') as f:
    users = json.load(f)

print(users)

@app.route('/', methods=['GET', 'POST'])
def login():
    print(" hello")
    print(request.method)
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(email,password)
        if email in users and users[email] == password:
            print("authentication succes")
            # Authentication successful, redirect to home page
            return redirect(url_for('home'))
        else:
            # Authentication failed, redirect to signup page
            return redirect(url_for('signup'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        print("insdue sign up")
        email = request.form['email']
        password = request.form['password']
        if email not in users:
            print(users)
            users[email] = password
            with open('data/users.json', 'w') as f:
                json.dump(users, f)
            return redirect(url_for('login'))
        else:
            return 'Email already exists. Please <a href="/">login</a>.'
    return render_template('signup.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/transactions')
def transactions():
    return render_template('transactions.html')

@app.route('/graph_output')
def graph_output():
    return render_template('graph_output.html')

if __name__ == '__main__':
    app.run(debug=True)
