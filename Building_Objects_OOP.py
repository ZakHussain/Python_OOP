# The Goal of this program is to get practice with Object Oriented Programming (OOP). 
# Here we create the 'blueprints' for 4 kind of objects - Cat, Human, Bike, and Car. 

# The Cat object requires a color, type, and age parameter to create an instance of a 'Cat'.
class Cat(object):
	def __init__(self, color, type, age):
		self.color = color 
		self.type = type 
		self.age = age

# The Human object requires no user input, and will print "New Human" once initialized.
class Human(object):
	def __init__(self, clan=None):
 		print "New Human!!!"

# The Bike object has an initialization that takes form, prim, max_speed, and miles as input. 
# It has a displayinfo(), ride(), and reverse() method to allow for interaction with the object.
class Bike(object):
 def __init__(self, form, price, max_speed, miles):
  self.form = form 	
  self.price = price
  self.max_speed = max_speed
  self.miles = 0

 def displayinfo(self):
 	print self.form 
 	print "Price for this is $" + str(self.price)
	print "Top speeds for this is "+ str(self.max_speed)+ 'mph'
	print "Total miles " + str(self.miles) + " miles "

 def ride(self):
 	print 'driving'
 	self.miles += 10 
	

 def reverse(self):
 	print 'Reversing'
 	if self.miles >= 5:
 		self.miles -= 5

# The car object is initialized with four attributes, price, speed, fuel, and mileage. 
# It also contains a display_all method that will show the information about the state of the
#car
class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel 
		self.mileage = mileage 	
		self.tax = .15 
		if self.price <= 10000:
			self.tax = 0.12

	def display_all(self):
		print 'the price is ', str(self.price)
		print 'the speed of this car is ', str(self.speed)
		print 'the current tank is ', str(self.fuel)
		print 'the present mileage is ', str(self.mileage)
		print self.tax

# here, we create an instance of a Cat, that we named 'garfield.' This 
# instance now has all the attributes that make a 'Cat,' (color, type, age, etc)
garfield = Cat('orange', 'fat', 5)

print garfield.color
print garfield.type
print garfield.age	

# these following calls create instances of the 'Bike' object		
locomotion = Bike('\n locomotion', 100, 200 , 0)
tricycle = Bike('\n trycyle', 2,20, 0)
motorcycle = Bike('\n motorcycle', 1000, 200, 0)

# the following object.method() calls, calls of the methods of the specific object
locomotion.ride()
locomotion.ride()
locomotion.ride()
locomotion.reverse()
locomotion.displayinfo()

tricycle.ride()
tricycle.ride()
tricycle.reverse()
tricycle.reverse()
tricycle.displayinfo

motorcycle.reverse()
motorcycle.reverse()
motorcycle.reverse()
motorcycle.displayinfo()

# the following object 'Kirby' is an instance of a 'Car' object 
Kirby1 = Car(10000, 35, 'Full', 15)

# the following print methods call on the 'fields' of the Kirby, Car Object
print Kirby1.speed
print Kirby1.fuel
print Kirby1.mileage
print Kirby1.price
print Kirby1.tax 






























