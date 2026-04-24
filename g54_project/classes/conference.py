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
        
        
        Conference.obj[self._id] = self
        Conference.lst.append(self._id)

    
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
    def date (self):
        return self._date
    
    @date.setter
    def date (self, date):
        self._date = date
        
               
        
# c1 = Conference(1,"AI Conference 2025","2025-06-15","Evento sobre inteligência artificial")
# c2 = Conference(2,"Data Science Summit","2025-09-20","Conferência sobre análise de dados")

# print("ID:", c1.id)
# print("Título:", c1.title)
# print("Comentários:", c1.comments)
# print("Data:", c1._date)

# print()

# print("ID:", c2.id)
# print("Título:", c2.title)
# print("Comentários:", c2.comments)
# print("Data:", c2._date)

# print()

# c1.title = "AI Global Conference 2025"
# c1.comments = "Evento internacional de IA"

# print("Após alteração:")
# print("Novo título:", c1.title)
# print("Novos comentários:", c1.comments)

# print()

# print("Objetos guardados em Conference.obj:")
# print(Conference.obj)

# print()

# print("Lista de IDs:")
# print(Conference.lst)
         
     


     