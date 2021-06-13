from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def basic():
    return render_template("frontend.html")

@app.route('/register_page')
def register_page():
    return render_template("register.html")
    
@app.route('/login_page')
def login_page():
    return render_template("login.html")

@app.route('/manage_page',methods=['POST','GET'])
def manage_page():
    if request.method =='POST':
        return redirect(url_for('manage_page'))
    return render_template('manage.html')


if __name__ == '__main__':
    app.run(debug=True)

    