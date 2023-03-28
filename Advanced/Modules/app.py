
# syntax #1
import converter               #now this converter will behave as an object and access everything in the "converter.py" file 

result=converter.kg_to_lbs(60);        # a function from converter.py file is accessed in this current python file using converter object (importing converter)
print(result);

# syntax #2
from converter import kg_to_lbs                  # the function is imported directly from converter.py file to this file

result=kg_to_lbs(60);
print(result);

