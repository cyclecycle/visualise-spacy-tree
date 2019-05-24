import pydot


DEFAULT_NODE_ATTRS = {
    'color': 'cyan',
    'shape': 'box',
    'style': 'rounded',
    'fontname': 'palatino',
    'fontsize': 10,
    'penwidth': 2
}


def node_text(token):
    try:
        text = token._.plot['text']
    except:
        text = '{0} [{1}]\n({2} / {3})'.format(
            token.orth_,
            token.i,
            token.pos_,
            token.tag_
        )
    return text


def plot(doc):

    graph = pydot.Dot(graph_type='graph')

    # Add nodes to graph
    idx2node = {}
    for token in doc:
        try:
            plot_attrs = token._.plot
        except AttributeError:
            plot_attrs = {}
        for attr, val in DEFAULT_NODE_ATTRS.items():
            if attr not in plot_attrs:
                plot_attrs[attr] = val
        text = node_text(token)
        plot_attrs['name'] = text
        node = pydot.Node(**plot_attrs)
        idx2node[token.i] = node
        graph.add_node(node)

    '''Add edges'''
    for token in doc:
        if token.dep_ != 'ROOT':
            from_node = idx2node[token.i]
            to_node = idx2node[token.head.i]
            label = ' ' + token.dep_
            edge = pydot.Edge(
                to_node, from_node, label=label,
                fontsize=12
            )
            graph.add_edge(edge)

    png = graph.create_png()

    return png
