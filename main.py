# For Backend Code
# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


@app.route('/greet', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if name.__len__() != 0:  # input field has content
            return render_template("greet.html", name=name)
        else:
            # starting and empty input default
            return render_template("greet.html", name="World")
    else:
        return render_template("greet.html")


# connects default URL to render index.html
#@app.route('/')
#def index():
#   return render_template("greet.html")



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/athena')
def athena():
    return render_template("athena.html")

@app.route('/allison')
def allison():
    return render_template("allison.html")

@app.route('/gaurish')
def gaurish():
    return render_template("gaurish.html")

@app.route('/aadya')
def aadya():
    return render_template("aadya.html")

@app.route('/A/')
def A_socialscience():
    return render_template("A.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
