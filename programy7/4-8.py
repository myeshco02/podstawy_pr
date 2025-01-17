from contact import Contact, cList


def main():
    my_contacts = cList()

    # Add contacts
    my_contacts.addContact(Contact("Sophia Carter", "SophieC@onet.pl", "698614538"))
    my_contacts.addContact(Contact("Liam Johnson", "LJ@o2.pl", "897256195"))
    my_contacts.addContact(Contact("Olivia Martinez", "OliMar@google.pl", "287006752"))
    my_contacts.addContact(Contact("Ethan Brown", "Ebrown@gmail.com", "426895279"))

    my_contacts.displayContacts()


if __name__ == "__main__":
    main()
