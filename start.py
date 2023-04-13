
''' 
    You need to run the 'start' module before starting a program with the 'main' module.
    You only need to execute this module once.

    After running this modeule, You will be enable to run Self-Service Cashier program
    by running the main.py module
''' 

#Import needed library
from tabulate import tabulate
import uuid


#Making a class by name Transaction() as the main class of this program
class Transaction():


  def __init__(self):
    '''the Class has the atribut consists of self.item,
       which list the item of each transaction in list type.
       it also has id transaction atribut which generate the ID transaction
       of each customer making a purchase
    '''
    self.item = list()
    self.id_transaction = str(uuid.uuid4())[0:16]
  
  def add_item(self, name, qty, price): 
    ''' this is a method to customers to add item.
        this method require 3 paramters to customers to enlist, namely:
        the name, quantity, and price
    '''
    self.item.append([name, qty, price, qty*price])

  def check_order(self):
    '''this method will display the order of customers in a table of order'
       it also display the generated ID transaction of customers.
    '''
    data_order = self.item
    header = ['Name', 'Quantity', 'Price', 'Total']
    
    print(f'ID transaction: {self.id_transaction}')
    print(tabulate(data_order, header, tablefmt = 'fancy_grid'))

  def index_name (self, name):
    ''' Since the purchase entered by customers will be enlisted in a list type,
        this method is needed to look out the name of item that will be referenced
        in the following methods
    '''
    for i in range(len(self.item)):
      if name == self.item[i][0]:
        return i  

  def update_name (self, name, new_name):
    '''this method has function to update/change the name of the item
       by referencing to the name of the item which be look out by index_name method
    '''
    self.item[self.index_name(name)][0]= new_name
    
  def update_qty (self, name, new_qty):
    '''this method has function to update/change the quantity of the item
       by referencing to the name of the item which be look out by index_name method
    '''
    self.item[self.index_name(name)][1]= int(new_qty)
    self.item[self.index_name(name)][3]= new_qty*self.item[self.index_name(name)][2]
  
  def update_price (self, name, new_price):
    '''this method has function to update/change the price of the item
       by referencing to the name of the item which be look out by index_name method
    '''
    self.item[self.index_name(name)][2]= int(new_price)
    self.item[self.index_name(name)][3]= self.item[self.index_name(name)][1]*new_price
     
  def delete_item (self, name):
    '''this method enables to delete the row of item entered
    '''
    self.item.pop(self.index_name(name))

  def reset_transaction (self):
    '''this method will reset all the list of order'''
    self.item.clear()

  def total_price(self):
    '''this method will display the table of the order,
       it also need a list to enlist the numbers of total price per item
       to sum up as the total price
    '''
    self.check_order()
      
    list_price = []

    for i in range(len(self.item)):
      list_price.append(self.item[i][3])
      
    total_price = sum(list_price)

    if total_price >= 500_000:
      after_disc = round(total_price * 0.9)

      print(f'Your total purchase is Rp{total_price}.\
              \nYou get a 10% discount! The amount of the payment you should make is Rp{after_disc}')
    
    elif total_price >= 300_000:
      after_disc = round(total_price * 0.92)

      print(f'Your total purchase is Rp{total_price}.\
              \nYou get a 8% discount! The amount of the payment you should make is Rp{after_disc}')
    
    elif total_price >= 200_000:
      after_disc = round(total_price * 0.95)

      print(f'Your total purchase is Rp{total_price}.\
              \nYou get a 5% discount! The amount of the payment you should make is Rp{after_disc}')
    
    else:
      print(f'Your total purchase is Rp{total_price}')
      
    print('='*30)
    print('Continue to payment')  
    print('='*30)
