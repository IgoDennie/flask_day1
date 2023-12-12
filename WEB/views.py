from flask import request, render_template
from WEB import app # buka folder web ambil app dari python environment


# Route Sections

@app.route('/')
def view(): 
    return render_template('index.html')