#

import json
import os,csv
from os import listdir
from PIL import Image
import cv2

# JSON file
f = open ('input.json', "r")

# Reading from file
data = json.load(f)

print(data)

# Closing file
f.close()
try:
    img1 = Image.open('wafer_image_1.png')
    img2 = Image.open('wafer_image_2.png')
    img3 = Image.open('wafer_image_3.png')
    img4 = Image.open('wafer_image_4.png')
    img5 = Image.open('wafer_image_5.png')
 
    
    width = 800
    length = 600
    pixel1 = list(img1.getdata())
    pixel2 = list(img2.getdata()) 
    pixel3 = list(img3.getdata())
    pixel4 = list(img4.getdata())
    pixel5 = list(img5.getdata())
    #print(pixel1[0])
    #print(pixel2)
    print(len(pixel1))
    print(len(pixel2))
    count = 0
    count1=0
    lst = []
    for i in range(width):
        for j in range(length):                
                if(pixel1[i]!= pixel2[j]):
                     count+=1
                     lst.append([1,i,j])
    print(count)

    for a in range(width):
        for b in range(length):                
                if(pixel1[a]!= pixel3[b]):
                    count1+=1
                    lst.append([2,a,b])

    for a in range(width):
        for b in range(length):                
                if(pixel1[a]!= pixel4[b]):
                    count1+=1
                    lst.append([3,a,b])

    for a in range(width):
        for b in range(length):                
                if(pixel1[a]!= pixel5[b]):
                    count1+=1
                    lst.append([4,a,b])
                            
    for a in range(width):
        for b in range(length):                
                if(pixel2[a]!= pixel5[b]):
                    count1+=1
                    lst.append([5,a,b])
                    
    print(count1)


     
except IOError:
    pass


output_file = "output.csv"
with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(lst)

print(f"Output saved to {output_file}")
