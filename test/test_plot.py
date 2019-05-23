import en_core_web_sm
from spacy.tokens import Token
import visualise_spacy_tree

text = 'Forging involves the shaping of metal using localized compressive forces.'

nlp = en_core_web_sm.load()
doc = nlp(text)


def test_default_plot():
    plot = visualise_spacy_tree.plot(doc)
    with open('example_plots/default_plot.png', 'wb') as f:
        f.write(plot)


def test_custom_plot():
    Token.set_extension('plot', default={'color': 'aquamarine'})
    for token in doc:
        node_text = '{0} [{1}]\n({2} / {3})'.format(
                token.orth_,
                token.i,
                token.pos_,
                token.tag_
            )
        token._.plot['text'] = node_text
        if token.dep_ in ['ROOT', 'acl']:
            token._.plot['color'] = 'dodgerblue'
        if token.dep_ in ['nsubj', 'dobj']:
            token._.plot['color'] = 'deeppink1'
    plot = visualise_spacy_tree.plot(doc)
    with open('example_plots/custom_plot.png', 'wb') as f:
        f.write(plot)
