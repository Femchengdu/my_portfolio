# Import statememts
from flask import Flask, render_template, request, redirect, url_for


# Instansiate the flask app object.
app = Flask(__name__)

@app.route('/')
def application():
	# Return the index template
    return render_template(index.html)

# Add the super scret and call the app
app.secret_key = 'chengdu_ruby_python'

# I guess this is for error logging
app.debug = True    

# Run the app without specifying a port
app.run()

    


