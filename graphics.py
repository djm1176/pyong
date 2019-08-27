# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 10:45:40 2019

@author: djm1176
"""

import pygame
import gameobject
from pygame.math import Vector2
from gameobject import GameObject
import utils

class Camera(GameObject):
    
    def __init__(self):        
        super().__init__()
        
    def render(self, display):
        for obj in gameobject.getObjectsOfType(GameObject):
            #Exclude any types that shouldn't be rendered
            if obj.__class__ in [Camera]: continue
            if obj.visible:
                #Reorient position (pygame renders topleft to bottomright)
                new_pos = (obj.position.x, display.get_height() - obj.position.y - obj.scale.y)
                
                #Call a basic render function for GameObject, or custom implementation for all other inherited classes
                #Note: All classes that inherit GameObject MUST implement render, even if it just does the same basic implementation
                if type(obj) == GameObject:
                    display.blit(obj.getSprite(), new_pos)
                else:
                    obj.render(display, new_pos)
                    
    def testRender(self, display):
        display.blit(self._sprite, (0, 0))