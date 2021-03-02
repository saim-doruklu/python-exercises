import json


class AccountBook(dict):
    def __init__(self):
        dict.__init__(self)
        self.book = {}

    def add(self, user, amount):
        existing_amount = self.book.get(user) or 0
        self.book[user] = amount + existing_amount

    def reduce(self, user, amount):
        existing_amount = self.book.get(user)
        if existing_amount is not None:
            if amount < existing_amount:
                self.book[user] = existing_amount - amount
                return 0
            else:
                del self.book[user]
                return amount - existing_amount
        return amount

    def convert_to_dict(self):
        return {k.name: v for k, v in sorted(self.book.items(), key=lambda x: x[0].name)}


class User(dict):
    def __init__(self, name):
        dict.__init__(self)
        self.name = name
        self.owes = AccountBook()
        self.owed_by = AccountBook()
        self.balance = 0.0

    def add_owes(self, other_user, amount: float):
        remaining = self.owed_by.reduce(other_user, amount)
        if remaining > 0:
            self.owes.add(other_user, remaining)
        self.balance -= amount

    def add_owed_by(self, other_user, amount: float):
        remaining = self.owes.reduce(other_user, amount)
        if remaining > 0:
            self.owed_by.add(other_user, remaining)
        self.balance += amount

    def __eq__(self, other):
        return isinstance(other, User) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def convert_to_dict(self):
        converted = {'name': self.name,
                     'owes': self.owes.convert_to_dict(),
                     'owed_by': self.owed_by.convert_to_dict(),
                     'balance': self.balance}
        return converted


class RestAPI:

    def __init__(self, database=None):
        self.database = {}
        if database is not None:
            for user in database['users']:
                name = user['name']
                self.database[name] = User(name)
            for user in database['users']:
                this_user = self.database[user['name']]
                self.process_owes(this_user, user['owes'])
                self.process_owed_by(this_user, user['owed_by'])

    def process_owes(self, this_user, owes: dict[str, int]):
        for other_user_name in owes.keys():
            other_user = self.database[other_user_name]
            this_user.add_owes(other_user, owes[other_user_name])

    def process_owed_by(self, this_user, owed_by: dict[str, int]):
        for other_user_name in owed_by.keys():
            other_user = self.database[other_user_name]
            this_user.add_owed_by(other_user, owed_by[other_user_name])

    def get(self, url, payload=None):
        if url == "/users":
            if payload is None:
                return json.dumps({'users': [user.convert_to_dict() for user in self.database.values()]})
            else:
                user_names = sorted(json.loads(payload)['users'])
                return json.dumps({'users': [self.database[user_name].convert_to_dict() for user_name in user_names]})

    def post(self, url, payload=None):
        if url == "/add":
            name = json.loads(payload)['user']
            if self.database.get(name) is None:
                new_user = User(name)
                self.database[name] = new_user
                return json.dumps(new_user.convert_to_dict())
        elif url == "/iou":
            transaction = json.loads(payload)
            lender_name = transaction['lender']
            borrower_name = transaction['borrower']
            amount = float(transaction['amount'])
            lender = self.database[lender_name]
            borrower = self.database[borrower_name]
            lender.add_owed_by(borrower, amount)
            borrower.add_owes(lender, amount)
            sorted_users = sorted([lender_name, borrower_name])
            return json.dumps({'users': [self.database[user_name].convert_to_dict() for user_name in sorted_users]})
