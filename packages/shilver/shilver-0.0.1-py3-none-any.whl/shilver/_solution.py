
from clingraph.orm import Factbase

from clingraph.graphviz import render
from clingraph.graphviz import compute_graphs

class Solution(Factbase):
    def as_json(self):
        return {'edges': [
            {'start': str(edge.symbol.arguments[0]), 'end': str(edge.symbol.arguments[1])}
            for edge in self.get_graph_elements(graph_id=self.get_all_graphs()[0], element_type='edge')
        ]}
        
    def view(self):
        render(compute_graphs(self), engine='neato', view=True)

    def save_as_pdf(self, filename):
        render(compute_graphs(self), directory='.', name_format=filename, format='pdf', engine='neato', view=False)
