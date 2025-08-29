import time
import sys
import os

inicio = time.perf_counter()

print(sys.platform)
print(os.getlogin())
os.system("ls")
time.sleep(15)
fim = time.perf_counter()
print (f"Tempo de execução: {fim - inicio:.2f}s")
