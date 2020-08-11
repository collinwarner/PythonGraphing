import os

from flask import Flask, render_template, request

from utils import Graph, Visualize

import random

import glob

glob_nodes = None
glob_edges = None

def create_app(test_config=None):
    global glob_nodes
    glob_nodes = None
    global glob_edges
    glob_edges = None
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    TEST_FOLDER = os.path.join('static', 'graph_plots')
    app.config['UPLOAD_FOLDER'] = TEST_FOLDER

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    #ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/default_graph')
    def default_graph():
        files = glob.glob(os.path.join(app.config['UPLOAD_FOLDER'], "*.png"))
        for f in files:
            os.remove(f)
        if glob_nodes is not None and glob_edges is not None:
            nodes = glob_nodes
            edges = glob_edges
        else:
            nodes = [1, 2, 3, 4]
            edges = [(1, 2), (2, 3), (3, 4), (4, 2)]

        isDirected = False
        g = Graph.Graph(nodes, edges, isDirected)
        filename = "plot"+str(random.randint(0, 10000))+".png"

        Visualize.save_fig(g, filename)

        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        return render_template("index.html", user_image=full_filename, graph_description=str(g))


    from model import InputForm


    @app.route('/input', methods=['GET', 'POST'])
    def index():
        template_name = "my-form"
        form = InputForm(request.form)
        if request.method == 'POST' and form.validate():

            global glob_nodes
            global glob_edges
            nodes = list(map(int, form.nodes.data.split()))
            edges = [tuple(map(int, t.split(","))) for t in form.edges.data.split()]

            glob_nodes = nodes
            glob_edges = edges
        return render_template(template_name + '.html',
                               form=form)
    return app

if __name__=="__main__":
    create_app().run()