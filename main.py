# class Human():
#     counter = 0

#     def __init__(self, Name):
#         Human.counter += 1
#         self._name = Name
    
#     def setName(self):
#         self._name = input("Введите ваше имя ")

#     def getName(self):
#         return self._name
    
#     def out(self):
#         print("Human",  self._name)
    
#     def getCounter(self):
#         return Bilder.counter



# class Bilder(Human):
#     counter = 0

#     def __init__(self, Name, Prof):
#         super().__init__(Name)
#         self.__prof = Prof
#         Bilder.counter += 1
#     def setProf(self):
#         self.__prof = input("Введите вашу профессию ")

#     def getProf(self):
#         return self.__prof
    
#     def getCounter(self):
#         return Bilder.counter

#     def out(self):
#         print("Bilder", self.__prof)







# class Pilot(Human):
#     counter = 0

#     def __init__(self, Name, Reic):
#         super().__init__(Name)
#         self.__Reic = Reic
#         Pilot.counter += 1
#     def setProf(self):
#         self.__Reic = input("Сколько у вас было рейсов")

#     def getProf(self):
#         return self.__Reic
    
#     def getCounter(self):
#         return Bilder.counter

#     def out(self):
#         print("Pilot", self.__Reic)




# class Sailor(Human):
#     counter = 0

#     def __init__(self, Name, Prof):
#         super().__init__(Name)
#         self.__prof = Prof
#         Sailor.counter += 1
#     def setProf(self):
#         self.__prof = input("Введите вашу профессию ")

#     def getProf(self):
#         return self.__prof
    
#     def getCounter(self):
#         return Bilder.counter
    
#     def out(self):
#         print ( "Sailor", self.__prof)

# list = [Human("User"), Bilder("builder", "welder"), Sailor("Jack","Cap"), Pilot("Ron", 103)]

# def out(list):
#     for el in list:
#         el.out()
# out(list)

# def getCounter(list):
#     for el in list:
#         el.getCounter()
# getCounter(list)




# class Passport():
#     counter = 0

#     def __init__(self, FIO, age, city, pol, nomerSeriya):
#         Passport.counter += 1
#         self._FIO = FIO
#         self._age = age
#         self._city = city
#         self._pol = pol
#         self._nomerSeriya = nomerSeriya
    
#     def getFIO(self):
#         return self._FIO
    
#     def setFIO(self, FIO):
#         self._FIO = FIO

#     def getAge(self):
#         return self._age
    
#     def setAge(self, age):
#         self._age = age

#     def getCity(self):
#         return self._city
    
#     def setCity(self, city):
#         self._city = city

#     def getPol(self):
#         return self._pol
    
#     def setPol(self, pol):
#         self._pol = pol

#     def getNomerSeriya(self):
#         return self._nomerSeriya
    
#     def setNomerSeriya(self, nomerSeriya):
#         self._nomerSeriya = nomerSeriya

#     def getCounter(self):
#         return Passport.counter

#     FIO = property(getFIO, setFIO)
#     age = property(getAge, setAge)
#     city = property(getCity, setCity)
#     pol = property(getPol, setPol)
#     nomerSeriya = property(getNomerSeriya, setNomerSeriya)
#     def out(self):
#         print(self._FIO , self._age, self._city, self._pol, self._nomerSeriya)

# class ForeignPassport(Passport):
#     counte = 0 
#     def __init__(self, FIO, age, city, pol, nomerSeriya, viza, NZ):
#         super().__init__(FIO, age, city, pol, nomerSeriya)
#         ForeignPassport.counte +=1
#         self.__viza = viza
#         self.__NZ = NZ

        
#     def getViza(self):
#         return self.__viza
    
#     def setViza(self, viza):
#         self.__viza = viza

#     def getNZ(self):
#         return self.__NZ
    
#     def setNZ(self, NZ):
#         self.__NZ = NZ
    
#     def getCounter(self):
#         return ForeignPassport.counte

#     viza = property(getViza, setViza)
#     NZ = property(getNZ, setNZ)
#     def out(self):
#         print(self._FIO , self._age, self._city, self._pol, self._nomerSeriya, self.__viza, self.__NZ)
    

# list  = [Passport("KEA", 15, "Sochi", "M", 155171513), ForeignPassport("ASD", 21, "Sochi", "M", 216513512, "usa",5151351531),]

# def out(list):
#     for el in list:
#         el.out()

# out(list)
# print('--------------------------------------------')
# def getCounter(list):
#     for el in list:
#         print(el.getCounter())

# getCounter(list)
# print(list[0].getCounter())



class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
    def get_area(self):
        return self.a * self.b
    
r = Rectangle(20, 40)
r.get_area()