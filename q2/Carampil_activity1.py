1. #Public
class GameCharacter:
    def __init__(self, username):
        self.username = username
2. #Private
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
3. #Protected
class Vehicle:
    def __init__(self, engineCode):
        self._engineCode = engineCode
4. #Public
class Student:
    def __init__(self, schoolName):
        self.schoolName = schoolName
5. #Private
class VotingSystem:
    def __init__(self, voterID):
        self.__voterID = voterID
        