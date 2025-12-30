from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#Open the image and make sure it has 3 colors (RGB)
img = Image.open('Sample.png').convert('RGB') 

#Convert the image into a numbers array (Matrix)
res = np.asarray(img)
print(f"Shape of array: {res.shape}")
colors = ("red", "green", "blue")

#Set up the graph (Title and Labels)
plt.figure(figsize=(10, 6))
plt.title("RGB Histogram")
plt.xlabel("Color Value (0-255)")
plt.ylabel("Number of Pixels")

#alculate data for each color
for i, color in enumerate(colors):
    channel_data = res[:, :, i]
    counts, bins = np.histogram(channel_data.ravel(), bins=256, range=(0, 256))
    plt.plot(bins[:-1], counts, color=color, label=color)

#Show the legend and the final result
plt.legend()
plt.grid(alpha=0.3)
plt.show()