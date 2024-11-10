# smallest = None
# print('Before')
# for value in [3,41,12,9,74,15]:
#     if smallest is None:
#         smallest = value
#     elif value < smallest :
#         smallest = value
#     print(smallest, value)

# print('After',smallest)
# abc = 'With three words'
# stuff = abc.split()
# print(stuff)
# counts = dict()
# names = ['csev','cwen','csev','zqian','cwen']
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1
# print(counts)
# c = {'a':10,'b':1,'c':22}
# print(sorted([(v,k) for k, v in c.items() ]))
#REGEX
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9] +',x)
print(y)
y = re.findall('[AEIOU] +',x)
print(y)