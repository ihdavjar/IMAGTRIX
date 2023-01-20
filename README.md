# IMAGTRIX
A program that can predict the weather by diagnosing images taken by it using artificial intelligence and give prior warning to the driver about the weather conditions on the road ahead. ​

# Introduction:-
## Problem:
Weather conditions on different parts of the road are different, Hence it is really important to keep caution while entering a part of road which has fog, rain etc. Normally the speed limits boards are static and hence they may not be appropriate for different weather conditions. Hence we decided to make this device which will basically provide a speed limit based on different weather conditions before the drivers enter that region.

## Aim:
To make a device that can predict the weather by diagnosing images taken by it using artificial intelligence and give prior warning to the driver about the weather conditions on the road ahead. ​

# Basic model of the complete device:
![Model_3](https://user-images.githubusercontent.com/95899338/213619782-a398e2b6-5815-458e-9501-e2c32ca1ff6d.jpg)
![Model_1](https://user-images.githubusercontent.com/95899338/213619774-0526c637-4723-4ecc-b595-93993f7064d3.png)
![Model_2](https://user-images.githubusercontent.com/95899338/213619799-7e2bd620-d256-4432-a2b5-b8e4441359e2.png)

# Basic Principle involved: 
- Device takes images to predict the weather by using grayscale method and colorful image methods. 
- This is trained using data sets of different images of different weather conditions. 
- After the module is trained it can compare the input image received from the camera module.  
- The image clicked by the camera will not be stored, will be directly input into the code and will be deleted once output is received hence reducing the space required. 
- After we input an image into the program it will list down the similarity percentage with each of the image in the data set  
- Then the Output will be shown on matrix display in such a way that if fog score is high, then it will display (“Fog ahead go slow”) and in similar fashion for others
