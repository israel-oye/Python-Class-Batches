import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("fitness_activity_update.csv").sample(5)

x_pts = df['Student_Name']
y_pts = df['BMI']

plt.plot(x_pts, y_pts)
plt.title("BMI of Students")
plt.xlabel('Names')
plt.ylabel('BMI')

plt.show()

