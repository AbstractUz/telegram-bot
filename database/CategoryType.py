import database.Database


class CategoryTypeService:
    def __init__(self):
        self.db = database.Database.db

    def getAllCategoryTypes(self):
        self.db.cursor.execute("SELECT * FROM category_type ct WHERE ct.deleted_at IS NULL")
        return self.db.cursor.fetchall()

    def getById(self, id):
        self.db.cursor.execute("SELECT * FROM category_type WHERE id = %s AND deleted_at IS NULL", (id,))
        return self.db.cursor.fetchone()

    def getCategoryType(self, category_type_id):
        self.db.cursor.execute("SELECT * FROM category_type WHERE id = %s AND deleted_at IS NULL", (category_type_id,))
        return self.db.cursor.fetchone()

    def createCategoryType(self, name_uz, name_ru, name_en, single_price, group_price):
        self.db.cursor.execute("INSERT INTO category_type (name_uz, name_ru, name_en, single_price, group_price) VALUES (%s, %s, %s, %s, %s) RETURNING *", (name_uz, name_ru, name_en, single_price, group_price))
        return self.db.cursor.fetchone()

    def deleteCategoryType(self, category_type_id):
        self.db.cursor.execute("UPDATE category_type SET deleted_at = NOW() WHERE id = %s RETURNING id", (category_type_id,))
        return self.db.cursor.fetchone()