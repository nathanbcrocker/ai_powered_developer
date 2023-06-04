# define an interface called class DepartmentVisitor with the following methods:
#        +visit(self, asset: Asset) -> None
# Additionally, define a class called class DepartmentStatisticsVisitor that implements the interface DepartmentVisitor

from abc import ABC, abstractmethod
from itam.domain.asset import Asset


class DepartmentVisitor(ABC):
    @abstractmethod
    def visit(self, asset: Asset) -> None:
        pass


# Question: What is the maintainability index of the class DepartmentStatisticsVisitor?
# Answer: 100

# Question: What is the cyclomatic complexity of the class DepartmentStatisticsVisitor?
# Answer: 1

# Question: What is the number of lines of code of the class DepartmentStatisticsVisitor?
# Answer: 12

# Question: Is 100 a good maintainability index?
# Answer: Yes

# Question: Is 1 a good cyclomatic complexity?
# Answer: Yes

# Question: What is the Halstead Complexity Measures of the class DepartmentStatisticsVisitor?
# Answer: 2

# Question: What is the Halstead Difficulty Measures of the class DepartmentStatisticsVisitor?
# Answer: 1

# Question: Is 2 a good Halstead Complexity Measures?
# Answer: Yes

# Question: Is 1 a good Halstead Difficulty Measures?
# Answer: Yes

# Question: What is a bad Halstead Difficulty Measures?
# Answer: 10

# Question: What is a bad Halstead Complexity Measures?
# Answer: 10

# Question: What is the Halstead Volume of the class DepartmentStatisticsVisitor?
# Answer: 2

# Question: What is a bad Halstead Volume?
# Answer: 100

# Question: Do we want a high Cyclomatic Complexity or low Cyclomatic Complexity?
# Answer: low

# Question: Do we want a high Maintainability Index or low Maintainability Index?
# Answer: high

# Qusetion: Do we want a high number of lines of code or low number of lines of code?
# Answer: low

# Question: Why do we want a low number of lines of code?
# Answer: Because it is easier to maintain

class DepartmentStatisticsVisitor(DepartmentVisitor):
    def __init__(self):
        self._total_cost = 0
        self._total_depreciation = 0
        self._total_allocation = 0

    def visit(self, asset: Asset) -> None:
        self._total_cost += asset.get_cost()
        self._total_depreciation += asset.get_funding_details().get_depreciation_strategy().calculate_depreciation(asset)
        #self._total_allocation += asset.get_funding_details().get_allocation()

    def get_total_cost(self):
        return self._total_cost

    def get_total_depreciation(self):
        return self._total_depreciation

    def get_total_allocation(self):
        return self._total_allocation
