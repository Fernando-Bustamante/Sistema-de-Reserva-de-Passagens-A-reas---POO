# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 07:19:58 2024

@author: Eduardo
"""
import abc as abc
 
class aviao(abc.ABC):
    
    @abc.abstractclassmethod
    def on_seat_click(self, row:int, col_title:str) -> None:
        pass
    
    @abc.abstractclassmethod
    def create_plane_widget(self):
        pass
    
    @abc.abstractclassmethod
    def destroy_plane_widget(self):
        pass