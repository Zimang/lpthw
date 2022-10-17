from flask import Flask
from flask import render_template
from flask import request
app=Flask(__name__)

@app.route('/')
def hello_world():
    greeting="World"
    #return 'Hello,{greeting}'
    return render_template("index.html",grting=greeting)

@app.route('/hello',methods=['POST','GET'])
def index():
    
#用form的方式
    if request.method=="POST":
        name=request.form['name']
        greet=request.form['greeting']
        greeting=f"{greet},{name}"
        return render_template("index.html",greeting=greeting)
    else:
        return render_template("h_form.html")

#用?namel=...的方式
#name=request.args.get('name','nobody')
#    if name:
#        greeting= f"Hello,{name}"
#    else:
#        greeting="Hello,world"
#    return render_template("index.html",greeting=greeting)

if __name__=="__main__":
    app.run()
