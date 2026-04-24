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
    att = ['_id','_created_date','_name']
    header = 'Institutions'
    desc = ['Id','Created_Date','Name']
   
    def __init__(self, id, created_date, name):
        super().__init__()
        
        self._id = int(id)
        self._created_date = datetime.date.fromisoformat(created_date)
        self._name = name
        
        Institutions.obj[self._id] = self
        Institutions.lst.append(self._id)

    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, novo):
        self._id = novo
    
    @property
    def created_date(self):
        return self._created_date

    @created_date.setter
    def created_date(self, novo):
        self._created_date = novo

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, novo):
        self._name = novo
        

# print("--- Teste de Criação de Instituições ---")
# i1 = Institutions(10, "2020-01-01", "Universidade de Coimbra")
# i2 = Institutions("20", "2024-04-24", "Instituto Politécnico do Porto")

# print(f"Instituição 1: {i1.name} (Criada em: {i1.created_date})")
# print(f"Instituição 2: {i2.name} (ID: {i2.id}, Tipo do ID: {type(i2.id)})")

# print("\n--- Teste de Alteração ---")
# i1.name = "U. Coimbra (Atualizado)"
# i1.created_date = datetime.date(1290, 3, 1) 
# print(f"Dados atualizados i1: {i1.name} - Data Histórica: {i1.created_date}")

# print("\n--- Teste de Gestão Global ---")
# print(f"Lista de IDs de Instituições: {Institutions.lst}")
# print(f"Dicionário de Instituições: {Institutions.obj}")

# if 10 in Institutions.obj and Institutions.obj[10].name == "U. Coimbra (Atualizado)":
#     print("\n✅ Sucesso: A Instituição foi criada, armazenada e editada corretamente.")


    