from __future__ import print_function
import collections
from ortools.sat.python import cp_model

def main():
  # Create the model and solver.
  model = cp_model.CpModel()
  solver = cp_model.CpSolver()
  # Create the variables.
  num_vals = 3
  x = model.NewIntVar(0, num_vals - 1, "x")
  y = model.NewIntVar(0, num_vals - 1, "y")
  z = model.NewIntVar(0, num_vals - 1, "z")
  # Create the constraints.
  model.Add(x != y)
  # Call the solver.
  solution_printer = SolutionPrinter([x, y, z])
  status = solver.SearchForAllSolutions(model, solution_printer)
  print('\nNumber of solutions found: %i' % solution_printer.SolutionCount())

class SolutionPrinter(cp_model.CpSolverSolutionCallback):
  """Print intermediate solutions."""

  def __init__(self, variables):
    self.__variables = variables
    self.__solution_count = 0

  def NewSolution(self):
    self.__solution_count += 1
    for v in self.__variables:
      print('%s = %i' % (v, self.Value(v)), end = ' ')
    print()

  def SolutionCount(self):
    return self.__solution_count

if __name__ == '__main__':
  main()