from flask import Flask, render_template, request
from controllers.login_controller import LoginController

# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__, template_folder='views', static_folder='static_files')

@app.route("/")
def main():
  return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    login_controller = LoginController(request)
    if login_controller.login():
      return render_template('login_success.html')
    else:
      return render_template('login_try_again.html')

  return render_template('login.html')
