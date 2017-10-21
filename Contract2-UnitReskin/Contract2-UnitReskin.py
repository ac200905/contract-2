import math
import pygame
# initialize pygame and create screen
pygame.init()
screen = pygame.display.set_mode((480, 100))

# func to measure distance between two colors
def Color_Distance(color_one, color_two):
    # variables for getting RGB color values from each of the two colors
    red1 = color_one.r
    blue1 = color_one.b
    green1 = color_one.g
    red2 = color_two.r
    blue2 = color_two.b
    green2 = color_two.g
    # equation to find average of two colors
    distance = math.sqrt((red1-red2)**2+(blue1-blue2)**2+(green1-green2)**2)
    return distance

# func returns True if two colors are sufficiently close (within a certain tolerance)
def Close_Enough(color_one, color_two):
    if Color_Distance(color_one, color_two) < 150.0:
        return True
    else:
        return False

# variable 'pic' assigned to the original image file that contains the four unskinned units
pic = pygame.image.load('Units.png')

# set variables for each color that will be used in later functions
color_unskinned = pygame.Color(255,0,255)
color_red = pygame.Color(255, 0, 0)
color_green = pygame.Color(0, 255, 0)
color_blue = pygame.Color(0, 0, 255)
color_yellow = pygame.Color(255, 255, 0)

# func to reskin units from original unskinned color (magenta) to red
def Unit_Reskin_Red(pic):
    for y in xrange(0, 100):
        for x in xrange(0, 480):
            # extract the color from each pixel at each position (x,y)
            original_color = pic.get_at((x, y))
            # set variable for the color you want to contrast and compare
            color_check = color_unskinned
            # check the color of each pixel against unskinned color (the color that you want to change)
            if Close_Enough(original_color, color_check):
                #if true, change those pixels to a new color
                pic.set_at((x, y), color_red)

# func to reskin units from red to green
def Unit_Reskin_Green(pic):
    for y in xrange(0, 100):
        for x in xrange(0, 480):
            original_color = pic.get_at((x, y))
            color_check = color_red
            if Close_Enough(original_color, color_check):
                pic.set_at((x, y), color_green)

# func to reskin units from green to blue
def Unit_Reskin_Blue(pic):
    for y in xrange(0, 100):
        for x in xrange(0, 480):
            original_color = pic.get_at((x, y))
            color_check = color_green
            if Close_Enough(original_color, color_check):
                pic.set_at((x, y), color_blue)

# func to reskin units from blue to yellow
def Unit_Reskin_Yellow(pic):
    for y in xrange(0, 100):
        for x in xrange(0, 480):
            original_color = pic.get_at((x, y))
            color_check = color_blue
            if Close_Enough(original_color, color_check):
                pic.set_at((x, y), color_yellow)

# func to save each red unit in separate png files
def Save_Red():
    # set var for x axis start position for each unit on the Units.png file
    dist_crop = 0
    # set for loop with range 0-4 to run for each of the 4 units in Units.png file
    for i in xrange(4):
        # set var for separating units in Units.png file
        crop_rect = (dist_crop,0,120,100)
        dist_crop += 120
        # create new subsurface to blit and save as new file
        cropped = pic.subsurface(crop_rect)
        screen.blit(cropped, (0, 0))
        pygame.image.save(cropped,  str(i + 1) + "_Red" + ".png")

# func to save each green unit in separate png files
def Save_Green():
    dist_crop = 0
    for i in xrange(4):
        crop_rect = (dist_crop,0,120,100)
        dist_crop += 120
        cropped = pic.subsurface(crop_rect)
        screen.blit(cropped, (0, 0))
        pygame.image.save(cropped, str(i + 1) + "_Green" + ".png")

# func to save each blue unit in separate png files
def Save_Blue():
    dist_crop = 0
    for i in xrange(4):
        crop_rect = (dist_crop,0,120,100)
        dist_crop += 120
        cropped = pic.subsurface(crop_rect)
        screen.blit(cropped, (0, 0))
        pygame.image.save(cropped, str(i + 1) + "_Blue" + ".png")

# func to save each yellow unit in separate png files
def Save_Yellow():
    dist_crop = 0
    for i in xrange(4):
        crop_rect = (dist_crop,0,120,100)
        dist_crop += 120
        cropped = pic.subsurface(crop_rect)
        screen.blit(cropped, (0, 0))
        pygame.image.save(cropped, str(i + 1) + "_Yellow" + ".png")

# call functions in order to reskin and save files
Unit_Reskin_Red(pic)
Save_Red()
Unit_Reskin_Green(pic)
Save_Green()
Unit_Reskin_Blue(pic)
Save_Blue()
Unit_Reskin_Yellow(pic)
Save_Yellow()
