class A:
  def __init__(self, val):
    val = 3;
    self.val = val
  def change(self):
    self.val = 12

ans = []
a = A(13)
print("a : ", a.val)
ans.append(a.val)
a.change()
print(ans)
ans.append(a.val)
print(ans)