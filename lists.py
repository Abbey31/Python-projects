# # # # # # users = ['Dave','John','Sara']

# # # # # # data = ['Dave', 42, True]

# # # # # # emptylist = []

# # # # # # print("dave" in emptylist)

# # # # # # print(users[0])
# # # # # # print(users[-2])

# # # # # # print(users.index('Sara'))

# # # # # # print(users[0:2])
# # # # # # print(users[1:])
# # # # # # print(users[-3:-1])

# # # # # # print(len(data))

# # # # # # users.append('Elsa')
# # # # # # print(users)

# # # # # # users += ['Jason']
# # # # # # print(users)
# # # # # # users.extend(['Robert','Jimmy'])
# # # # # # print(users)

# # # # # # users.insert(0,'Bob')
# # # # # # print(users)
# # # # # # users[2:2] = ['Eddie','Alex']
# # # # # # print(users)

# # # # # # users[1:3] = ['Robert','JPJ']
# # # # # # print(users)
# # # # # # users.remove('Bob')
# # # # # # print(users)

# # # # # # print(users.pop())
# # # # # # print(users)

# # # # # # data.clear()
# # # # # # print(data)

# # # # # # users[1:2] = ['dave']
# # # # # # users.sort()
# # # # # # print(users)

# # # # # # users.sort(key=str.lower)
# # # # # # print(users)

# # # # # #nums = [4,42,78,1,5]
# # # # # #nums.reverse()
# # # # # #print(nums)
# # # # # #nums.sort(reverse=True)
# # # # # #print(nums)
# # # # # #print(sorted(nums, reverse=True))
# # # # # #print(nums)
# # # # # #numscopy = nums.copy()
# # # # # #mynums = list(nums)
# # # # # #mycopy = nums[:]

# # # # # #print(numscopy)
# # # # # #print(mynums)
# # # # # #mycopy.sort()
# # # # # #print(mycopy)
# # # # # #print(nums)

# # # # # anothertuple = (1,4,2,8)

# # # # # (one, *two, hey) = anothertuple
# # # # # print(one)
# # # # # print(two)
# # # # # print(hey)
# # # # num = {1,2,3,4}
# # # # for i in range(num):
# # # #     print(i)
# # # # one = {1,2,3}
# # # # two = {5,6,7}
# # # # mynewset = one.union(two)
# # # # print(mynewset)
# # # one = {1,2,3}
# # # two = {5,6,7}
# # # mynewset = one.union(two)
# # # print(mynewset)
# # # one.intersection_update(two)
# # # print(one)
# # # one = {1,2,3}
# # # two = {2,3,4}
# # # one.intersection_update(two)
# # # print(one)
# # one = {1,2,3}
# # two = {2,3,4}
# # one.symmetric_difference_update(two)
# # print(one)
# # LOOPS
# #value = 1
# #while value < 10:
#  #   print(value)
#   #  value += 1
# names = ['Dave','sara','John']
# actions = ['codes','eats','sleeps']
# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")
#FUNCTIONS
# def hello_world():
#     print("Hello world!")

# hello_world()
# def sum(num1, num2):
#     return num1 + num2


# total = sum(2,3),

# print(total)
# def multiple_items(*args):
#     print(args)
#     print(type(args))

# multiple_items("Dave","John","Sara")  
# def multi_named_items(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# multi_named_items(first="Dave",last="Gray")
#RECURSION
# def add_one(num):

#     if(num >=9):
#         return num + 1
#     total = num + 1
#     print(total)

#     return add_one(total)
# mynewtotal = add_one(0)
# print(mynewtotal)
value = "y"
count = 0

while value:
    count += 1
    print(count)
    if count == 5:
        break
    else:
        value = 0
        continue