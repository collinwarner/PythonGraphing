from flask import Flask, render_template, request, redirect, url_for, session
from utils import Graph, Visualize, random_graphs, path_finding

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = "some secret"
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/display", methods=["GET", "POST"])
def display():
    g = session.get("current_graph")
    print(g)
    g = Graph.convert_back(g)
    print(repr(g))
    filename = "static/graph_plots/inputPlot.png"
    filename1 = "inputPlot.png"
    shortest_path = None
    if request.method == "POST" and g:
        n1, n2 = tuple(map(int, request.form["node_pair"].strip().split(',')))
        shortest_path = path_finding.shortest_path(g, n1, n2)
        Visualize.save_fig(g, filename1, shortest_path)

    return render_template("display.html", graph_img=filename, shortest_path=shortest_path)


@app.route("/input", methods=["GET", "POST"])
def input():
    error = None
    if request.method == "POST":
        if "nodes" in request.form and "edges" in request.form and "isDirected" in request.form or "numNodes" in request.form:
            if "numNodes" in request.form:
                g = random_graphs.create_uniform_graph(int(request.form["numNodes"].strip()),
                                                float(request.form["connectionProb"].strip()))
            else:
                nodes = int(request.form["nodes"].strip())
                edges = [tuple(map(int, t.split(","))) for t in request.form["edges"].strip().split()]
                isDirected = False if request.form["isDirected"].lower() == "false" else True
                g = Graph.Graph(nodes, edges, isDirected)
            session["current_graph"] = repr(g)
            filename = "inputPlot.png"
            Visualize.save_fig(g, filename)
            return redirect(url_for("display"))

    return render_template("input.html")

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache"#, no-store, must-revalidate"
    #r.headers["Pragma"] = "no-cache"
    #r.headers["Expires"] = "0"
    #r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    app.run(debug=True)