import database.Database


class UserTypeService:
    def __init__(self):
        self.db = database.Database.db

    def __get_user_type(self, type_name) -> int:
        self.db.cursor.execute("SELECT id FROM user_type WHERE type = %s", (type_name,))
        result = self.db.cursor.fetchone()
        return result['id'] if result else None

    def getCustomerType(self) -> int:
        return self.__get_user_type('CUSTOMER')

    def getModeratorType(self) -> int:
        return self.__get_user_type('MODERATOR')

    def getAdminType(self) -> int:
        return self.__get_user_type('ADMIN')