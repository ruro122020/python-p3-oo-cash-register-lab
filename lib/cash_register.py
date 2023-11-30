#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = 0
    
  def add_item(self, title, price, quantity=1):
      self.total += price * quantity
      quantity_items = [title] * quantity
      self.items += quantity_items 
      

  def apply_discount(self):
     if self.discount == 0:
        print('There is no discount to apply.')
     else:
        self.total -= (self.discount * self.total) / 100
        print(f'After the discount, the total comes to ${int(self.total)}.')
   
      
     
