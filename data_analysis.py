import pandas as pd
import numpy as np

df = pd.read_csv("clean_data.csv")
print(df["Accel-Z"].mean())
#9.743679279894787
print(df["Accel-Z"].median())
#9.720214451623715
print(np.linalg.norm((df[['Accel-X','Accel-Y','Accel-Z']].mean())))
#9.746110489742701
print(np.linalg.norm((df[['Accel-X','Accel-Y','Accel-Z']].median())))
#9.721328048631616
mean = df[['Accel-X', 'Accel-Y', 'Accel-Z']].mean()
median = df[['Accel-X', 'Accel-Y', 'Accel-Z']].median()
gravity = [0,0,-1]
mean_tilt = 180 - np.degrees(np.arccos( (np.dot(gravity, mean) / np.linalg.norm(mean)) ))
median_tilt = 180 - np.degrees(np.arccos( (np.dot(gravity, median) / np.linalg.norm(median)) ))
print(mean_tilt)
print(median_tilt)