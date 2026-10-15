class Singletone:
  __instance = None
  def __init__(self):
    if Singletone.__instance is None:
      Singletone.__instance = self
    else:
      raise Exception("This is singletone, Already have an instance, use that only by calling get_instance method.")
  @staticmethod
  def get_instance():
    if Singletone.__instance is None:
      Singletone()
    return Singletone.__instance

Singletone()
print(Singletone.get_instance())
print(Singletone.get_instance())
print(Singletone.get_instance())
# Singletone()