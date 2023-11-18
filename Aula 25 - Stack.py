class Stack:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return len(self.itens) == 0

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.is_empty():
            return self.itens.pop()
        else:
            raise IndexError("A pilha está vazia")

    def top(self):
        if not self.is_empty():
            return self.itens[-1]
        else:
            raise IndexError("A pilha está vazia")

    def length(self):
        return len(self.itens)


# Exemplo de uso da pilha
pilha_exemplo = Stack()
pilha_exemplo.is_empty()
pilha_exemplo.push(1)
pilha_exemplo.push(2)
pilha_exemplo.push(3)

print("Topo da pilha:", pilha_exemplo.top())  # Saída: 3
print("Tamanho da pilha:", pilha_exemplo.length())  # Saída: 3

item_removido = pilha_exemplo.pop()
print("Item removido:", item_removido)  # Saída: 3
print("Tamanho da pilha após desempilhar:",
      pilha_exemplo.length())  # Saída: 2
