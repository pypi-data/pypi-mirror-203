from clingo import Control
from collections.abc import Sequence

from ._solution import Solution
from ._encoder import Encoder
from .shilver_lp import SOLVER_LP, VIZ_LP

from clingraph.clingo_utils import ClingraphContext

class Solver(Control):
    def __init__(self):
        super().__init__([])

    def add_instance_from_file(self, input_file):
        self.add('base', [], Encoder().from_file(input_file))

    def add_str_facts(self, str_facts):
        self.add('base', [], str_facts)

    def _get_solutions(self, input_file) -> Sequence[Solution]:
        self.add('base', [], SOLVER_LP)
        self.add('base', [], VIZ_LP)
        
        self.ground([('base',[])], context=ClingraphContext())
        
        solutions = []
        self.solve(on_model=lambda m: solutions.append(Solution.from_model(m)))
        return solutions

    def get_solution(self, input_file=None, asp_str=None) -> Solution:
        return self._get_solutions(input_file=input_file).pop()

    def _check_individual_solution(self, input_file=None, asp_str=None):
        return len(self._get_solutions(input_file=input_file)) == 1
