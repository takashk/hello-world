# my_list = [1, 2, "kitten", 4, "five"]
# # print my_list[2]
# # print my_list[3]
# # print my_list[1]
# # print my_list[-1]
# # print my_list[len(my_list)-1]
# # print my_list[4]
# # print len(my_list)

# print my_list[0]
# print my_list[1:3]
# print my_list[1:6]
# print my_list[1:10]
# print my_list[-1]
# print my_list[-1:-3]
# print my_list[-3:-1]

shopping_list = ["flour", "water", "salt"]

input = raw_input("Would you like to type '1' to add, type '2' remove, or '3' view your list? ")


def add_list():
    add_list = str.lower(raw_input("What would you like to add to your list? "))
    if add_list in shopping_list:
        print "You already have that on your list."
    else:
        shopping_list.append(add_list)
        print shopping_list.sort()


def order_list():
    print shopping_list.sort()


def remove_item():
    remove_item = str.lower(raw_input("What would you like to remove from your list?"))
    if remove_item in shopping_list == False:
        print "The item you entered is not there."
    else:
        shopping_list.remove(remove_item)
        print shopping_list.sort()

input == "1"
    print add_list

input == "2"
    print remove_item

input == "3"
    print order_list

