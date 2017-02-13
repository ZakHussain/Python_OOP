#the goal of this program is to create an object, 'Bike', that contains methods which allow a user 
#to create a bike object, display info about the bike, and move the bike
#forward and and in reverse. 

class Bike(object): 
  #__init__ is used to initialize the bike
  def __init__(self, price, max_speed, miles=None):
    self.price = price 
    self.max_speed = max_speed
    self.miles = 0

  #this method give information about the state of the bike  
  def displayinfo(self):
    print '\nthis bike costs $'+ str(self.price)
    print 'this bike can go', str(self.max_speed)+ 'mph'
    print 'this bike has been driven', str(self.miles), 'miles'
    return self

  #the ride method allows you to add 10 miles to distance of 'miles'  
  def ride(self):
    self.miles += 10
    return self

  #the reverse method subtracts 5 miles from the ridden distance travelled 
  def reverse(self):
    if self.miles >= 5:
      self.miles -= 5
    return self

#create three instances
bike1 = Bike(10,50)
bike1.ride().ride().ride().reverse().displayinfo();


bike2 = Bike(50,100)
# bike2.displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo();


bike3= Bike(100,200)
bike3.reverse().reverse().reverse().displayinfo();
# bike3.displayinfo()