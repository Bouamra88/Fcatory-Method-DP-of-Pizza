#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Amira
#
# Created:     01/03/2020
# Copyright:   (c) Amira 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
class Pizza:
    price:float
    def get_price(self): print("Les prix des pizza:")

class TunaPizza(Pizza):
     price=60.0
     def get_price(self):
        p=self.price
        print("Le prizza Tuna est:"+str(p))

class SimplePizza(Pizza):
    price=30.0
    def get_price(self):
        p=self.price
        print("Le prix de prizza simple est:"+str(p))

class MargaritaPizza(Pizza):
     price=70.0
     def get_price(self):
        p=self.price
        print("Le prix de prizza Margarita est:"+str(p))

class PizzaFactory:
    def createPizza(self):
        pass

class LuxPizzaFactory(PizzaFactory):
    print("pizzeriaLux :")
    def createPizza(self):

        if type=="SimplePizza": return SimplePizza()
        elif type=="MargaritaPizza": return MargaritaPizza()
        else :
          print("Le type qui n'existe pas est:"+type)

class HoumaPizzaFactory(PizzaFactory):

    def createPizza(self):

        if type=="TunaPizza": return TunaPizza()
        elif type=="SimplePizza": return SimplePizza()
        else :
            print("Le type qui n'existe pas est:"+type)
if __name__ == '__main__':
  for type in ("SimplePizza" ,"MargaritaPizza"):
    pizza = LuxPizzaFactory.createPizza(type)
    pizza.get_price()
  for type in ("SimplePizza" ,"TunaPizza"):
    pizza = HoumaPizzaFactory.createPizza(type)
    pizza.get_price()

