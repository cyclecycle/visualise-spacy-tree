import pydot


DEFAULT_NODE_ATTRS = {
    'color': 'cyan',
    'shape': 'box',
    'style': 'rounded',
    'fontname': 'palatino',
    'fontsize': 10,
    'penwidth': 2
}


def node_label(token):
    try:
        label = token._.plot['label']
    except:
        label = '{0} [{1}]\n({2} / {3})'.format(
            token.orth_,
            token.i,
            token.pos_,
            token.tag_
        )
    return label


def get_edge_label(from_token, to_token):
    label = ' ' + from_token.dep_
    return label


def to_pydot(tokens, get_edge_label=get_edge_label):
    graph = pydot.Dot(graph_type='graph')

    # Add nodes to graph
    idx2node = {}
    for token in tokens:
        try:
            plot_attrs = token._.plot
        except AttributeError:
            plot_attrs = {}
        for attr, val in DEFAULT_NODE_ATTRS.items():
            if attr not in plot_attrs:
                plot_attrs[attr] = val
        label = node_label(token)
        plot_attrs['name'] = token.i
        plot_attrs['label'] = label
        node = pydot.Node(**plot_attrs)
        idx2node[token.i] = node
        graph.add_node(node)

    '''Add edges'''
    for token in tokens:
        if token.dep_ == 'ROOT':
            continue
        if token.head not in tokens:
            continue
        from_token = token
        to_token = token.head
        from_node = idx2node[from_token.i]
        to_node = idx2node[to_token.i]
        label = get_edge_label(from_token, to_token)
        edge = pydot.Edge(
            to_node, from_node, label=label,
            fontsize=12
        )
        graph.add_edge(edge)

    return graph


def create_png(tokens):
    graph = to_pydot(tokens)
    png = graph.create_png()
    return png
