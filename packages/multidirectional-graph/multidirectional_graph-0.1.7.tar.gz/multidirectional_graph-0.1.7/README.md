# Multidirectional Graph

[![PyPI version](https://badge.fury.io/py/multidirectional-graph.svg)](https://badge.fury.io/py/multidirectional-graph)
[![codecov](https://codecov.io/gh/username/multidirectional-graph/branch/main/graph/badge.svg?token=abc123def456)](https://codecov.io/gh/username/multidirectional-graph)

Multidirectional Graph is a Python package that allows you to easily create graphs with multiple evaluation criteria, such as good, neutral, and bad.

## Installation

You can install Multidirectional Graph using pip:

```bash
pip install multidirectional-graph
```

## Usage

Here is an example of how to use Multidirectional Graph:

```python
from multidirectional_graph import MultidirectionalGraph

data = {
    "Leitura": {
        "categ 1A": 5,
        "categ 1B": 9,
        "categ 1C": 5,
    },
    "Escrita": {
        "categ 2A": 2,
        "categ 2B": 4,
        "categ 2C": 9,
        "categ 2D": 3,
    },
    "Nome extremamente grande\nque não cabe no espaço": {
        "categ 3A": 6,
        "categ 3B": 7,
    },
    "Listening": {
        "categ 4A": 2,
        "categ 4B": 3,
    },
}


added_data = {
    "categ 1A": 4,
    "categ 1B": 5,
    "categ 1C": 4,
    "categ 2A": 3,
    "categ 2B": 3,
    "categ 2C": 7,
    "categ 2D": 2,
    "categ 3A": 7,
    "categ 3B": 6,
    "categ 4A": 3,
    "categ 4B": 2,
}

graph = MultidirectionalGraph(
    data,
    tipo_avaliacao = "Lingua Inglesa",
    figsize=(5.5,15),
    main_plot_color="#902020",
    category_fontsize=12,
    group_title_fontsize=10,
)

graph.add_values(added_data, label="Autoavaliação")

fig = graph.plot()

fig.savefig("images/teste.png", dpi=100, bbox_inches='tight')

```

![](images/teste.png)