import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
  HP, MP, attack, defense, equipmentHP, equipmentMP, equipmentAttack, equipmentDefense = map(int, sys.stdin.readline().strip().split())

  HP = 1 if HP + equipmentHP < 1 else HP + equipmentHP
  MP = 1 if MP + equipmentMP < 1 else MP + equipmentMP
  attack = 0 if attack + equipmentAttack < 0 else attack + equipmentAttack
  defense = defense + equipmentDefense

  combatPower = HP + 5 * MP + 2 * attack + 2 * defense

  print(combatPower)