# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 10:09:29 2019

@author: djm1176
"""

#config imports sys and other necessary classes for checking 
from config import *


if __name__ == "__main__":
    print("Cannot run this file in this context")
    sys.exit(1)

import pygame
import utils
from pygame.math import Vector2



gameobjects = []
idCounter = 0

"""
Base class for any object on screen. Contains a name and position/scale, as well as basic manipulation functions.
Graphics should be a separate class that derives from GameObject
"""
class GameObject:

    
    def __init__(self, name = "New GameObject", position = Vector2(0,0), scale = Vector2(32, 32)):
        self.id = takeId()
        self.name = name
        #Sets the position or attempts to cast to Vector2 if not already
        self.position = position if type(position) == Vector2 else Vector2(position)
        #Defaults to a 32x32 pixel scale. Will also try to cast
        self.scale = scale if type(scale) == Vector2 else Vector2(scale)
        self.visible = True
        self.sprite = None
        self.color = None #Used mainly for debugging or testing; sprites should normally be used
        
        insertObject(self) #Places this object into the list of all objects
        
    def __repr_(self):
        return self.name
    
    def colorize(self, color):
        self.sprite = pygame.Surface(self.scale)
        self.sprite.fill(color)
    
    #Sets the position of the objects. X can be substituted with a Vector2
    def setPosition(self, x, y = None):
        if type(x) == Vector2:
            self.position = x
        elif type(x) in [tuple, list, set]:
            self.position = Vector2(x)
        else:
            self.position = Vector2(x, y)
            
    def movePosition(self, dx, dy = None):
        if type(dx) == Vector2:
            self.position += dx
        elif type(dx) in [tuple, list, set]:
            self.position += Vector2(dx)
        else:
            self.position += Vector2(dx, dy)
            
    def getSprite(self):
        return self.sprite
            
    def render(self, display, position):
        """Render method is abstract and should be implemented by classes that derive from GameObject"""
        raise NotImplementedError('Render method for type \'' + type(self).__name__ + '\' must be implemented since it derives from GameObject')


"""
Object which has physics interactions
"""
class Entity(GameObject):
    def __init__(self, position = Vector2(0,0), scale = Vector2(32, 32), static = True, collisions = True, velocity = Vector2(0, 0)):
        super().__init__("New Entity", position, scale)
        self.static = static
        self.collisions = collisions
        self.velocity = velocity
        self.collisionCallbacks = [] #Call these functions on collision
        
    def render(self, display, position):
        display.blit(self.getSprite(), position)
        
    def __repr__(self):
        return "[Entity] '"  + self.name + "'"
    
    

#Static gameobject functions

def takeId():
    global idCounter
    idCounter += 1
    return idCounter - 1


"""
    Returns a list of all objects matching type classType or its inherited classes
"""
def getObjectsOfType(classType = GameObject):
    if classType == GameObject:
        return gameobjects
    return [item for item in gameobjects if classType in item.__class__.mro()]

"""Inserts a GameObject into the scene."""
def insertObject(obj):
    if not GameObject in obj.__class__.mro():
        raise TypeError('The object passed must inherit GameObject')
    
    global gameobjects
    #Get the index of the next highest value
    #Change 'x.id' to search by a different value other than the z depth
    i = utils.binarySearch([x.id for x in gameobjects], obj.id, 0, len(gameobjects) - 1)
    gameobjects = gameobjects[:i] + [obj] + gameobjects[i:]
    
def removeObject(obj):
    global gameobjects
    gameobjects.remove(obj)
    del obj

