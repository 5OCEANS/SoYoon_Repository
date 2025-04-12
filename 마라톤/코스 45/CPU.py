import sys

def get_opcode(cmd):
  cmd = str(cmd)
  opcode = ""
  if cmd.startswith("ADD"):
    opcode = "0000"
  elif cmd.startswith("SUB"):
    opcode = "0001"
  elif cmd.startswith("MOV"):
    opcode = "0010"
  elif cmd.startswith("AND"):
    opcode = "0011"
  elif cmd.startswith("OR"):
    opcode = "0100"
  elif cmd.startswith("NOT"):
    opcode = "0101"
  elif cmd.startswith("MULT"):
    opcode = "0110"
  elif cmd.startswith("LSFTL"):
    opcode = "0111"
  elif cmd.startswith("LSFTR"):
    opcode = "1000"
  elif cmd.startswith("ASFTR"):
    opcode = "1001"
  elif cmd.startswith("RL"):
    opcode = "1010"
  elif cmd.startswith("RR"):
    opcode = "1011"
  if cmd.endswith("C"):
    opcode += "1"
  else:
    opcode += "0"
  opcode += "0"
  return opcode

def get_rA(cmd1, cmd2):
  cmd1 = str(cmd1)
  rA = ""
  if cmd1.startswith("MOV") or cmd1.startswith("NOT"):
    rA = "000"
  else:
    rA = bin(cmd2)[2:].zfill(3)
  return rA
  
def get_rB(cmd1, cmd2):
  cmd1 = str(cmd1)
  rB = bin(cmd2)[2:].zfill(3)
  if cmd1.endswith("C"):
    rB = rB.zfill(4)
  else:
    rB += "0"
  return rB


N = int(sys.stdin.readline().strip())
for i in range(N):
  command = list(sys.stdin.readline().strip().split())
  opcode = get_opcode(command[0])
  opcode += bin(int(command[1]))[2:].zfill(3)
  opcode += get_rA(command[0], int(command[2]))
  opcode += get_rB(command[0], int(command[3]))
  print(opcode)  