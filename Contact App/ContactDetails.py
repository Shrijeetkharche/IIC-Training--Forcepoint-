class ContactDetails:
    def __init__(self, contactDetailId, infoType = '', info = ''):
        self.contactDetailId = contactDetailId
        self.infoType = infoType
        self.info = info

    def readContactDetails(self):
        print(f'Contact Detail ID: {self.contactDetailId}')
        print(f'Type: {self.infoType}')
        print(f'Information: {self.info}')

    def updateContactDetails(self, infoType, info):
        self.infoType = infoType
        self.info = info

