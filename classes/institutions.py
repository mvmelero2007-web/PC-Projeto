# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:45:38 2026

@author: up202505000
"""

from gclass import Gclass
import datetime   

class Institutions(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and called 'id'
    att = ['_id','_created_date','_name']
    # Class header title
    header = 'Institutions'
    # field header for use in, for example, input form
    desc = ['Id','Created_Date','Name']
    # Constructor. Called when an object is instantiated
    def __init__(self, id, created_date, name):
        super().__init__()
        # Object attributes
        self._id = int(id)
        self._created_date = datetime.date.fromisoformat(created_date)
        self._name = name
        
        # Add the new object to the dictionary of objects
        Institutions.obj[id] = self
        # Add the id to the list of object ids
        Institutions.lst.append(id)

    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    
    @property
    def created_date(self):
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        self._created_date = created_date

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
        
        
    