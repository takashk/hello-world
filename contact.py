class Contact(object):
    def __init__(self, first_name, last_name, work_number, email, mobile_number="4156786970"):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number
        self.work_number = work_number
        self.email = email

    def send_text(self, message):
        print "To: %s - %s" % (self.text, message)


new_contact = Contact("yenny", "last", "4582565655", "test@test.com")
print new_contact
next_contact = Contact("kyoko", "last", "381096099", "4582565655", "test@test.com")

print new_contact.first_name


def main():
    contact_list = []
    contact_one = "kyoko", "takashima", "4151241234", "test@test.com"
    contact_two = "yenny", "yulianny", "4155551234", "test@test.com"
    contact_three = "pumpkin", "pie", "33333333", "test@test.com"

    contact_list.append(contact_one)
    contact_list.append(contact_two)
    contact_list.append(contact_three)
    # contact_list.append(Contact("kyoko", "takashima", "4151241234", "test@test.com"))
    # contact_list.append(Contact("kyoko", "takashima", "4151241234", "test@test.com"))
    # contact_list.append(Contact("kyoko", "takashima", "4151241234", "test@test.com"))


    # Contact("kyoko", "takashima", "4151241234")

    # contact_one = contact_list[("kyoko", "takashima", "4151241234")]
    # contact_two = contact_list["yenny", "yulianny", "4155551234"]
    # contact_three = contact_list["pumpkin", "pie", "33333333"]

    for burger in contact_list[0:]:
        print burger in contact_list

if __name__ == "__main__":
    main()

