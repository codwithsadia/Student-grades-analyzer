import pandas as pd
import matplotlib.pyplot as plt
data = {
  'Student' : ['John', 'Ayesha', 'Neha', 'Maxwell', 'Rahul'],
  'Maths' : [80,74.5,92,62,90],
  'Science' : [67,95,77,89,62],
  'English' : [87,69,93.5,86,83]
}

df = pd.DataFrame(data)
df['Average'] = df[['Maths','English','Science']].mean(axis=1)

top_students = df.sort_values(by = 'Average', ascending = False)
print("Top Students :\n",top_students[['Student','Average']])


plt.figure(figsize=(8, 5))
plt.bar(df['Student'], df['Average'], color='skyblue')
plt.title('Average Scores per Student')
plt.xlabel('Student')
plt.ylabel('Average Score')
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("average_scores.png")  
plt.show()
  
  
