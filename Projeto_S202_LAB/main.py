from medico import Medico
from consultorio import Consultorio
from recepcionista import Recepcionista
from database import Graph
from write_a_json import write_a_json as wj


db = Graph(uri='bolt://3.235.44.236:7687', user='neo4j', password='flight-products-wings')
db.execute_query("MATCH(n) DETACH DELETE n")

consultorio = Consultorio(37540000, 'Rua A bairro B')
medico = consultorio.cadastra_medico('Davi', 99999999, 33333333333, 15000, 58462)
recepcionista = consultorio.cadastra_recepcionista("Joao",95654157, 66666666666, 2200)
paciente = recepcionista.cadastra_paciente('Leticia', 6541654254, 884615241, 524, "media")
wj(consultorio.mostra_funcionarios(),"Funcionarios")
wj(consultorio.mostra_dados(consultorio.endereco), "Dados Consultorio")
wj(consultorio.mostra_paciente(), "Pacientes")
paciente.marcar_consulta(1, '13/7',500, 'Davi')
wj(recepcionista.verifica_agendamentos(), "Agendamentos")
medico.atender(1)
wj(recepcionista.verifica_agendamentos(), "Agendamentos_apos_atender")
medico.medicar('15/5',884615241, 'Leticia', 'Dipirona')




