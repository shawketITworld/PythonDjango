print('Takrim Grocery')
# Item1:
item_name = input('item_name :')
item_price = int(input('item_unit_price :'))
item_quantity = int(input('item_quantity :'))
sale = item_price * item_quantity
# --------output---------
print() # print For gape
print('You have purchased')
print('Item Name :', item_name)
print('Item Unit Price:', item_price)
print('Item Quantity :', item_quantity)
print(f'Total sale ={sale}' )
x = 'sale'
if x == 'sale':
    net1 = sale + sale*5/100
    print(f'Net Sale including 5% vat from the Government = {net1}')
    print(f'Net Sale={net1}')
    r=round(net1)
    print(r)
class Cal:
    def add(self,a,b) # def is function,add is method self is 
    return a+b    # self is conventional name which is instant variable
cal1 = cal()   # cal1 is object then must be cal but no need object in Function
print(cal1.add(5,6)) 