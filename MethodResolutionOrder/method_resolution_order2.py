class A:
	def whereiam(self):
		print "I am in A"

		
class B(A):
	def whereiam(self):
		print "I am in B"

		
class C(A):
	def whereiam(self):
		print "I am in C"
		
		
class D(C, B):
	pass

if __name__ == "__main__":
	d = D()
	d.whereiam() #result: I am in C
