from shilver import Solver
from shilver import Solution

solver = Solver()
solver.add_instance_from_file('tests/txt/8x8.txt')
solution = solver.get_solution()

print(solution.as_json())
