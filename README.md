# sklearn-expense-tracker
 Python app that takes in raw transaction data, classifies individual purchases using logistic regression, then outputs statistics and charts.


## Steps to take:

0. Clean data: take in raw data from card statements and format it into tables

1. Classifier: ML or Manual
Given a "store" string, classify it into a category
	Groceries
	Eating Out
	Tech/Entertainment
	Clothing/Haircuts
	Gym/Fitness
	Household
	Rent/Utilities
	Music/Band
	Tuition

Which are classified as:
Necessities: (Rent, Groceries, Tuition) that must be paid 
Basics: (Gym, Clothing/Haircuts) that should have expenses but not too much
Luxuries: (Tech, Eating Out, Entertainment, Band) that should not go overboard 

2. Save learnt info
Have a saved set of confirmed store names and their category so old places are always categorized correctly

3. Visualization: Graphs, comparison features, budget 