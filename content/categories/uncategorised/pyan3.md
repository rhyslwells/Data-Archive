Pyan3 is a **static call graph generator for Python**. It analyses source code (AST-level) and produces a directed graph of function/method relationships.

pyan3

For a specific file:
pyan3 src/components/competitor.py --uses --dot > competitor.dot

vscode extension "Graphviz interactive" to saave to svg

For the full graph of the repo:
pyan3 src/**/*.py --dot > repo.dot

multiple: 
pyan3 src/components/competitor.py src/predictor.py --uses --dot > competitor_predictor.dot

instead of --uses do --defines

