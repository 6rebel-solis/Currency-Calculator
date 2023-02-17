from currency_converter import CurrencyConverter #Importing main lib 
from datetime import date #importing date
#
c = CurrencyConverter()
lng = {'USD', 'GBP', 'AUD', 'PLN', 'EUR', 'CAD'}
osn = input(' Input your action(LIST, CONVERT, INFO, exit, quit, q)  ')
print('Welcome to CCL-1')
if osn == 'LIST' or osn == 'CONVERT' or osn == 'INFO':
    if osn == 'LIST':
         print('All currencies available: ', lng)
    if osn == 'CONVERT':
         val = input('Start currency ')
         val2 = input('End currency ')
         num = input('Amount of currency 1 ')
         output = c.convert(num, val, val2)
         print (output)
    if osn == 'INFO':
         print('Currency CalcuLator 1 - is my new project, just for opensourcing')
    if osn.lower() in {'EXIT', 'QUIT', 'Q'}:
         print('Bye!')
         exit()
        
    
        





