# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:00:29 2026

@author: up202505000
"""
from gclass import Gclass
import datetime

class Conference(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att = ['_id','_title','_date','_comments']
    header = 'Conference'
    desc = ['Id','Title', 'Date','Comments']

    def __init__(self, id, title, date, comments):
        super().__init__()
        self._id = int(id)
        self._title = title
        self._date = datetime.date.fromisoformat(date)
        self._comments = comments
        
        
        Conference.obj[id] = self
        Conference.lst.append(id)

    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title
         
    @property
    def comments(self):
        return self._comments

    @comments.setter
    def comments(self, comments):
        self._comments = comments
    
    @property
    def comments(self):
        return self._comments
    
    @comments.setter
    def comments(self, comments):
        self._comments = comments
         
   
       


     