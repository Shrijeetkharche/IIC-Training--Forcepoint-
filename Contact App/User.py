import uuid
from ContactDetails import ContactDetails
from Contacts import Contact

class User:
    # userID = []
    allUsers = []
    def __init__(self, fName, lName, contacts, isActive, isAdmin):
        self.fName = fName
        self.lName = lName
        self.contacts = contacts
        self.isActive = isActive
        self.isAdmin = isAdmin
        self.userID = uuid.uuid4()
        # User.userID.append(self.userID)
        User.allUsers.append(self)

    @staticmethod
    def findUser(fName, lName):
        """Checks if user exist or not"""
        for user in User.allUsers:
            if user.fName == fName and user.lName == lName:
                return True, user
        return False, None

    @staticmethod
    def createUser(fName, lName, contacts = [], isActive = True, isAdmin = False):
        """Creates a new user."""
        check, user = User.findUser(fName, lName)
        return user if check else User(fName, lName, contacts, isActive, isAdmin)

    def printAllUsers(self):
        """Prints all the active user"""
        if self.isAdmin and self.isActive:
            for user in User.allUsers:
                if user.isActive:
                    user.printUser()
    
    def printUser(self):
        """Prints the details of user"""
        print('Admin User') if self.isAdmin else print('Not a Admin User')
        print(f'UserID: {self.userID}')
        print(f'Full Name: {self.fName} {self.lName}')

    def updateUser(self, fName, lName):
        """Updates the user information."""
        if not self.isAdmin:
            print("Rights only for admin to update.")
            return False
        self.fName = fName
        self.lName = lName
        print("User details updated successfully!")

    def deleteUser(self):
        """Delete the user from database"""
        if not self.isAdmin:
            print("Rights only for admin to delete.")
            return False
        self.isActive = False
        print(f"User - ({self.fName} {self.lName}) has been deleted successfully!")

    # Class Contact Methods

    def findContact(self, fName, lName):
        for contact in self.contacts:
            if contact.fName == fName and contact.lName == lName:
                return True, contact
        return False, None

    def addContact(self, fName, lName, isActive = True, contactDetails = []):
        """Creates the new contact."""
        contactId = uuid.uuid4()
        newContact = Contact(contactId, fName, lName, isActive, contactDetails)
        self.contacts.append(newContact)
        print('Contact added successfully!')

    def readAllContacts(self):
        """Reads all the available contacts"""
        for contact in self.contacts:
            if contact.isActive == True:
                contact.printContact()

    def updateContact(self, fName, lName):
        flag, contact = self.findContact(fName, lName)
        if flag:
            firstName = input('Enter the updated first name: ')
            lastName = input('Enter the updated last name: ')
            contact.updateContact(firstName, lastName)

    def deleteContact(self, fName, lName):
        flag, contact = self.findContact(fName, lName)
        if not flag:
            print('Contact doesnot exist.')
            return False
        contact.isActive = False
        print('Contact deleted successfully.')
        return True
    
    # Class Contact Detail Methods

    def addContactDetails(self, fName, lName, infoType, info):
        flag, contact = self.findContact(fName, lName)
        if not flag:
            print('Contact doennot exist.')
            return False
        contactDetailId = uuid.uuid4()
        contact.addContactDetails(contactDetailId, infoType, info)
        return True

    def printContactDetails(self, fName, lName):
        flag, contact = self.findContact(fName, lName)
        if not flag:
            print('Contact doennot exist.')
            return False
        contact.printContactDetails()

    def updateContactDetail(self, fName, lName, index, infotype, info):
        flag, contact = self.findContact(fName, lName)
        if not flag:
            print('Contact doennot exist.')
            return False
        contact.updateContactDetail(index, infotype, info)
        print('Information updated succesfully.')

    def deleteContactDetail(self, fName, lName, index):
        flag, contact = self.findContact(fName, lName)
        if not flag:
            print('Contact doennot exist.')
            return False
        print('Information deleted successfully') if contact.deleteContactDetail(index) else print('Contact detail index doesnot exit')


if __name__ == "__main__":
    Shri = User.createUser('Shrijeet', 'Kharche', isAdmin=True)