#!/usr/bin/env python3

from enum import EnumMeta
from lidar_ros_task.srv import lidar, lidarResponse
import sys
import rospy 
import PIL
from PIL import Image, ImageDraw
import math

new_map = PIL.Image.new(mode = '1', size = (400, 400))

#function to move bot around the map
def move_bot():
    pass

#function to create the map from scans
def create_map(centerX, centerY, lidar_scan_readings, map):
    
    for values in lidar_scan_readings:
        i = values[0]
        r = values[1]

        x_pos = int(i*math.cos(i*math.pi/180) + centerX)
        y_pos = int(i*math.sin(i*math.pi/180) + centerY)

        map_pixels = map.load()
        map_pixels[x_pos, y_pos] = 0  



#Let's hope this part works, fingers crossed lol :)
def lidar_clien_func (x, y):
    rospy.wait_for_service('scan')

    try:
        scan_data = rospy.ServiceProxy('scan', lidar)
        resp1 = scan_data(x, y)
        scan_values = []
        for i, j in enumerate(resp1.lidar_array):
            if (i%2 == 0):
                scan_values.append((resp1.lidar_array[i-1],j))
        return scan_values


    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x, y]"%sys.argv[0]



if __name__ == "__main__":
    
    if len(sys.argv) == 3:
        x = int (sys.argv[1])
        y = int (sys.argv[2])
    
    else:
        print(usage())
        sys.exit(1)
    #Enter execution code here
    create_map(399, 0, lidar_clien_func(0, 399), new_map)
    new_map.save("new_map.jpg")  

