# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:56:45 2026

@author: up202505000
"""


from gclass import Gclass

class Researcher(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and called 'id'
    att = ['_id','_name','_comments']
    # Class header title
    header = 'Researcher'
    # field header for use in, for example, input form
    desc = ['Id','Name','Comments']
    # Constructor. Called when an object is instantiated
    def __init__(self, id, name, comments):
        super().__init__()
        # Object attributes
        self._id = int(id)
        self._name = name
        self._comments = comments
        
        # Add the new object to the dictionary of objects
        Researcher.obj[id] = self
        # Add the id to the list of object ids
        Researcher.lst.append(id)

    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
         
    @property
    def comments(self):
        return self._comments

    @comments.setter
    def comments(self, comments):
        self._comments = comments

   
        