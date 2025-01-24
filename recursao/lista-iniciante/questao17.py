'''
numDiscos: int - Quantidade de discos a movimentar.
origem: identificador da torre de origem
destino: identificador da torre destino.
temp: identificador da torre auxiliar
'''
def moveTower(numDiscos,origem, destino, auxiliar):
    if numDiscos >= 1:
        (numDiscos-1,origem,auxiliar,destino)
        moveDisco(origem,destino)
        moveTower(numDiscos-1,auxiliar,destino,origem)
def moveDisco(origem,destino):
    print("Movendo disco da haste",origem,"para a haste",destino)
moveTower(3,"A","B","C")

# Movendo disco da haste A para a haste B
# Movendo disco da haste C para a haste B
# Movendo disco da haste A para a haste B