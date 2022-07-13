

class ContactDetails:
    contactDetailsId = -1
    allContactDetails = []

    def __init__(self, infoType, info):
        ContactDetails.contactDetailsId += 1
        self.cdId = ContactDetails.contactDetailsId
        self.type = infoType
        self.info = info

    def printContact(self):
        print(f'{self.cdId}: Information Type - {self.type}, Information - {self.info}')

    @staticmethod
    def createContactDetails(infoType, info):
        newContactDetail = ContactDetails(infoType, info)
        ContactDetails.allContacts.append(newContactDetail)
        
        return newContactDetail, "Contact successfully created!"

    def readContactDetails(self):
        for i in ContactDetails.allContactDetails:
            i.printContactDetail()

    def updateContactDetails(self, infoType, info):
        self.type = infoType
        self.info = info
        return True, "User details updated successfully!"

class Contacts:
    contactId = -1
    allContacts = []
    
    def __init__(self, contactId, fName, lName, isActive, contactDetails = []):
        # self.__class__.allContacts.append(self)
        Contacts.contactId += 1
        self.contactId = Contacts.contactId
        self.fName, self.lName = fName, lName
        self.isActive = isActive
        self.contactDetails = contactDetails
    
    def printContact(self):
        print(f'Contact Name - {self.fName} {self.lName}')
        print('Active Contact') if self.isActive else print('Not a Active Contact')

    @staticmethod
    def findContact(fName, lName):
        """To find if the contact already exist."""            
        if i in Contacts.allContacts:
            if i.fName == fName and i.lName == lName:
                return True, i
        return False, None
        
    @staticmethod
    def createNewContact(fName, lName, isActive, contactDetails):
        isContactExist, _ = Contacts.findContact(fName, lName)
        if isContactExist:
            return False, "Contact already exist."

        newContact = Contacts(fName, lName, isActive, contactDetails)
        Contacts.allContacts.append(newContact)
        
        return newContact, "Contact successfully created!"

    def readContact(self):
        for i in Contacts.allContacts:
            i.printContact()

    def updateContact(self, fName, lName):
        self.fName = fName
        self.lName = lName
        return True, "User details updated successfully!"
        
    def deleteContact(self, isActive):
        self.isActive = False
        return True, f"User - ({self.fName} {self.lName}) has been deleted successfully!"

class User:
    userId = -1
    allUsers = []

    def __init__(self, fName, lName, isActive, contacts, isAdmin):
        """Constructor"""
        self.__class__.allUsers.append(self)
        User.userId += 1
        self.userId = User.userId
        self.fName, self.lName = fName, lName
        self.isAdmin, self.isActive = isAdmin, isActive
        self.contacts = []

    @staticmethod
    def findUser(fName, lName):
        """To find the presence of user."""
        if i in User.allUsers:
            if i.fName == fName and i.lName == lName:
                return True, i
        return False, None

    @staticmethod
    def createNewUser(fName, lName, isActive, contacts, isAdmin = False):
        """To create a new user."""
        isUserExist, userObject = User.findUser(fName, lName)
        if isUserExist:
            return False, "User already exist."
        return User(fName, lName, isActive, contacts, isAdmin)

    def printUser(self):
        print(f'User Name - {self.fName} {self.lName}')
        print('Active User') if self.isActive else print('Not a Active User')
        print('Admin User') if self.isAdmin else print('Not a Admin User')

    def __isUserActive(self):
        if self.isActive==False:
          print("you are not active cannot read contacts")
          return False 
        return True

    def readUsers(self):
        if not self.isAdmin:
            return False, "Only for admin to read"
        for i in self.allUsers:
            i.printUser()
        # return User.allUser
        return True

    def updateUser(self, fName, lName):
        if not self.isAdmin:
            return False, "Only for admin to read"
        self.fName = fName
        self.lName = lName
        return True, "User details updated successfully!"

    def deleteUser(self):
        if not self.isAdmin:
            return False, "Only for admin to read"
        self.isActive = False
        return True, f"User - ({self.fName} {self.lName}) has been deleted successfully!"

    def createContact(self, contactId, fName, lName):
        if self.isAdmin == True or self.isActive==False:
            print("Cnontact can not be added")
            return 
        newContact =  Contacts(contactId, fName, lName)
        self.contacts.append(newContact)

    def readContact(self, index):
        if self.isActive==False:
            print("you are not active cannot read contacts")
            return 
        contact =  self.contacts[index]
        print("contact ID is "+contact.contactId)
        print("contact First Name is "+contact.fName)
        print("contact lastName is "+contact.lName)
        return 

    def updateContacts(self,index,fName,lName):
        if self.isActive==False:
            print("you are not active cannot read contacts")
            return 
        contact =  self.contacts[index]
        contact.contacts(fName,lName)

    def deleteContact(self, index):
      if self.__isUserActive:
        self.contacts.pop(index)
    
    def readContactDetails(self, contactIndex, contactDetailsIndex):
      if self.__isUserActive:
        contact = self.contacts[contactIndex]
        contact.readContactDetails(contactDetailsIndex)
      return 

    def updateContactDetails(self,contacID,contactType,contactEmail,contactIndex,contactDetailsIndex):
      if self.__isUserActive:
         contact = self.contacts[contactIndex]
         contact.updateContactDetails(contactDetailsIndex,contacID,contactType,contactEmail)
      return 

    def deleteContactDetails(self,contactIndex,contactDetailsIndex):
      if self.__isUserActive:
            contact = self.contacts[contactIndex]
            contact.deleteContactDetails(contactDetailsIndex)
      return
        