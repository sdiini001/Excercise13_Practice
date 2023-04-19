# this is opening the file, a stands for append
pelican = open('pelican.txt', 'a')
# this adds the two lines to the code
# use a variable =
num = pelican.write('A wonderful bird is the pelican \n')
print(num)
num2 = pelican.write('His bill holds more than his belican \n')
print(num2)
# this is a list
# then appended this to file
lines = ['He can take in his beack, \n', "Enough food for a week, \n", "But I'm damned if I see how the helican. \n"]
append_line = pelican.writelines(lines)