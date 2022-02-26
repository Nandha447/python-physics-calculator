while True:
      
 print("Welcome to Physics calculator ")
 inp=int(input("enter 1 for gravity, 2 for work and energy :"))
 if(inp==1):
      
      sinp=int(input("enter 1 for mass to weight, 2 for gravitational force: "))
      if(sinp==1):
       mass=float(input("enter mass: "))
       weight=mass*9.8
       print("the weight on earth is " + str(weight) + "kilograms")
      elif(sinp==2):
          radius=float(input("enter distance: "))
          m1=float(input("enter mass 1: "))
          m2=float(input("enter mass 2: "))
          G=6.67*(10**-11)
          force=G*m1*m2/(radius**2)
          print("the gravitational pull is " + str(force) + " newtons")
      else:(exit)
      
 elif(inp==2):
      sinp=int(input("enter 1 for work done, 2 for kinetic energy, 3 for potential energy, 4 for rate of work: "))
      if(sinp==1):
       force=int(input("enter force :"))
       distance=int(input("enter distance: "))
       joules=force*distance
       print("work done is " + str(joules) + "joules")
      elif(sinp==2):
       velocity=int(input("enter velocity: "))
       mass=int(input("enter mass: "))
       kenergy=1/2*mass*(velocity**2)
       print("kinetic energy is " + str(kenergy))
      elif(sinp==3):
       mass=int(input("enter object mass: "))
       g=9.8
       hieght=int(input("enter hieght: "))
       penergy=mass*g*hieght
       print("the potential energy is " + str(penergy))
      elif(sinp==4):
       work=int(input("enter work: "))
       time=int(input("enter time period: "))
       watt=work/time
       print("the rate of work is " + str(watt) + " watts")
else:(exit)
     
