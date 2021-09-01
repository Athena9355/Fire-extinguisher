# For Backend Code
# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)


@app.route('/greet', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if name.__len__() != 0:  # input field has content
            return render_template("greet.html", name=name)
    # starting and empty input default
    return render_template("greet.html", name="World")

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("greet.html")



@app.route('/A/')
def A_socialscience():
    return render_template("A.html")


