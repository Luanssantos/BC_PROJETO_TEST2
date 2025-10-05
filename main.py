from database import session
from models import Produto, Venda, Cadastro

produto = Produto(nome="Teclado Gamer", preco=150.0, estoque=20)
session.add(produto)
session.commit()

cliente = Cadastro(nome="João Silva", email="joao@example.com", senha="1234")
session.add(cliente)
session.commit()

quantidade = 2
valor_total = produto.preco * quantidade

venda = Venda(
    produto_id=produto.id,
    cliente_id=cliente.id,
    quantidade=quantidade,
    valor_total=valor_total
)
session.add(venda)

produto.estoque -= quantidade

session.commit()

print("Venda registrada com sucesso!")