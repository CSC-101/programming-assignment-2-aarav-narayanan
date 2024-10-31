from typing import Optional

import data


# Write your functions for each part in the space below.

# Part 1
#Purpose of this function is to take two points and create a rectangle with coordinates placed on the top left and bottom right corners
#Inpout are the x and y coordinates and there are two parameters Ex.(2,3) and (5,4)
#Output is the new coordinates with the coordinates being placed into top left and bottom right but as a Rectangle object
#Ex. top left=(2,4) bottom right=(5,3)
def create_rectangle(point1:data.Point, point2:data.Point)->data.Rectangle:
    if point1.x>point2.x: #If statement checks which x coordinate is bigger and whichever is bigger will be the top left coordinate and the other will be the bottom right coordinate
        bottom_right_x=point1.x
        top_left_x=point2.x
    else:  #Same thing as the if statement but now if it is point1.x<=point2.x
        bottom_right_x = point2.x
        top_left_x = point1.x
    if point1.y<point2.y: #If statement checks which y coordinate is smaller and whichever is smaller will be the top left coordinate and the other will be the bottom right coordinate
        top_left_y=point2.y
        bottom_right_y=point1.y
    else:#Same thing as the if statement but now if it is point1.y>=point2.y
        top_left_y=point1.y
        bottom_right_y=point2.y
    return data.Rectangle(data.Point(top_left_x,top_left_y),data.Point(bottom_right_x,bottom_right_y))

# Part 2
#Purpose of the function is to find out if the first time is less than the second time
#Input are the two time parameters which are both in minutes and seconds (3,20) and (4,30)
#Output is the boolean response to show if time 1 is less than time 2  Ex. True
def shorter_duration_than(time1:data.Duration,time2:data.Duration)->bool:
    full_time1=time1.minutes*60+time1.seconds #In order to correctly compare them, the time should be in seconds so convert mintues to seconds and add both of them
    full_time2=time2.minutes*60+time2.seconds
    if full_time1<full_time2:  #If statement to check if time 1 is less than time 2
        return True
    else:
        return False

# Part 3
#Purpose is give out the list of songs that are less than a specified upper bound
# Input is the list of songs from the Song class and the upper bound from Duration class  Ex. [data.Song("Mike","title",data.Duration(3,20)], data.Duration(3,10)
#Output is the list of songs from the data class that is less than the upper bound. Example above []
def song_shorter_than(lst:list[data.Song],upper:data.Duration)->list[data.Song]:
    new_list=[] #Create empty list
    upper=upper.minutes*60+upper.seconds #Convert duration into seconds by multiplying mintutes by 60 and adding it to seconds
    for i in lst: #For loop to check each iteration in the list with data.Song
        duration_i=i.duration.minutes*60+i.duration.seconds #Convert duration into seconds for each iteration
        if duration_i<upper: #If statament to see which duration is less than the upper bounds and append to new_list
            new_list.append(i)
    return new_list

# Part 4
#Purpose of the function is to give the total runtime based on the song list and the list of numbers
#Input would be the list from the SOng class [data.Song("Mike","title",data.Duration(3,20),data.Song("Mike2","title2",data.Duration(4,30)]
#ANother input would be the list of numbers that would be used to add up the duration [0,1,0]
#Output is the total time given as a duration class  Ex. Duration(11,10)
def running_time(lst:list[data.Song],number:list[int])->data.Duration:
    minutes=0
    seconds=0  #Start off both minutes and seconds as 0
    for idx in number:
        #For loop checks every interation in the list and computes what below
        if 0 <= idx < len(lst): #check if idx is >=0 and less than length of list and take out negative song numbers
            runtime=lst[idx].duration  #Used to find the duration aspect of the list since that is what we need
            minutes=minutes+runtime.minutes  #Add up the minutes from the previous one and the current one and the same goes for the seconds one
            seconds=seconds+runtime.seconds
    total_minutes=minutes+seconds//60  #Add up the total minutes by adding the minutes and the seconds divided by 60 as an integer.
    total_seconds=seconds%60 #Total seconds would be the remainder of the seconds that was divided by 60
    return data.Duration(total_minutes,total_seconds)

# Part 5
# Purpose: To find a connection or a link between them with a nest list containing cities and the other list having the names to see if there is connection in the previous list.
#Input is the listy with cities like [["citya","cityb"],["cityb","cityc"]] and the names list ["citya","cityc"]
#Output is to give a boolean response if the names list is within the nested list.  Ex. False
def validate_route(city:list[list[str]], names:list[str])->bool:
    if len(names)<=1: #If statement to show only 1 value or an empty list and whatever it is it will return true.
        return True
    for i in range(1,len(names)): #A for loop to check each iteration within the range from 1 to length of names list
        link=False #Start off with false
        for connection in city: #For loop to check the city list
            if names[i] in connection and names[i-1] in connection: #If statement to see iif the names[i] and names[i-1] is in connection
                link=True
        if not link: #To show if link isn't true then it will show false
            return False
    return True

# Part 6
#Purpose is to give the starting index of the longest contiguous repetition of a single number
#Input is the list of numbers Ex. [1,2,3,3,3,3,4,5]
#Output is the index number that starts off the longest contiguous repetition Ex. 2
def longest_repetition(num:list[int])->Optional[int]:
    if len(num)==0: #If there is an empty list then it should return none
        return None
    beg_idx=0  #Start it off with 0 for the beginning list
    long_length=1 #Length to be updated within the loop
    max_length=1  #1 is the minimum and that would currently be the max andit would be updated later
    for i in range(1,len(num)): #For loop to go within the range of the list of num and start it from one.
        if num[i]==num[i-1]:  #Check if the first iteration and the previous iteration integers are the same
            long_length+=1 #Update the long list
        else:
            long_length=1 #If not the same long_length goes back to 1.
        if long_length>max_length: #Statement used to update the max_length variable is long_length is more than the max_length.
            max_length=long_length #Convert max_length into making it the same as long_length
            beg_idx=i-max_length+1  #Find the idx by subtracting the iteration to the max_length and add it by 1 since the range started from 1.
    return beg_idx




