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
    att = ['_id','_name','_comments']
    header = 'Researcher'
    desc = ['Id','Name','Comments']
    
    def __init__(self, id, name, comments):
        super().__init__()
        self._id = int(id)
        self._name = name
        self._comments = comments
        
        Researcher.obj[self._id] = self
        Researcher.lst.append(self._id)

    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, novo):
        self._id = novo

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, novo):
        self._name = novo
         
    @property
    def comments(self):
        return self._comments

    @comments.setter
    def comments(self, novo):
        self._comments = novo
        

# print("--- Teste de Criação ---")
# r1 = Researcher(101, "Dr. Alan Turing", "Pioneiro da computação")
# r2 = Researcher("102", "Ada Lovelace", "Primeira programadora") 

# print(f"Investigador 1: {r1.name} (ID: {r1.id})")
# print(f"Investigador 2: {r2.name} (ID: {r2.id})")

# print("\n--- Teste de Alteração ---")
# r1.name = "Alan M. Turing"
# r1.comments = "Lógica e Criptografia"
# print(f"Dados atualizados r1: {r1.name} - {r1.comments}")

# print("\n--- Teste de Gestão Global ---")
# print(f"Lista de IDs ativos: {Researcher.lst}")
# print(f"Dicionário de objetos: {Researcher.obj}")

# if Researcher.obj[101] == r1:
#     print("\n✅ Sucesso: O objeto r1 está guardado corretamente no dicionário da classe.")

   
        