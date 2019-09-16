from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

# TODO:

form = """

<!DOCTYPE html>
<html>
    <head>
        <style>
         form {{
            background-color: #eee;
            padding: 20px;
            margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px;
        }}
            
        textarea {{
            margin: 10px 0;
            width: 540px;
            height: 120px;
        }}
        </style>
    </head>
    <body>

        <form method="post">
            <label for="rot">Rotate by:
                <input type="text" name="rot" value="0">
            </label>
            <textarea type="text" name="text">{0}</textarea>
            <br />
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
"""    

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    # Store cypher key and text to be encrypted into local variables.
    cypher = int(request.form['rot'])
    text_to_encrypt = request.form['text']

    # Encrypt the supplied credentials.
    encrypted_text = rotate_string(text_to_encrypt, cypher)

    # Display encrypted message.
    return form.format(encrypted_text)


app.run()