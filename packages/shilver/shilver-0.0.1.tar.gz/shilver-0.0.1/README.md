# Shingoki solver

Práctica RCRA 2022-2023

## Setup

```sh
python -m install clingo clingraph
```

## Usage

```sh
# Solve example: clingo 0 solver.lp <examplefile>
clingo 0 solver.lp tests/6x6easy.lp

# Solve and draw solution:
clingo 0 tests/8x8normal.lp solver.lp --outf=2 | clingraph --viz-encoding=viz.lp --engine=neato --out=render --view

# Remove 'solver.lp' for drawing initial state
clingo 0 tests/8x8normal.lp --outf=2 | clingraph --viz-encoding=viz.lp --engine=neato --out=render --view
```