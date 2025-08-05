---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - graph
---
PyGraphviz
Interface: Thin wrapper around the C Graphviz API.
Better integration with NetworkX, especially with graphviz_layout.

Advantages:

Native Graphviz object model (AGraph).

Seamless conversion between NetworkX graphs and Graphviz objects.

Supports advanced Graphviz features and layout options.

Limitations:

Requires Graphviz development libraries to be installed (can be hard to set up on Windows).

Slightly more complex installation due to C bindings.

Example with NetworkX:

python
from networkx.drawing.nx_agraph import graphviz_layout
pos = graphviz_layout(G, prog="dot")