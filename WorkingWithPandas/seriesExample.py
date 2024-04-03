import pandas as pd

reviews = pd.Series([4.6, 4.4, 4.8, 5])
print(reviews)
print(reviews.describe())
print(reviews[1])

print(reviews.count())
print(reviews.mean())
print(reviews.min())
print(reviews.max())
print(reviews.std())

reviews = pd.Series([4.6, 4.4, 4.8, 5],index=["Python","Django","Java","DRF"])
print(reviews)

reviews = pd.Series({'python' : 4.6, 'Django' : 4.8, 'DRF' : 5})
print(reviews)
print(reviews['python'])
print(reviews.python)
print(reviews.Django)
print(reviews.DRF)
print(reviews.values)
print(reviews.index)

courses = pd.Series(["Python","Django","DRF","Azure"])
print(courses)
print(courses.str.upper())
print(courses.str.contains('z'))