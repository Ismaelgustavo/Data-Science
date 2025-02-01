class Personagem:

    def __init__(self,nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa


    def atacar(self,outro_personagem):
        dano = self.ataque - outro_personagem.defesa 
        dano = max(dano, 0)
        outro_personagem.vida -= dano
        outro_personagem.vida = max(outro_personagem.vida, 0) 
        print(f'O personagem {self.nome} atacou {outro_personagem.nome} e causou {dano} de dano.')


    def status(self):
        print(f'{self.nome} - Vida:{self.vida}, Ataque:{self.ataque}, Defesa:{self.defesa}')



guerreiro = Personagem('Guerreiro', 100, 20, 10)
mago = Personagem('Mago', 100, 25, 5)        

print(guerreiro.status())
print(mago.status())

guerreiro.atacar(mago)
print(mago.status())

mago.atacar(guerreiro)
print(guerreiro.status())


