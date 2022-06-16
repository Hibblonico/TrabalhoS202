from pessoa import Pessoa
from database import Graph

class Paciente(Pessoa):
    def __init__(self, nome, telefone, cpf, cadastro, prioridade):
        self.db = Graph(uri='bolt://3.235.44.236:7687', user='neo4j', password='flight-products-wings')
        self._name = nome
        self._telefone = telefone
        self._cpf = cpf
        self._cadastro = cadastro
        self._prioridade = prioridade

    def marcar_consulta(self,numero, data, valor, medico):
        self.db.execute_query("CREATE(:Consulta{numero_da_consulta: $numero, cpf: $cpf, data: $data, valor: $valor, medico: $medico})", {'numero':numero, 'cpf':self._cpf, 'data':data, 'valor': valor, 'medico': medico})
        self.db.execute_query("MATCH(c:Consulta{numero_da_consulta: $numero}), (p:Paciente{cpf: $cpf}) CREATE(p)-[:Tem]->(c)", {'numero': numero, 'cpf': self._cpf})

    



