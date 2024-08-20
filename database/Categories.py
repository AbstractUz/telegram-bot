from database.Database import Database


class CategoriesService:
    def __init__(self):
        self.db = Database()

    def getAll(self):
        self.db.cursor.execute("SELECT * FROM categories WHERE deleted_at IS NULL")
        return self.db.cursor.fetchall()

    def getByType(self, type_id):
        self.db.cursor.execute("SELECT * FROM categories WHERE category_type = %s AND deleted_at IS NULL", (type_id,))
        return self.db.cursor.fetchall()

    def getById(self, id):
        self.db.cursor.execute("SELECT * FROM categories WHERE id = %s AND deleted_at IS NULL", (id,))
        return self.db.cursor.fetchone()

    def create(self, name, photo, type_id):
        self.db.cursor.execute("INSERT INTO categories (name, photo_id, category_type) VALUES (%s, %s, %s) RETURNING *", (name, photo, type_id))
        return self.db.cursor.fetchone()

    def delete(self, id):
        self.db.cursor.execute("UPDATE categories SET deleted_at = NOW() WHERE id = %s RETURNING id", (id,))