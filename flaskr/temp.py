from flask import Flask, render_template
import os

TEST_FOLDER = os.path.join('static', 'graph_plots')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = TEST_FOLDER

@app.route('/')
@app.route('/index')
def show_index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'output.png')
    return render_template("index.html", user_image = full_filename )

if __name__=="__main__":
    app.run()
