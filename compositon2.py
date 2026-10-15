class CPU:
  def __init__(self, cores):
    self.cores = cores

class RAM:
  def __init__(self, size):
    self.size = size

class HardDrive:
  def __init__(self, capacity):
    self.capacity = capacity

class Computer:
  def __init__(self, cores, ram_size, hardDrive_Capacity):
    self.cpu = CPU(cores)
    self.ram = RAM(ram_size)
    self.hardDrive = HardDrive(hardDrive_Capacity)

mac = Computer(8, 16, 512)
print(mac.cpu.cores)
print(mac.hardDrive.capacity)
print(mac.ram.size)