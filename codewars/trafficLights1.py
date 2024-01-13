# Traffic light simulation 
#
# A character string represents a city road.
# Cars travel on the road obeying the traffic lights.
# Legend: . = Road, C = Car, G/O/R = Green, orange, red traffic light
# Example: "C...R............G......"
# Rules:
#   At each iteration:
#       the lights change, according to the traffic light rules...
#       then the car moves, obeying the car rules
#   Traffic Light Rules
#       Traffic lights change colour as follows:
#       GREEN for 5 time units... then
#       ORANGE for 1 time unit... then
#       RED for 5 time units....
#       ... and repeat the cycle
#   Car Rules
#       Cars travel left to right on the road, moving 1 character position per time unit
#       Cars can move freely until they come to a traffic light. Then:
#       if the light is GREEN they can move forward (temporarily occupying the same cell as the light)
#       if the light is ORANGE then they must stop (if they have already entered the intersection they can continue through)
#       if the light is RED the car must stop until the light turns GREEN again
#
# Task:
# Given the initial state of the road and simulation time, return the states for all iterations of the simiulation
# Source: https://www.codewars.com/kata/5d0ae91acac0a50232e8a547/python
# 
#
# Version 1: This version passes all of the tests on Codewars.
# However by the codewars test requirements the car can never end up on an orange light.
# To pass all the tests, had to make the behavior as follows: 
# If the light is about to turn orange (from green) in the next iteration the car
# stays put, even though the light is still green in the current iteration. (line 215)
# For a version where the car can end up on an orange light (cover up the orange light),
# see trafficLights2.py

  
  
class TrafficLight():
    '''A class to model a traffic light'''
    def __init__(self):
        """Initialize attributes describing the traffic light."""
        self.color = ""
        self.time_count = 0
        self.is_occupied = False
    
    def setColor(self, newcolor):
        # newcolor is a character, either G, R or O
        self.color = newcolor
        
    def getColor(self):
        return self.color
    
    def incrementTime(self):
        self.time_count += 1
    
    def resetTime(self):
        self.time_count = 0
        
    # does the same thing as getColor
    def show(self):
        return self.color


class Asphalt():
    '''A class to model asphalt'''
    def __init__(self, appearance="."):
        self.appearance = appearance        
        self.is_occupied = False
    
    def show(self):
        return self.appearance


# turn the road string into a list
def makeRoadObj(roadstr):
    roadObj = []
    for i in roadstr:
        if i==".":
            i=Asphalt()
            roadObj.append(i)
        elif i=="G":
            i=TrafficLight()
            i.setColor("G")
            roadObj.append(i)
        elif i=="R":
            i=TrafficLight()
            i.setColor("R")
            roadObj.append(i)
        elif i=="O":
            i=TrafficLight()
            i.setColor("O")
            roadObj.append(i)
        elif i=="C":
            i=Asphalt()
            i.is_occupied=True
            roadObj.append(i)
    return roadObj


# move car by one increment
# if car is in last position, move car off of road (make last position unoccupied 
# without occupying the next position)
def moveCar(road):
    for i in road:
        # case last position in road
        if road.index(i)==-1 or road.index(i) == len(road)-1:
            road[-1].is_occupied = False
        else:
            if i.is_occupied == True:
                i.is_occupied = False
                road[road.index(i)+1].is_occupied = True
                break
            elif i.is_occupied == False:
                pass


# Display the road. For unoccupied positions, print the character in that 
# position (asphalt or traffic light). For an occupied position, the car covers 
# the character so print the car (C). 
# (didn't end up using this in the final version)
def displayRoad(r):
    for i in r:
        if i.is_occupied == False:
            print(i.show(), end="")
        elif i.is_occupied == True:
            print("C", end="")
            

# turn the road list back into a string
# similar to displayRoad(r), but returns the road in string form rather than printing it
def makeRoadStr(r):
    roadstr = ""
    for i in r:
        if i.is_occupied == False:
            roadstr = roadstr + i.show()
        elif i.is_occupied == True:
            roadstr = roadstr + "C"
    return roadstr


# cycle through the traffic light colors according to the traffic light rules
def cycleTrafficLight(light):
    # case green light
    if light.getColor()=="G" and light.time_count<=4:
        pass
    if light.getColor()=="G" and light.time_count==5:
        light.setColor("O")
        light.resetTime()
    # case orange light
    if light.getColor()=="O" and light.time_count==0:
        pass
    if light.getColor()=="O" and light.time_count>=1:
        light.setColor("R")
        light.resetTime()
    # case red light    
    if light.getColor()=="R" and light.time_count<=4:
        pass
    if light.getColor()=="R" and light.time_count==5:
        light.setColor("G")
        light.resetTime()
    light.incrementTime()


# get positions of all traffic lights on the road
def getTrafficLightIndices(r):
    indices = []
    for i in r:
        if isinstance(i,TrafficLight):
            indices.append(r.index(i))
        else:
            pass
    return indices


# for road with multiple cars (not used here)
def getCarIndices(r):
    indices = []
    for i in r:
        if i.is_occupied == True:
            indices.append(r.index(i))
        else:
            pass
    return indices


# get position of car on road
def getCarIndex(r):
    for i in r:
        if i.is_occupied == True:
            return r.index(i)
        else:
            pass


# move the car depending on its relation to traffic lights and increment the traffic lights
def updateRoad(road, lights):
    # get car position for the current state of the road
    carpos = getCarIndex(road)
    # cases for car
    # if no car on road, do nothing
    if carpos == None:
        pass
    # if car is in last position, move car off the road
    elif carpos == len(road)-1:
        moveCar(road)
    else:
        # 1 current pos asphalt, next pos asphalt
        if isinstance(road[carpos], Asphalt) and isinstance(road[carpos+1], Asphalt):
            moveCar(road)
        # 2 current pos asphalt, next pos traffic light
        elif isinstance(road[carpos], Asphalt) and isinstance(road[carpos+1], TrafficLight):
            if road[carpos+1].color=="G":
                if road[carpos+1].time_count <= 4:
                    moveCar(road)
                elif road[carpos+1].time_count == 5:
                    pass
            elif road[carpos+1].color == "O":  
                pass
            elif road[carpos+1].color == "R":  
                if road[carpos+1].time_count <= 4:
                    pass
                elif road[carpos+1].time_count == 5:
                    moveCar(road)
        # 3 current pos traffic light, next pos asphalt
        elif isinstance(road[carpos], TrafficLight) and isinstance(road[carpos+1], Asphalt):
            if road[carpos].color == "G":
                moveCar(road)
            elif road[carpos].color == "O":
                moveCar(road)
            elif road[carpos].color=="R":  
                pass 
        # 4 current pos and next pos are traffic lights
        elif isinstance(road[carpos], TrafficLight) and isinstance(road[carpos+1], TrafficLight):
            if road[carpos].color=="G" and road[carpos+1].color=="G" or road[carpos].color=="O" and road[carpos+1].color=="G": 
                moveCar(road)
            else:
                pass
    # cycle traffic lights in every iteration
    for light in lights:
        cycleTrafficLight(road[light])
    return road


# bring everything together; place all of the road states in an array (as strings)
def traffic_lights(r, t):
    roadStateArray = [r]
    roadObj = makeRoadObj(r)
    lights = getTrafficLightIndices(roadObj)
    for light in lights:
        cycleTrafficLight(roadObj[light])    
    for i in range(t):
        roadObj = updateRoad(roadObj, lights)
        roadStateArray.append(makeRoadStr(roadObj))
    return roadStateArray


#r1 = "C...R............G......"
r1 = "C...G............G......"
t1 = 15

rsa1 = traffic_lights(r1, t1)
state_num = len(rsa1)
for num in range(state_num):
    if num <= 9:
        print(str(num) + "   " + rsa1[num])
    else:
        print(str(num) + "  " + rsa1[num])

            

# car cases: 
# consider car's current position and next position concurrently.
# 1 current position is asphalt and next position is asphalt: 
      # move car
# 2 current position is asphalt and next position is light: 
      # if light is green: move car
      # if light is red or orange: pass
# 3 current position is light and next position is asphalt:
      # if light is green or orange: move car
      # if light is red: pass
# 4 current position is light and next position is light:
      # possibilities: (G,R) (G,O) (G,G) (O,R) (O,O) (O,G)
      # move: (G,G) or (O,G)
      # else don't move 
          

