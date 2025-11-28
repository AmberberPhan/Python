new_list = ["Asli", 576, 3.1415, False, None]

print(new_list[2])

new_list = ["Asli", 576, 3.1415, False, None]

new_list[2] = "banana"

print(new_list)

new_list = ["Asli", 576, 3.1415, False, None]

print(new_list[-1])

alphabet = ["a", "b", "c", "d", "e", "f", "g"]

print(alphabet[0:6:2])

new_list = ["Asli", 576, 3.1415, False, None, ["Ashwini", "Ling", "Reece", "Camila"]]

print(new_list[5][3])
#This means select the fifth element and find the third element within it

new_list = ["Asli", 576, 3.1415, False, None, ["Ashwini", "Ling", "Reece", "Camila"]]

new_list_length = len(new_list)

print(new_list_length)

for i in range(0,10,2):
    print(i)

L = [None, 1, 2, 4, 5]
for i in L[:-1]:
    print(i)

#This is printing the second last element only

my_list = [None, False, 45, 11, 67, 78]
#So now you might want to find the length of the list:
L = len(my_list)
for i in range(0,L,1):
    print(i)

count = 0

while count <= 10:
    count = count + 1
    print(count)
#count <= 10 is a Boolean bc it will test if it's True or False

numlist = [1, 9001, -3, 0]

for each_number in numlist:
    print(each_number*each_number)

alphabet = ["a", "b", "c", "d", "e"]

for index, letter in enumerate(alphabet):
    print(f"{letter} is at position {index} in the alphabet!")

print("Starting the outer loop!")
