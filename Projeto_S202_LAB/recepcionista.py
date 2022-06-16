from calendar import c
from pessoa import Pessoa
from database import Graph
from paciente import Paciente

class Recepcionista(Pessoa):
    def __init__(self, nome, telefone, cpf, salario):
        self.db = Graph(uri='bolt://3.235.44.236:7687', user='neo4j', password='flight-products-wings')
        self._nome = nome
        self._telefone = telefone
        self._cpf = cpf
        self._salario = salario

    def cadastra_paciente(self, nome, telefone, cpf, cadastro, prioridade):
        self.db.execute_query("CREATE(:Paciente{nome: $nome, telefone: $telefone, cpf: $cpf, cadastro: $cadastro, prioridade: $prioridade})",{'nome':nome, 'telefone':telefone, 'cpf':cpf, 'cadastro':cadastro, 'prioridade': prioridade})
        return Paciente(nome,telefone, cpf, cadastro, prioridade)

    def verifica_agendamentos(self):
        return self.db.execute_query("MATCH(c:Consulta) RETURN c")

    
    
