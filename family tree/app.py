# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Aarav" # write your name
    age = "7" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def fatherFlask():
    name = "Danish" # write your name
    age = "46" # write your age

    return render_template('father.html' , name = name , age = age)
app.run()


# define the route to mother webpage
@app.route("/mother")
def motherFlask():
    name = "Vibha" # write your name
    age = "44" # write your age

    return render_template('mother.html' , name = name , age = age)
app.run()


# define the route to friends webpage
@app.route("/friend")
def friendFlask():
    name = "Arjun" # write your name
    age = "7" # write your age

    return render_template('friend.html' , name = name , age = age)
app.run()


# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
