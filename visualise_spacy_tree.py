# from IPython.display import Image, display
import pydot


PLOT_COLOUR_MAP = [
    {
        'attr': 'chunk_type',
        'is_underscore': True,
        'val': 'entity',
        'colour': 'lightsalmon',
    },
    {
        'attr': 'chunk_type',
        'is_underscore': True,
        'val': 'predicate',
        'colour': 'palegreen',
    }
]


def plot(doc, colour_map=PLOT_COLOUR_MAP, default_colour='cyan', display_plot=False):

    def choose_color(token):
        for cond in colour_map:
            try:
                if not cond['is_underscore']:
                    attr = getattr(token, cond['attr'])
                else:
                    attr = getattr(token._, cond['attr'])
                if attr == cond['val']:
                    return cond['colour']
            except AttributeError:
                # print('No attribute named {}'.format(cond['attr']))
                pass
        return default_colour

    graph = pydot.Dot(graph_type='graph')

    '''Add nodes to graph (tokens)'''
    idx2node = {}
    for token in doc:
        color = choose_color(token)
        node_text = '{0} [{1}]\n({2} / {3})'.format(token.orth_, token.i, token.pos_, token.tag_)
        node = pydot.Node(
            node_text,
            shape='box',
            color=color,
            penwidth=1,
            # style='rounded',
        )
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

    if display_plot:
        display(Image(png))

    return png