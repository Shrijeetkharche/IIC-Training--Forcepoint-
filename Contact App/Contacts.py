from ContactDetails import ContactDetails

class Contact:
    def __init__(self, contactId, fName, lName, isActive, contactDetails):
        self.contactId = contactId
        self.fName = fName
        self.lName = lName
        self.isActive = isActive
        self.contactDetails = contactDetails

    def printContact(self):
        print(f'Contact ID: {self.contactId}')
        print(f'Contact Name: {self.fName} {self.lName}')
        for item in ContactDetails:
            item.readContactDetail()

    def updateContact(self, fName, lName):
        if not self.isActive:
            print('Cannot update inactive contact.')
            return False
        self.fName = fName
        self.lName = lName
        print('Contact successfully updated!')
        return True

    # Class Contact Detail Methods

    def findContactDetail(self, index):
        for item in self.contactDetails:
            if item.contactDetailId == index:
                return True, item
        return False, None

    def addContactDetail(self, contactDetailId, infoType, info):
        newContactDetail = ContactDetails(contactDetailId, infoType, info)
        self.contactDetails.append(newContactDetail)
        print('Contact Detail Successfully added')

    def printContactDetail(self):
        for cd in self.contactDetails:
            cd.readContactDetail()

    def updateContactDetail(self, index, infoType, info):
        flag, contactDetail = self.findContactDetail(index)
        if not flag:
            print('Contact Detail doesnot exist')
            return False
        contactDetail.updateContactDetail(infoType, info)
        return True

    def deleteContactDetail(self, index):
        for i in range(len(self.contactDetails)):
            if self.contactDetails[i].contactDetailId == index:
                self.contactDetails.pop(i)
                return True
        return False
                
        
