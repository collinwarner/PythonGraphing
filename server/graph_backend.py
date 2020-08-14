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
    filename = "plot" + str(random.randint(0, 10000)) + ".png"

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