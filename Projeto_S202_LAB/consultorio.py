import pprint
from database import Graph
from medico import Medico
from recepcionista import Recepcionista

class Consultorio():
    def __init__(self, cep, endereco):
        self.db = Graph(uri='bolt://3.235.44.236:7687', user='neo4j', password='flight-products-wings')
        self.cep = cep
        self.endereco = endereco
        self.db.execute_query("CREATE(:Consultorio{cep:$cep, endereco:$endereco})", {'cep':cep, 'endereco': endereco})

    def cadastra_medico(self, nome, telefone, cpf, salario, crm):
        self.db.execute_query("CREATE(:Pessoa:Medico{nome:$nome, telefone:$telefone, cpf:$cpf, salario: $salario, crm: $crm})", {'nome':nome, 'telefone':telefone, 'cpf': cpf, 'salario': salario, 'crm':crm})
        self.db.execute_query("MATCH(m:Medico{nome:$nome}), (c:Consultorio{cep: $cep}) CREATE(m)-[:TRABALHA_EM]->(c)", {'nome':nome, 'cep':self.cep})
        return Medico(nome, telefone, cpf, salario, crm)
    
    def cadastra_recepcionista(self, nome, telefone, cpf, salario):
        self.db.execute_query("CREATE(:Pessoa:Recepcionista{nome:$nome, telefone:$telefone, cpf:$cpf, salario: $salario})", {'nome':nome, 'telefone':telefone, 'cpf': cpf, 'salario': salario})
        self.db.execute_query("MATCH(r:Recepcionista{nome:$nome}), (c:Consultorio{cep: $cep}) CREATE(r)-[:TRABALHA_EM]->(c)", {'nome':nome, 'cep':self.cep})
        return Recepcionista(nome, telefone, cpf, salario)

    def mostra_funcionarios(self):
        return self.db.execute_query("MATCH(p:Pessoa)-[:TRABALHA_EM]->(c:Consultorio{endereco: $endereco}) RETURN p.nome", {'endereco':self.endereco})
    
    def mostra_dados(self, endereco):
        return self.db.execute_query("MATCH(c:Consultorio{endereco:$endereco}) RETURN c", {'endereco':endereco})

    def mostra_paciente(self):
        return self.db.execute_query("MATCH(p:Paciente) RETURN p")
        


    

