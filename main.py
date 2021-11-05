# For Backend Code
# import "packages" from flask
from flask import Flask, render_template, request
from image import image_data
import configparser
from pathlib import \
    Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

# create a Flask instance
from templates.Stubs.generator import get_comment1, get_comment2
# from templates.Stubs.translatorAPI import api_translator
# from multiprocessing import Process
from templates.Stubs.translatorAPI import get_numberfact

app = Flask(__name__)


@app.route('/greet', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if name.__len__() != 0:
            if name.lower() == "athena":  # input field has content
                return render_template("About Me/athena.html", name=name)
            if name.lower() == "allison":  # input field has content
                return render_template("About Me/allison.html", name=name)
            if name.lower() == "gaurish":  # input field has content
                return render_template("About Me/gaurish.html", name=name)
            if name.lower() == "aadya":  # input field has content
                return render_template("About Me/aadya.html", name=name)
            else:
                return render_template("Labs/minilab.html", name=name)
        else:
            # starting and empty input default
            return render_template("Labs/minilab.html", name="World")
    else:
        return render_template("Labs/minilab.html")


@app.route('/greet_commentforum', methods=['GET', 'POST'])
def greet_commentforum():
    # submit button has been pushed
    if request.form:
        comment = request.form.get("comment")
        if comment.__len__() != 0:  # input field has content
            return render_template("Stubs/commentforum.html", comment=comment)
        else:
            # starting and empty input default
            return render_template("Stubs/commentforum.html", comment="World")
    else:
        return render_template("Stubs/commentforum.html")


@app.route('/greet_commentforum1', methods=['GET', 'POST'])
def greet_commentforum1():
    # submit button has been pushed
    if request.form:
        comment1 = request.form.get("comment1")
        if comment1.__len__() != 0:  # input field has content
            return render_template("Stubs/commentforum.html", comment1=comment1)
        else:
            # starting and empty input default
            return render_template("Stubs/commentforum.html", comment1="World")
    else:
        return render_template("Stubs/commentforum.html")


@app.route('/greet_commentforum3', methods=['GET', 'POST'])
def greet_commentforum3():
    # submit button has been pushed
    if request.form:
        comment3 = request.form.get("comment3")
        if comment3.__len__() != 0:  # input field has content
            return render_template("Stubs/classrecommendations.html", comment3=comment3)
        else:
            # starting and empty input default
            return render_template("Stubs/classrecommendations.html", comment3="World")
    else:
        return render_template("Stubs/classrecommendations.html")


@app.route('/greet_commentforum4', methods=['GET', 'POST'])
def greet_commentforum4():
    # submit button has been pushed
    if request.form:
        comment4 = request.form.get("comment4")
        if comment4.__len__() != 0:  # input field has content
            return render_template("Stubs/classrecommendations.html", comment4=comment4)
        else:
            # starting and empty input default
            return render_template("Stubs/classrecommendations.html", comment4="World")
    else:
        return render_template("Stubs/classrecommendations.html")


@app.route('/greet_athena', methods=['GET', 'POST'])
def greet_athena():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if name.__len__() != 0:  # input field has content
            return render_template("About Me/athena.html", name=name)
        else:
            # starting and empty input default
            return render_template("About Me/athena.html", name="World")
    else:
        return render_template("About Me/athena.html")


@app.route('/greet_gaurish', methods=['GET', 'POST'])
def greet_gaurish():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if name.__len__() != 0:  # input field has content
            return render_template("About Me/gaurish.html", name=name)
        else:
            # starting and empty input default
            return render_template("About Me/gaurish.html", name="World")
    else:
        return render_template("About Me/gaurish.html")


@app.route('/greet_allison', methods=['GET', 'POST'])
def greet_allison():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if name.__len__() != 0:  # input field has content
            return render_template("About Me/allison.html", name=name)
        else:
            # starting and empty input default
            return render_template("About Me/allison.html", name="World")
    else:
        return render_template("About Me/allison.html")


@app.route('/greet_aadya', methods=['GET', 'POST'])
def greet_aadya():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if name.__len__() != 0:  # input field has content
            return render_template("About Me/aadya.html", name=name)
        else:
            # starting and empty input default
            return render_template("About Me/aadya.html", name="World")
    else:
        return render_template("About Me/aadya.html")


# hi
# connects default URL to render index.html


@app.route('/rgb_render')
def rgb_render():
    # path = Path(app.root_path).joinpath("/static/assets")
    return render_template('Labs/RGB/rgb.html', images=image_data())


@app.route('/rgb')
def rgb():
    return render_template('Labs/RGB/rgb.html')


@app.route('/logicgate')
def logicgate():
    BITS = 8
    if request.method == 'POST':
        BITS = int(request.form['BITS'])
        print(BITS)
    return render_template("Labs/Logic Gate/logicgate.html", BITS=BITS)




# for input on binary
@app.route('/bits', methods=['GET', 'POST'])
def bits():
    BITS = 16
    if request.method == 'POST':
        BITS = int(request.form['BITS'])
        print(BITS)
    return render_template("Labs/Binary/binary.html", BITS=BITS)


# for input on ratingsystem
@app.route('/stars', methods=['GET', 'POST'])
def stars():
    STARS = 8
    if request.method == 'POST':
        STARS = int(request.form['STARS'])
        print(STARS)
    return render_template("Stubs/ratingsystem.html", STARS=STARS)


@app.route('/star', methods=['GET', 'POST'])
def star():
    STAR = 5
    if request.method == 'POST':
        STAR = int(request.form['STAR'])
        print(STAR)
    return render_template("Stubs/ratingsystem.html", STAR=STAR)


@app.route('/generator1', methods=['GET'])
def generator1():
    return render_template("Stubs/generator.html", random_comment1=get_comment1())


@app.route('/generator2', methods=['GET'])
def generator2():
    return render_template("Stubs/generator.html", random_comment2=get_comment2())


# binary inputs end

# @app.route('/input_binary', methods=['GET', 'POST'])
# def input_binary():
# submit button has been pushed
#    if request.form:
#       bitnumber = request.form.get("number")
#      if len(bitnumber) != 0:  # input field has content
#        return render_template("binary.html", BITS=int(bitnumber))
# return render_template("binary.html", BITS=8)

# binary input ends


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")


@app.route('/athena')
def athena():
    return render_template("About Me/athena.html")


@app.route('/allison')
def allison():
    return render_template("About Me/allison.html")


@app.route('/gaurish')
def gaurish():
    return render_template("About Me/gaurish.html")


@app.route('/aadya')
def aadya():
    return render_template("About Me/aadya.html")


@app.route('/binary')
def binary():
    BITS = 16
    if request.method == 'POST':
        BITS = int(request.form['BITS'])
        print(BITS)
    return render_template("Labs/Binary/binary.html", BITS=BITS)


@app.route('/ratingsystem')
def ratingsystem():
    BITS = 5
    if request.method == 'POST':
        BITS = int(request.form['BITS'])
        print(BITS)
    return render_template("Labs/Binary/binary.html", BITS=BITS)


@app.route('/classrecommendations')
def classrecommendations():
    return render_template("Stubs/classrecommendations.html")


@app.route('/commentforum')
def commentforum():
    return render_template("Stubs/commentforum.html")


@app.route('/videos')
def videos():
    return render_template("videos.html")


@app.route('/team/')
def team():
    return render_template("About Me/team.html")


@app.route('/binarywithinput')
def binarywithinput():
    return render_template("Labs/Binary/binarywithinput.html")


@app.route('/signedAddition')
def signedAddition():
    return render_template("Labs/Binary/signedAddition.html")


@app.route('/api_translator', methods=['GET', 'POST'])
def api_translator():
    number = " "
    if request.form:
        english_text = request.form.get("translate")
        number = get_numberfact(english_text)
        if number != 0:  # input field has content
            print("Please enter an input")
        print(number)

    return render_template("Stubs/api-translator.html", fact=number)


# translation=api_translator()

@app.route('/bits2', methods=['GET', 'POST'])
def bits2():
    BITS = 16
    if request.method == 'POST':
        BITS = int(request.form['BITS'])
        print(BITS)
    return render_template("Labs/Binary/signedAddition.html", BITS=BITS)

@app.route('/feedbackbase')
def feedbackbase():
    return render_template("Stubs/feedbackbase.html")


@app.route('/feedback')
def feedback():
    return render_template("Stubs/feedback.html")

@app.route('/feedback2')
def feedback2():
    return render_template("Stubs/feedback2.html")

@app.route('/feedback3')
def feedback3():
    return render_template("Stubs/feedback3.html")
# to display variable


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
