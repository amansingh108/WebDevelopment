class Student:
	def __init__(self, name,contact):
		self.name = name
		self.contact= contact

	def getdata(self):
		print("We are accepting Students")
		self.name= input('Enter a Name: ')
		self.contact = input('Enter a Contact info: ')

	def putdata(self):
		print('The name is'+ self.name+'.' + 'This is the contact: '+self.contact)

# Inheritance of  class

class ScienceStudent(Student):

	def __init__(self, age):
		self.age = age

	def science(self):
		print('I am a ascience student ')


ScienceStudent1 = ScienceStudent(20)
ScienceStudent1.getdata()
ScienceStudent1.putdata();

