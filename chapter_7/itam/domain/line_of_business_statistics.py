# Define a class called LineOfBusinessStatistics
# with the following attributes
#        -line_of_business: LineOfBusiness
#        -total_cost: float
#        -total_depreciation: float
# and with the following methods:
#        +__init__(self, line_of_business: LineOfBusiness, total_cost: float, total_depreciation: float)
#        +get_line_of_business(self) -> Department
#        +get_total_cost(self) -> float
#        +get_total_depreciation(self) -> float
#        +set_line_of_business(self, line_of_business: LineOfBusiness)
#        +set_total_cost(self, total_cost: float)
#        +set_total_depreciation(self, total_depreciation: float)

class LineOfBusinessStatistics:
    def __init__(self, line_of_business, total_cost, total_depreciation):
        self.line_of_business = line_of_business
        self.total_cost = total_cost
        self.total_depreciation = total_depreciation

    def get_line_of_business(self):
        return self.line_of_business

    def get_total_cost(self):
        return self.total_cost

    def get_total_depreciation(self):
        return self.total_depreciation

    def set_line_of_business(self, line_of_business):
        self.line_of_business = line_of_business

    def set_total_cost(self, total_cost):
        self.total_cost = total_cost

    def set_total_depreciation(self, total_depreciation):
        self.total_depreciation = total_depreciation