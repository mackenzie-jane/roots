class Account:

    def __init__(self, name, community, interests):

        self.name = name

        self.community = community

        self.interests = interests

    def getName(self):

        return self.name

    def getCommunity(self):

        return self.community

    def getInterests(self):

        return self.interests



def accounts():

    account1 = Account("Saif Chaudhry", "Pakistani", "Interest Blank")
    account2 = Account("Mackenzie Linn", "Scottish and Irish", "Interest Blank")
    account3 = Account("Emma Noonan", "Italian and Irish", "Interest Blank")

    return account1, account2, account3