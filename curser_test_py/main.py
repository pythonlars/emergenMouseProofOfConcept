import json
import numpy as np
import matplotlib.pyplot as plt

with open('2025-12-14_16_40_47_my_iOS_device.json') as f:
    data = json.load(f)

accelerometerX = []
accelerometerY = []
accelerometerZ = []
accelerometerTimeStamps = []
for item in data:
    accX = float(item['accelerometerAccelerationX'])
    accY = float(item['accelerometerAccelerationY'])
    accZ = float(item['accelerometerAccelerationZ'])
    accTimeStamps = float(item['accelerometerTimestamp_sinceReboot'])
    accelerometerX.append(accX)
    accelerometerY.append(accY)
    accelerometerZ.append(accZ)
    accelerometerTimeStamps.append(accTimeStamps)

timeBetweenSamples = []
for i in range(0, len(accelerometerTimeStamps) - 1):
    timeDiff = accelerometerTimeStamps[i+1] - accelerometerTimeStamps[i]
    timeBetweenSamples.append(timeDiff)


print(timeBetweenSamples)
print(accelerometerX)
print(accelerometerY)
print(accelerometerZ)

Velocity_timeX = [0]
Velocity_timeY = [0]

for i in range(len(timeBetweenSamples)):
    Vtx = Velocity_timeX[i] + timeBetweenSamples[i] * accelerometerX[i]
    Velocity_timeX.append(Vtx)

for i in range(len(timeBetweenSamples)):
    Vty = Velocity_timeY[i] + timeBetweenSamples[i] * accelerometerY[i]
    Velocity_timeY.append(Vty)

cordsX = [0]
cordsY = [0]

for i in range(len(timeBetweenSamples)):
    Xtx = cordsX[i] + timeBetweenSamples[i] * Velocity_timeX[i]
    cordsX.append(Xtx)

for i in range(len(timeBetweenSamples)):
    Xty = cordsY[i] + timeBetweenSamples[i] * Velocity_timeY[i]
    cordsY.append(Xty)

plt.plot(cordsY)
plt.show()