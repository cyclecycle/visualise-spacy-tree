# visualise-spacy-tree

An alternative to SpaCy's built-in visualisation method.

[[https://github.com/cylcecycle/visualise_spacy_tree/blob/master/example_plots/custom_plot.png]]

## Installation

With pip:

```bash
pip install visualise-spacy-tree
```

## Usage

```python

import en_core_web_sm
import visualise_spacy_tree

text = 'Forging involves the shaping of metal using localized compressive forces.'

# Parse text, create Doc object
nlp = en_core_web_sm.load()
doc = nlp(text)

# Create png plot
plot = visualise_spacy_tree.plot(doc, default_color='cyan')

# Write it to a file
with open('parse_tree.png', 'wb') as f:
    f.write(plot)

# Or render it in jupyter notebook
from IPython.display import Image, display
display(Image(plot))

# Override node display text with the 'plot' token underscore extension
from spacy.tokens import Token
Token.set_extension('plot', default={})
for token in doc:
    node_text = '{0} [{1}]\n({2} / {3})'.format(
            token.orth_,
            token.i,
            token.pos_,
            token.tag_
        )
    token._.plot['text'] = node_text

# Customise node styles
doc[0]._.plot['color'] = 'green'  # Make first token green
doc[1]._.plot['style'] = 'rounded'  # Make second token rounded

# See GraphViz docs for reference of possible node attributes: https://graphviz.gitlab.io/_pages/doc/info/attrs.html

```

## Built with

[pydot][https://github.com/pydot/pydot]
