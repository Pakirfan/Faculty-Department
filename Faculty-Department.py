class campus:
	__name=input("Enter the university name : \n")
	__location=input("Enter your campus location: \n")
	def show(self):
		print("campus name=",self.__name,"and location in",self.__location)
class department(campus):
	__name=input("Enter your department name : \n")
	__head=input("Enter your dean name : \n")
	__compus=input("Enter your campus : \n")
	def info(self):
		print("department=",self.__name,"and head of computer depar",self.__head,"of",self.__compus)
class faculty:
	__name=input("Enter your Faculty : \n")
	__head=input("Enter your head of Faculty : ")
	__department=input("Enter your department")
	def init(self):
		print("faculty name=",self.__name,"and head of faculty",self.__head,"and department",self.__department)
m=department()
m.show()
m.info()
k=faculty()
k.init()