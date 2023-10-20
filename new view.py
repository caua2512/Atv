from models.cliente import Cliente, NCliente
from models.serviço import Servico, NServico
from models.agenda import Agenda, NAgenda

class View:
  @classmethod
  def cliente_inserir(cls, nome, email, fone):
    cliente = Cliente(0, nome, email, fone)
    NCliente.inserir(cliente)
  @classmethod
  def cliente_listar(cls):
    return NCliente.listar()
  @classmethod
  def cliente_atualizar(cls, id, nome, email, fone):
    cliente = Cliente(id, nome, email, fone)
    NCliente.atualizar(cliente)
  @classmethod
  def cliente_excluir(cls, id):
    cliente = Cliente(id," ", " ", " ")
    NCliente.excluir(cliente)
  @classmethod
  def servico_inserir(cls, Descrição, valor, Duração):
    serviço = Servico(0, Descrição, valor, Duração)
    NServico.inserir(serviço)
  @classmethod
  def servico_listar(cls):
    return NServico.listar()
  @classmethod
  def servico_atualizar(cls, id, Descrição, valor, Duração):
    servico = Servico(id, Descrição, valor, Duração)
    NServico.atualizar(servico)
  @classmethod
  def servico_excluir(cls, id):
    servico = Servico(id," ", " ", " ")
    NServico.excluir(servico)
  @classmethod
  def agenda_inserir(cls, Descrição, valor, Duração):
    agenda = Agenda(0, Descrição, valor, Duração)
    NAgenda.inserir(agenda)
  @classmethod
  def agenda_listar(cls):
    return NAgenda.listar()
  @classmethod
  def agenda_atualizar(cls, id, Descrição, valor, Duração):
    agenda = Agenda(id, Descrição, valor, Duração)
    NAgenda.atualizar(agenda)
  @classmethod
  def agenda_excluir(cls, id):
    agenda = Agenda(id," ", " ", " ", " ")
    NAgenda.excluir(agenda)
