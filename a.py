from pip._vendor.distlib.compat import raw_input

__author__ = 'Azad'
largest, smallest = None, None

num_list = []  # list holds numbers only
while True:
    try:
        num = raw_input('Enter the num:')
        if num == 'done':
            break
        num = int(num)  # convert this to integer
        num_list.append(num)  # save it to array
    except:  # if we can not convert the number
        print('Invalid number')

num_list.sort()  # sort it ascending order

print('Largest {0} and smallest {1}'.format(num_list[-1], num_list[0]))