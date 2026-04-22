# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:07:25 2026

@author: up202505000
"""

from gclass import Gclass
from researcher import Researcher
from conference import Conference

class Registration(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att = ['_id','_researcher_id','_conference_id','_fee','_attendance_status']
    header = 'Registration'
    des = ['Id','Researcher_id','Conference_id','Fee','Attendance_status']
   
    def __init__(self, id, researcher_id, conference_id, fee, attendance_status):
        super().__init__()
        researcher_id = int(researcher_id)
        conference_id = int(conference_id)
        
        if researcher_id in Researcher.lst:
            if conference_id in Conference.lst:
                id = Registration.get_id(id)
                
                self._fee = float(fee)
                self._id  = int(id)
                self._attendance_status = attendance_status
                self._researcher_id = int(researcher_id)
                self._conference_id = int(conference_id)
          
                Registration.obj[id] = self
                Registration.lst.append(id)
            else:
                print('Conference ', conference_id, ' not found')
        else:
            print('Researcher ', researcher_id, ' not found')
   

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id
        
    @property
    def fee (self):
        return self._fee 
    @fee.setter
    def fee (self,fee):
        self._fee = fee 
        
    @property
    def researcher_id(self):
        return self._researcher_id
    
    @researcher_id.setter
    def researcher_id(self,researcher_id):
        self._researcher_id = researcher_id
 
    @property
    def conference_id(self):
        return self._conference_id
   
    @conference_id.setter
    def conference_id(self, conference_id):
        self._conference_id = conference_id
        
   

        