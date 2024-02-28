from flask import Flask,request,render_template

obj=Flask(__name__)

@obj.route('/')
def welcome():
    return "just a usual thing flask"
print(__name__)
if __name__== '__main__':
    obj.run(debug=True)