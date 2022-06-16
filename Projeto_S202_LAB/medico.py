from pessoa import Pessoa
from database import Graph


class Medico(Pessoa):
    def __init__(self, nome, telefone, cpf, salario, crm):
        self.db = Graph(uri='bolt://3.235.44.236:7687', user='neo4j', password='flight-products-wings')
        self._name = nome
        self._telefone = telefone
        self._cpf = cpf
        self._salario = salario
        self._crm = crm

    def atender(self, numero):
        self.db.execute_query("MATCH(c:Consulta{numero_da_consulta: $numero}) DETACH DELETE c", {'numero': numero})

    def medicar(self, validade, cpf, nome, remedio):
        self.db.execute_query("CREATE(:Receita{remedio: $remedio, medico: $medico, crm: $crm, validade: $validade, cpf: $cpf, nome: $nome})", {'remedio': remedio, 'medico': self._name, 'crm': self._crm, 'validade': validade, 'cpf':cpf, 'nome':nome})
        self.db.execute_query("MATCH(r:Receita{cpf: $cpf}), (m:Medico{nome: $nome}) CREATE(m)-[:Faz]->(r)", {'cpf':cpf, 'nome': self._name})
        