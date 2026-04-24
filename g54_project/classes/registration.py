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
    desc = ['Id','Researcher_id','Conference_id','Fee','Attendance_status']
   
    def __init__(self, id, researcher_id, conference_id, fee, attendance_status):
        super().__init__()
        researcher_id = int(researcher_id)
        conference_id = int(conference_id)
        
        if researcher_id in Researcher.lst:
            if conference_id in Conference.lst:
                # id = Registration.get_id(id)
                
                self._fee = float(fee)
                self._id  = int(id)
                self._attendance_status = attendance_status
                self._researcher_id = int(researcher_id)
                self._conference_id = int(conference_id)
          
                Registration.obj[self._id] = self
                Registration.lst.append(self._id)
            else:
                print('Conference ', conference_id, ' not found')
        else:
            print('Researcher ', researcher_id, ' not found')
   

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, novo):
        self._id = novo
        
    @property
    def fee (self):
        return self._fee 
    
    @fee.setter
    def fee (self,novo):
        self._fee = novo 
        
    @property
    def researcher_id(self):
        return self._researcher_id
    
    @researcher_id.setter
    def researcher_id(self,novo):
        self._researcher_id = novo
 
    @property
    def conference_id(self):
        return self._conference_id
   
    @conference_id.setter
    def conference_id(self, novo):
        self._conference_id = novo
        
    @property
    def attendance_status (self):
        return self._attendance_status 

    @attendance_status.setter  
    def attendance_status (self, novo):
        self._attendance_status = novo
        


# res1 = Researcher(101, "João Silva", "Comentário A")
# res2 = Researcher(102, "Maria Santos", "Comentário B")

# conf1 = Conference(500, "Workshop Python", "2025-05-10", "Tech")
# conf2 = Conference(501, "IA Summit", "2025-06-20", "Science")

# print("--- INÍCIO DOS TESTES DE REGISTRATION ---")

# print("Teste 1: Criar registo válido...")
# reg1 = Registration(1, 101, 500, 150.50, "Confirmado")
# print(f"ID: {reg1.id}, Researcher: {reg1.researcher_id}, Fee: {reg1.fee}, Status: {reg1.attendance_status}")

# print("\nTeste 2: Criar registo com Researcher inexistente (ID 999)...")
# reg_err1 = Registration(2, 999, 500, 100.0, "Pendente")

# print("\nTeste 3: Criar registo com Conference inexistente (ID 888)...")
# reg_err2 = Registration(3, 101, 888, 100.0, "Pendente")

# print("\nTeste 4: Alterar status e taxa do Registo 1...")
# reg1.fee = 200.0
# reg1.attendance_status = "Presença Confirmada"
# print(f"Novo Status: {reg1.attendance_status}, Nova Taxa: {reg1.fee}")

# print("\n--- RESUMO FINAL (Registration.obj) ---")
# print(f"IDs registados com sucesso: {Registration.lst}")
# for r_id, obj in Registration.obj.items():
#     print(f"Registo ID {r_id}: Researcher {obj.researcher_id} na Conf {obj.conference_id}")

        