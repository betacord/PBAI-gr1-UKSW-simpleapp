from dataclasses import dataclass


@dataclass
class UserModel:
    id: int
    login: str
    password: str

    @classmethod
    def find_by_login(cls, login: str) -> 'UserModel':
        return [user for user in user_db if user.login == login][0]


user_db = [
    UserModel(id=0, login='user0', password='6d932c406fa15164ee48ff5a52f81dae'),
    UserModel(id=1, login='user1', password='ed71c5d55af657bc2413020e5580d4dd'),
]
