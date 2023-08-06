from pyEngine2D_ddd.game_object import GameObject
from itertools import combinations
import math
import pygame

class CollisionHandler():
    """Top level class to hold main methods and attributes for colliders. 
    Each child class will contain methods to determine if two game objects are touching."""
    ALL_COLLIDERS = []
    def __init__(self, game_object):
        self.MULTIPLE_INSTANCES = False
        self.prev_colliders = ["a", "b", "c"]
        self.game_object = game_object
        self.smallest_vertex = [[0,0], [1,1]]
        self.l1 = [[0,0], [1,1]]
        self.l2 = [[0,0], [1,1]]
    def start(self):
        self.colliderPairs = list(combinations(CollisionHandler.ALL_COLLIDERS, 2))

    def fixed_update(self):
        if CollisionHandler.ALL_COLLIDERS != self.prev_colliders:
            self.colliderPairs = list(combinations(CollisionHandler.ALL_COLLIDERS, 2))
            self.prev_colliders = CollisionHandler.ALL_COLLIDERS
        
        for i in self.colliderPairs:
            # line = [i[0].collider_transform, i[1].collider_transform]
            vertex = self._get_axis(i)
            self.l1 = [i[0].collider_transform, vertex[0]]
            self.l2 = [i[1].collider_transform, vertex[1]]
            line1 = self.l1[0]
            line2 = self.l2[0]
            colliding = True
            for z in range(i[0].axis_amount + i[1].axis_amount):
                if not ((line2[0] <= line1[1] and line2[0] >=line1[1]) or (line1[0] <=line2[1] and line1[1] >= line2[0])):
                    colliding = False



        '''
        get closest vertexes
        draw line from center to vertex
        for each axis:
            flatten line to that axis 
            check for overlaps for the lines 
            if yes then break:
                collision
            else:
                keep going    
            
        '''
    def update(self):
        self.draw_collider()

    def _get_axis(self, colliders):
        self.smallest_dist = 999999999999
        for vertex in colliders[0].verticies:
            for vertex2 in colliders[1].verticies:
                dist = math.sqrt(((vertex[0] - vertex2[0])**2) + ((vertex[1] - vertex2[1])**2))
                if dist < self.smallest_dist:
                    self.smallest_dist = dist
                    self.smallest_vertex = [vertex, vertex2]
        return self.smallest_vertex

                    
    def draw_collider(self, color=(0,0,0)):
        for object in CollisionHandler.ALL_COLLIDERS:
            collider = pygame.Surface(object.collider_size).convert_alpha()
            collider = pygame.transform.rotate(collider, object.game_object.Transform.rotation)
            object_transform = collider.get_rect(
		    	center = object.game_object.Transform.center)
            self.game_object.screen.screen.blit(collider, object_transform)

            for v in object.get_verticies():
                pygame.draw.circle(object.game_object.screen.screen, (255,255,0), v, 3)
            for x in self.smallest_vertex:
                pygame.draw.circle(self.game_object.screen.screen, (255,0,0), x, 3)
            pygame.draw.line(self.game_object.screen.screen, (0,0,255), self.l1[0], self.l1[1])
            pygame.draw.line(self.game_object.screen.screen, (0,0,255), self.l2[0], self.l2[1])
            pass
        
        


class RectangleCollider2D():
    def __init__(self, game_object):
        self.MULTIPLE_INSTANCES = True
        self.game_object = game_object
        self.is_trigger = False
        self.top_left = []
        self.top_right = []
        self.bottom_left = []
        self.bottom_right = []
        CollisionHandler.ALL_COLLIDERS.append(self)
        self.collider_transform = [self.game_object.Transform.transform[0], self.game_object.Transform.transform[1]]
        self.collider_transform_prev = [0,0]
        self.collider_size = [0,0]
        self.collider_size_prev = [-1,-1]
        self.collider_size_orig = [0,0]
        self.rotation_prev = 1000
        self.prev_t_scale = [-1,-1]
        self.axis_amount = 2

    def start(self):
        self.fixed_update()

    def _is_update(self):
        if self.collider_size == self.collider_size_prev:
            if self.collider_transform == self.collider_transform_prev:
                if self.game_object.Transform.scale == self.prev_t_scale:
                    if self.rotation_prev == self.game_object.Transform.rotation:   
                        return False
        return True  


    def fixed_update(self):
        self.collider_transform = [self.game_object.Transform.transform[0], self.game_object.Transform.transform[1]]
        if self._is_update():
            self.collider_size[0] = self.collider_size_orig[0] * self.game_object.Transform.scale[0]
            self.collider_size[1] = self.collider_size_orig[1] * self.game_object.Transform.scale[1]
            self.collider_transform_prev = self.collider_transform
            self.collider_size_prev = self.collider_size
            self.prev_t_scale = self.game_object.Transform.scale
            self.rotation_prev = self.game_object.Transform.rotation
            self.verticies = self.get_verticies()
  
    def get_verticies(self):
        """returns vertecies of the collider using the center point and width -
        [topleft, topright, bottomleft, bottomright]"""
        vertex = [0,1,2,3]
        rot_x = [0,1,2,3]
        rot_y = [0,1,2,3]
        
        cos_rot = math.cos(math.radians(-self.game_object.Transform.rotation))
        sin_rot = math.sin(math.radians(-self.game_object.Transform.rotation))

        rot_x[0] = (self.collider_size[0]/2) * cos_rot - (self.collider_size[1]/2) * sin_rot
        rot_x[1] = (self.collider_size[0]/2) * cos_rot - (-self.collider_size[1]/2) * sin_rot
        rot_x[2] = (-self.collider_size[0]/2) * cos_rot - (self.collider_size[1]/2) * sin_rot
        rot_x[3] = (-self.collider_size[0]/2) * cos_rot - (-self.collider_size[1]/2) * sin_rot
       
        rot_y[0] = (self.collider_size[1]/2) * sin_rot + (self.collider_size[0]/2) * cos_rot
        rot_y[1] = (self.collider_size[1]/2) * sin_rot + (-self.collider_size[0]/2) * cos_rot
        rot_y[2] = (-self.collider_size[1]/2) * sin_rot + (self.collider_size[0]/2) * cos_rot
        rot_y[3] = (-self.collider_size[1]/2) * sin_rot + (-self.collider_size[0]/2) * cos_rot
        
        vertex[0] = [self.collider_transform[0] + rot_x[0], self.collider_transform[1] + rot_y[0]]
        vertex[1] = [self.collider_transform[0] + rot_x[1], self.collider_transform[1] + rot_y[1]]
        vertex[2] = [self.collider_transform[0] + rot_x[2], self.collider_transform[1] + rot_y[2]]
        vertex[3] = [self.collider_transform[0] + rot_x[3], self.collider_transform[1] + rot_y[3]]
        return vertex
        

    def set_collider_size(self, size):
        self.collider_size_orig = size
    
    def _get_final_cords(self, xy):
        rot = math.degrees(self.game_object.Transform.rotation)
        Rx = self.collider_transform[0] + (xy[0]  * math.cos(rot)) - (xy[1] * math.sin(rot))
        Ry = self.collider_transform[1] + (xy[0]  * math.sin(rot)) + (xy[1] * math.cos(rot))
        return [Rx, Ry]      


    
# class CircleCollider2D():
#     def __init__(self, game_object):
#         self.game_object = game_object
#         self.is_trigger = False
#         self.collider_type = ""
#         super().__init__(self, game_object)
#         CollisionHandler.ALL_COLLIDERS.append(self)
#         self.collider_transform = [self.game_object.Transform.transform[0], self.game_object.Transform.transform[1]]
#         self.collider_size = [self.game_object.Transform.final_scale[0], self.game_object.Transform.final_scale[1]]
#         self.scale = [1,1,1,1] #[top, bottom, right, left]
    

#     def fixed_update(self):
#         if self.collider_size != self.collider_size_prev or self.collider_transform != self.collider_transform_prev:
#             self.center = self.collider_transform
#             self.collider_transform_prev = self.collider_transform
#             self.collider_size_prev = self.collider_size


# class SpriteColliderConvexPoly2D():
#     def get_verticies(self):
#         return self.verticies


'''
transform.x + 1/2 size.x = x for top 
transform.x - 1/2 size.x = x for bottom 
transform.y + 1/2 size.y = y for right
transform.y - 1/2 size.y = y for left

'''

#https://www.jkh.me/files/tutorials/Separating%20Axis%20Theorem%20for%20Oriented%20Bounding%20Boxes.pdf#:~:text=In%202D%20space%2C%20the%20Separating%20Axis%20Theorem%20states,A%20and%20rectangle%20B%20in%20the%20illustration%20below.


'''
PA = coordinate position of the center of rectangle A
Ax = unit vector representing the local x-axis of A
Ay = unit vector representing the local y-axis of A
WA = half width of A (corresponds with the local x-axis of A)
HA = half height of A (corresponds with the local y-axis of A)
PB = coordinate position of the center of rectangle B
Bx = unit vector representing the local x-axis of B
By = unit vector representing the local y-axis of B
WB = half width of B (corresponds with the local x-axis of B)
HB = half height of B (corresponds with the local y-axis of B)


Let
T = PB – PA
L = an arbitrary axis (i.e. a unit vector)
Proj ( v ) = v • L = projection of v onto an axis, L
Then a separating axis, L, exists if and only if
|Proj ( T )| > ½|Proj ( RectangleA )| + ½|Proj ( RectangleB )|
which is equivalent to
|Proj ( T )| > |Proj ( WA*Ax )| + |Proj ( HA*Ay )| + |Proj ( WB*Bx )| + |Proj( HB*By )|
which is equivalent to
| T • L | > | ( WA*Ax ) • L | + | ( HA*Ay ) • L | + | ( WB*Bx ) • L | + |( HB*By ) • L |
where | s | denotes the absolute value of scalar s
'''


#potential efficiency: only check collisions for moving objects and make pairs a set not a list 