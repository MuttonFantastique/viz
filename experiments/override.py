from dis import dis

class A(object):
  def _pick(self):
      print "1"

  def doitinA(self):
      self._pick()

class B(A):
  def _pick(self):
      print "2"

  def doitinB(self):
      self._pick()

b = B()
b.doitinA() # prints 1
b.doitinB() # prints 2

dis(A.doitinA)
print
dis(B.doitinB)