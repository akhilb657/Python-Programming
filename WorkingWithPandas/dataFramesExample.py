import pandas as pd

scores_dict = {'Kohli': [100,50,90], 'Rohit': [11,22,33], 'Surya':  [44,55,66], 'Jadeja': [111,2,32]}

scores = pd.DataFrame(scores_dict)
scores.index = ['Match_1', 'Match_2', 'Match_3']
print(scores)

print("Kohli's score")
print(scores['Kohli'])
print(scores.Kohli)

print(scores.loc['Match_1'])
print(scores.iloc[1])

print(scores.loc['Macth_1':'Match_2'])
print(scores.iloc[0:2])

print(scores.loc[['Match_1','Match_3']])
print(scores.iloc[[0,1]])

print(scores.loc['Match_1':'Match_2',['Kohli','Surya']])
print(scores.iloc[[0,2],0:3])

print(scores[scores > 90])
print(scores[(scores >= 80) & (scores <= 90)])

print(scores.at['Match_2','Kohli'])
print(scores.iat[2,0])

scores.at['Match_2','Kohli'] = 150
print(scores.at['Match_2','Kohli'])

scores.iat[2,0] = 200
print(scores.iat[2,0])

print(scores)
print(scores.mean())
pd.set_option('display.precision',2)
print(scores.describe())
print(scores.T.describe())

print(scores)
print(scores.sort_index(ascending=False))
print(scores.sort_index(axis=1))

print(scores)
print(scores.sort_values(by='Match_1',axis=1, ascending=False))

customer_df = pd.read_csv('customer.csv',names=['firstName','lastName','email','phoneNo'])
print(customer_df)

customer_df.to_csv('customer_df.csv',index=False)