import pandas as pd
import requests
import os
import os
df = pd.read_csv('./resource/PalData.csv')
df["Img"] = df['Image'].apply(lambda src: requests.get(src).content)
print("Download complete, Saving . .")
# Save images using the "Name" column as the name
for index, row in df.iterrows():
    name = row['Name']
    img_data = row['Img']
    directory = './resource/images'
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(f'{directory}/{name}.png', 'wb') as f:
        f.write(img_data)
