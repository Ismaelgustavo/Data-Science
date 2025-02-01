class Prato:
    def __init__(self, nome, preco, ingredientes):
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes

    def detalhes_prato(self):
        ingredientes_str = ', '.join(self.ingredientes)
        return f"Prato: {self.nome} | Preço: R${self.preco:.2f} | Ingredientes: {ingredientes_str}"


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.lista_pratos = []

    def adicionar_prato(self, prato):
        if isinstance(prato, Prato):
            self.lista_pratos.append(prato)
        else:
            print("Erro: Apenas objetos do tipo Prato podem ser adicionados ao pedido.")

    def valor_total(self):
        total = sum(prato.preco for prato in self.lista_pratos)
        return total

    def resumo_pedido(self):
        pratos_detalhes = '\n'.join(prato.detalhes_prato() for prato in self.lista_pratos)
        total = self.valor_total()
        return f"Cliente: {self.cliente}\n{pratos_detalhes}\nTotal do Pedido: R${total:.2f}"


# Demonstração de funcionamento
if __name__ == "__main__":
    # Instanciando pratos
    prato1 = Prato("Macarrão Carbonara", 32.90, ["Macarrão", "Ovos", "Queijo Pecorino", "Pancetta"])
    prato2 = Prato("Risoto de Camarão", 45.50, ["Arroz Arbóreo", "Camarão", "Caldo de Legumes", "Queijo Parmesão"])
    prato3 = Prato("Sopa de Cebola", 18.00, ["Cebola", "Caldo de Carne", "Queijo Gruyère", "Pão Torrado"])

    # Criando um pedido
    pedido = Pedido("João Silva")

    # Adicionando pratos
    pedido.adicionar_prato(prato1)
    pedido.adicionar_prato(prato2)
    pedido.adicionar_prato(prato3)

    # Exibindo resumo do pedido
    print(pedido.resumo_pedido())
