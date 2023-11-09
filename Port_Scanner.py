import socket

target = input("Target: ")
if target == "":
  print("Invalid Sintax")
else:
  print(f"Scanning Target: {target}")
  for port in range(1, 1040):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
      print(f"Port {port} is open!")
    s.close()