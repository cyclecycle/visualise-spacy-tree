# visualise-spacy-tree

An alternative to [SpaCy's](https://spacy.io) [visualizer](https://spacy.io/usage/visualizers#dep), built on [GraphViz](https://graphviz.gitlab.io/). 

![Example plot image](https://github.com/cyclecycle/visualise-spacy-tree/blob/master/visualise_spacy_tree/example_plots/custom_plot.png)

## Prerequisites

- You need [GraphViz](https://graphviz.gitlab.io/download/) installed.

## Installation

With pip:

```bash
pip install visualise-spacy-tree
```

Or from source:

```bash
git clone https://github.com/cyclecycle/visualise-spacy-tree.git visualise_spacy_tree
cd visualise_spacy_tree
python setup.py install
```

## Usage

```python

# Parse a string to create SpaCy Doc object
import en_core_web_sm

text = 'Forging involves the shaping of metal using localized compressive forces.'

nlp = en_core_web_sm.load()
doc = nlp(text)

# Create the plot
import visualise_spacy_tree
png = visualise_spacy_tree.create_png(doc)

# Write it to a file
with open('parse_tree.png', 'wb') as f:
    f.write(png)

# If you're using Jupyter notebook, you can render it inline
from IPython.display import Image, display
display(Image(png))

# Override node attributes to customise the plot
from spacy.tokens import Token
Token.set_extension('plot', default={})  # Create a token underscore extension
for token in doc:
    node_label = '{0} [{1}])'.format(token.orth_, token.i)
    token._.plot['label'] = node_label
    if token.dep_ == 'ROOT':
        token._.plot['color'] = 'green'

'''
You can set any valid GraphViz dot attribute in 'plot'.
See GraphViz docs for reference of possible node attributes:
https://graphviz.gitlab.io/_pages/doc/info/attrs.html
'''

```

## Running the tests

Run 

```bash
pytest
```

from the root directory.

## Acknowledgements

Uses:

- [pydot](https://github.com/pydot/pydot)

## Contributions

Are welcome :)