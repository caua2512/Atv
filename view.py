from cliente import Cliente, NCliente

class views:
 def cliente_inserir( nome, email, fone ):
    cliente = Cliente(0, nome, email, fone)
    NCliente.inserir(cliente)
 def cliente_listar():
     return NCliente.listar()
 def cliente_atualizar(id, nome, email,fone):
        pass    
 def cliente_excluir(cliente):
     NCliente.excluir(cliente)
