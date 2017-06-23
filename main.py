#homework for web-caesar due June 22 using form not templates
from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #D864D6;
                padding: 30px;
                margin: 10 auto;
                width: 640px;
                font: 32px sans-serif;
                border-radius: 20px;
         
            }}
            
            textarea {{
                margin: 10px;
                width: 540px;
                height: 120px;
            }}
        
        </style>
    </head>
    <body>
    <form method="post">
        <label>rotation</label>
        <input type="text" name="rot" value="0"></label>
        <br>
        <textarea type="text" name="text">{0}</textarea>   
        <input type="submit" value="encrypt phrase">
    </form>

   </body>
</html>
""" 
@app.route("/", methods = ['POST'])
def encrypt():
 
    rotation_number=int(request.form['rot'])
    phrase=request.form['text']
    encryptedTxt = rotate_string(phrase, rotation_number)
    return form.format(encryptedTxt)

@app.route("/")
def index():
    return form.format('')

app.run()

