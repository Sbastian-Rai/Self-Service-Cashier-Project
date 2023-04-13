
''' 
    This module provide the transaction option from
    Self-Service Cahsier system.
    
    You can run this module after running start.py in terminal.
'''

#Import needed library and 'start' module
from tabulate import tabulate
import uuid
from start import Transaction

''' this bloc code has a function as interface of the program that be shown to the user '''
print('='*60)
print("\t || WELCOME TO THE SELF-SERVICE CASHIER SYSTEM || ")
print('='*60)

cust_name = input('Please, enter your name: ').title()

print(f'Hi, {cust_name}!\
        \nMake a purchase and sense a more efficient and sophisticated shopping experience')

#making an instance to assign the class
customer = Transaction()


def user_interface():
  '''this function connects the customer input to the firts assigned method in class Transaction'''
  try:
    name = input('Enter the name of the item: ').title()
    qty = int(input('Enter the amount of the item: '))
    price = int(input('Enter the price of the item: '))

    customer.add_item(name, qty, price)
    customer.check_order()

  except ValueError:
    print('Enter numbers only!')
    user_interface()

#assigning the function
user_interface()


def transaction_option():
  '''
    this function would call all the menu or transaction options that customers could choose
    this function run in the loop to display all the menu or whenever customers make a wrong input
  '''
  print('What are you up to next?')
  print('1. Add Item')
  print('2. Check Order')
  print('3. Update Name of Item')
  print('4. Update Amount of Item')
  print('5. Update Price of Item')
  print('6. Delete Item')
  print('7. Reset Transaction')
  print('8. Total Purchase')
  print('9. Log Out')

  try: 
    next_transaction = int(input('Enter the number of the option you would like to: '))

    if next_transaction == 1:
      try: 
        name = input('Enter the name of the item: ').title()
        qty = int(input('Enter the amount of the item: '))
        price = int(input('Enter the price of the item: '))

        customer.add_item(name, qty, price)
        customer.check_order()

      except ValueError:
        print('Enter numbers only!')
      
      transaction_option()
        
    elif next_transaction == 2:
      customer.check_order()

      transaction_option()
        
    elif next_transaction == 3:
      try: 
        customer.check_order()

        name = input('Enter the name of the item: ').title()
        new_name = input('Enter the name of the new item: ').title()

        customer.update_name(name, new_name)

        customer.check_order()

      except TypeError:
        print('You have not purchased the item')
            
      transaction_option()

    elif next_transaction == 4:
      try: 
        customer.check_order()

        name = input('Enter the name of the item: ').title()
        new_qty = int(input('Enter the new amount: '))

        customer.update_qty(name, new_qty)

        customer.check_order()

      except TypeError:
        print('You have not purchased the item')

      except ValueError :
        print('Enter numbers only!')
        
      transaction_option()

    elif next_transaction == 5:
      try: 
        customer.check_order()

        name = input('Enter the name of the item: ').title()
        new_price = int(input('Enter the new price: '))

        customer.update_price(name, new_price)

        customer.check_order()

      except TypeError:
        print('You have not purchased the item')

      except ValueError:
        print('Enter numbers only!')
            
      transaction_option()

    elif next_transaction == 6:
      try: 
        customer.check_order()

        name = input('Enter the name of the item: ').title()
        customer.delete_item(name)

        customer.check_order()

      except TypeError:
        print('You have not purchased the item')
          
      transaction_option()

    elif next_transaction == 7:
      customer.check_order()

      customer.reset_transaction()
      
      print('Transaction cancelled')
      customer.check_order()

      transaction_option()

    elif next_transaction == 8:
      customer.total_price()
        
    elif next_transaction == 9:
      print('Thanks for your purchase!')

  except ValueError:
     print('Enter numbers only!')
     transaction_option()

#assigning the function
transaction_option()