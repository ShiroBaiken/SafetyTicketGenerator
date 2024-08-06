import bcrypt
from pymongo import MongoClient


class LoginManipulator:
    def __init__(self, cli: MongoClient, collection: str = 'logins'):
        self.db = cli.questions_generator
        self.collection = collection

    def pass_check(self, login: str, password: str):
        log_pairs = self.db[self.collection].find({login: {"$exists": True}})
        if log_pairs:
            for log_pair in log_pairs:
                if bcrypt.checkpw(bytes(password, 'utf-8'), bytes(log_pair[login], 'utf-8')):
                    return True
            else:
                return False
        else:
            return False

    def add_new_pair(self, login, password):
        hashed_pass = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        self.db[self.collection].insert_one({login: hashed_pass})

    def delete_one(self, login, password):
        users = self.db[self.collection].find({login: {"$exists": True}})
        valid = [x for x in users if bcrypt.checkpw(bytes(password, 'utf-8'), bytes(x[login], 'utf-8'))]
        if valid:
            self.db[self.collection].delete_one({login: valid[0][login]})
        else:
            pass




