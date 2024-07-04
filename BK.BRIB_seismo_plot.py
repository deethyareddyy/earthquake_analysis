import matplotlib.pyplot as plt
import numpy as np

data = open("BK.BRIB_seismo.txt")

time = []
mag = []
lat = []
long = []
depth = []

for i in range (540):
    s = data.readline()
    p = s.split()
    if (p[1] in time):
        continue
    else:
        time.append(p[1])
        mag.append(float(p[2]))
        lat.append(float(p[3]))
        long.append(float(p[4]))
        depth.append(float(p[5]))

# plt.subplot(1,1,1)
plt.plot(time, mag, marker = 'o', color = '#DC143C', label = 'Magnitude (Richter scale)') #red
# plt.subplot(1,1,2)
plt.plot(time, lat, marker = 'o', color = '#6495ED', label = 'Latitude (degrees)') #blue
# plt.subplot(1,1,3)
plt.plot(time, long, marker = 'o', color = '#B8860B', label = 'Longitude (degrees)') #yellow
# plt.subplot(1,1,4)
plt.plot(time, depth, marker = 'o', color = '#3CB371', label = 'Depth (km)') #green
plt.title("BK.BRIB / 37.91886 / -122.15179")
plt.xlabel("Time")
plt.legend()
plt.show()
