# a package(a directory/folder) is a container having multiple modules


                          # syntax #1
import Package1.shipping                 #shipping module of package1(a package) is imported in this current python file 
# now Package1.shipping can be used as an object to access the shipping.py in Package1 

Package1.shipping.calc_shipping();


                          # syntax #2
from  Package1.shipping import calc_shipping       # a function named calc_shipping in directly imported from a module in package named Package1

calc_shipping()

#we can import more than one functions using the same syntax
from  Package1.shipping import calc_shipping , calc_tax

calc_shipping()
calc_tax()


                          # syntax #3
from Package1 import shipping                   # now shipping.py from Package1 is imported in this curent python file
# now shipping can be used as a object to access everything present in shipping.py which is present in a package named Package1

shipping.calc_shipping()
shipping.calc_tax()





