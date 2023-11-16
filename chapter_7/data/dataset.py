# Generate a dataset of assets for an ITAM system. The dataset should include the following columns: id (int), name (varchar), status (varchar), category (varchar), cost (float), useful_life (float), salvage_value (float), funding_details (varchar), depreciation_strategy (varchar). The dataset should have 1000 rows, sorted by id. Each row should have the following characteristics:
# - id should be a unique integer and sequential starting at 1.
# - name should be a random first names Each name should be between 3 and 10 characters long and should be a common name for the English language.
# - status should be a random selection from the following valid asset statuses: in use, in storage, disposed, in repair, in transit, other. 
# - category should be a random selection from the following valid categories: hardware. 
# - cost should be a random float between 0 and 100000.
# - useful_life should be a random float between 1 and 10.
# - salvage_value should be a random float between 0 and 10000.
# - funding_details should be a random selection from the following valid funding details: purchased. 
# - depreciation_strategy should be a random selection from the following valid depreciation strategies: straight line. 
# The dataset should be saved as a CSV file named assets.csv in the data directory. The file should have a header row and the columns should have the following data types: id (int), name (varchar), status (varchar), category (varchar), cost (float), useful_life (float), salvage_value (float), funding_details (varchar), depreciation_strategy (varchar).
# All varchar columns should be between double quotes. The CSV file should be sorted by id.


# Question: Is there a way to make the random names more realistic? 
# Answer: Yes, we could use a list of common names for the English language.

# Question: Where can I get that list?
# Answer: https://www.ssa.gov/oact/babynames/limits.html


import pandas as pd
import numpy as np
import random
import string
import csv

#write a function that takes the list of names from https://www.ssa.gov/oact/babynames/limits.html and returns 1000 random names from that list
def random_names():
    names = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles', 'Christopher', 'Daniel', 'Matthew', 'Anthony', 'Donald', 'Mark', 'Paul', 'Steven', 'Andrew', 'Kenneth', 'George', 'Joshua', 'Kevin', 'Brian', 'Edward', 'Ronald', 'Timothy', 'Jason', 'Jeffrey', 'Ryan', 'Jacob', 'Gary', 'Nicholas', 'Eric', 'Stephen', 'Jonathan', 'Larry', 'Justin', 'Scott', 'Brandon', 'Frank', 'Benjamin', 'Gregory', 'Samuel', 'Raymond', 'Patrick', 'Alexander', 'Jack', 'Dennis', 'Jerry', 'Tyler', 'Aaron', 'Jose', 'Henry', 'Adam', 'Douglas', 'Nathan', 'Peter', 'Zachary', 'Kyle', 'Walter', 'Harold', 'Jeremy', 'Ethan', 'Carl', 'Keith', 'Roger', 'Gerald', 'Christian', 'Terry', 'Sean', 'Arthur', 'Austin', 'Noah', 'Lawrence', 'Jesse', 'Joe', 'Bryan', 'Billy', 'Jordan', 'Albert', 'Dylan', 'Bruce', 'Willie', 'Gabriel', 'Alan', 'Juan', 'Logan', 'Wayne', 'Ralph', 'Roy', 'Eugene', 'Randy', 'Vincent', 'Russell', 'Louis', 'Philip', 'Bobby', 'Johnny', 'Bradley']
    return random.choices(names, k=1000)

#write a function that takes the list of statuses and returns 1000 random statuses from that list
def random_statuses():
    statuses = ['in use', 'in storage', 'disposed', 'in repair', 'in transit', 'other']
    return random.choices(statuses, k=1000)

#write a function that takes the list of categories and returns 1000 random categories from that list
def random_categories():
    categories = ['hardware']
    return random.choices(categories, k=1000)

#write a function that takes the list of funding details and returns 1000 random funding details from that list
def random_funding_details():
    funding_details = ['purchased']
    return random.choices(funding_details, k=1000)

#write a function that takes the list of depreciation strategies and returns 1000 random depreciation strategies from that list
def random_depreciation_strategies():
    depreciation_strategies = ['straight line']
    return random.choices(depreciation_strategies, k=1000)

def random_costs():
    costs = np.random.uniform(low=0, high=100000, size=1000)
    return costs

def random_useful_lives():
    useful_lives = np.random.uniform(low=1, high=10, size=1000)
    return useful_lives

def random_salvage_values():
    salvage_values = np.random.uniform(low=0, high=10000, size=1000)
    return salvage_values

def random_ids():
    ids = np.arange(1,1001)
    return ids

# write a main run function that calls all of the above functions and creates a dataframe with the results
def main():
    names = random_names()
    statuses = random_statuses()
    categories = random_categories()
    funding_details = random_funding_details()
    depreciation_strategies = random_depreciation_strategies()
    costs = random_costs()
    useful_lives = random_useful_lives()
    salvage_values = random_salvage_values()
    ids = random_ids()
    df = pd.DataFrame({'id': ids, 'name': names, 'status': statuses, 'category': categories, 'cost': costs, 'useful_life': useful_lives, 'salvage_value': salvage_values, 'funding_details': funding_details, 'depreciation_strategy': depreciation_strategies})
    df = df.sort_values(by=['id'])
    df.to_csv('data/assets.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)

if __name__ == '__main__':
    main()