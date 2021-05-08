# Flask Flashing and the folder structure of the Flask Application
# flash() method is used for client side in the flask application application
# alert() method in the client side they are going to use in the java script
# flash(message, category)
#  message is show to the user( the password is incorrect)
# category - optional paramteter
# get_flashed_template() in the html template
# get_flashed_template(with_categories, category_filter)
# with_categories- optional parameters
# category_filter - optional parameters that is going to display special message

from flask import *

app=Flask(__name__)
app.secret_key="tek solutions"

@app.route("/index")
def home():
    return render_template("index1.html")

@app.route("/login", methods=['GET','POST'])
def login():
    error=None
    if request.method=="POST":
        if request.form['pass']!='tek':
            error="Invalid Password"
        else:
            flash("You are succesfully login into the Flask Application")
            return redirect(url_for('home'))

    return render_template("login.html",error=error )


if __name__=='__main__':
    app.run(debug=True)
