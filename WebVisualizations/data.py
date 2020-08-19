import pandas as pd
	
# Read the cities.csv file
df = pd.read_csv('Resources/cities.csv')
	
# Save as html file
df.to_html('data1.html', index=False)
	
# Assign to table to view
table = df.to_html()
print(table)
