from mpu6050 import mpu6050
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


#sensor
sensor = mpu6050(0x68)

plt.ion()
num = 0
while num<10000:
    accelerometer_data = sensor.get_accel_data()
    print(accelerometer_data)
    
    plt.clf()
    fig = plt.gcf()
    
    ax = fig.gca(projection='3d')  # 获取当前轴
    
    ax.quiver(0,0,0,accelerometer_data['x'],accelerometer_data['y'],accelerometer_data['z'],color='r')
    ax.quiver(0,0,0,0,0,accelerometer_data['z'])
    ax.quiver(0,0,0,0,accelerometer_data['y'],0)
    ax.quiver(0,0,0,accelerometer_data['x'],0,0)
    ax.scatter(accelerometer_data['x'],accelerometer_data['y'],accelerometer_data['z'],color='g')
    
    ax.scatter(0,0,-10,color='b')
    ax.scatter(-10,0,0,color='b')
    ax.scatter(0,10,0,color='b')
    
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-10, 10)
    
    ax.set_zlabel('Z', fontdict={'size': 15, 'color': 'red'})
    ax.set_ylabel('Y', fontdict={'size': 15, 'color': 'red'})
    ax.set_xlabel('X', fontdict={'size': 15, 'color': 'red'})
    
    plt.pause(0.2)     #设置暂停时间，太快图表无法正常显示z'],

plt.ioff()       # 关闭画图的窗口，即关闭交互模式
plt.show()       # 显示图片，防止闪退


