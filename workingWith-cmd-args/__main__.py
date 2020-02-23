import argparse

parser = argparse.ArgumentParser(
    description="Lalith working with command line arguments"
)

parser.add_argument("echo") #Required argument
parser.add_argument("echo2", help="This is echo2 argument")  #Required argument

parser.add_argument('-a', help='some description') #Optional argument
parser.add_argument('-b', action="store", default=False) #Optional argument
parser.add_argument('-c', action="store_true", default=False) #Optional argument
parser.add_argument('-s', action='store',
                    dest='simple_value',
                    default= 'hello',
                    help='Store a simple value')  #Optional argument
parser.add_argument('-square', action="store", dest="square", help="provide a number to find its square value", type=int)

results = parser.parse_args()

print(results.echo)
print(results.echo2)
print(results.a)
print(results.b)
print(results.c)
print('simple_value     = {!r}'.format(results.simple_value))
if(results.square):
    print('Square value of ' , results.square*2)

#Example 
'''
#Example: 

> python3 __main__.py -a hello -b secondarg -c -s "this is school" echo echo2 -square 3
echo
echo2
hello
secondarg
True
simple_value     = 'this is school'
Square value of  6

'''

#print('simple_value     = {!r}'.format(results.C))


#  print(
#     parser.parse_args(
#         ['-c=hello']
#     )
# )
