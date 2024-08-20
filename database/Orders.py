from database.Database import Database


class OrderStatus:
    PENDING = 0
    ACCEPTED = 1
    PAID = 2
    COMPLETED = 3
    CANCELED = -1


class OrdersService:
    def __init__(self):
        self.db = Database()

    def getAll(self):
        self.db.cursor.execute("SELECT * FROM orders")
        return self.db.cursor.fetchall()

    def getById(self, id):
        self.db.cursor.execute("SELECT * FROM orders WHERE id = %s", (id,))
        return self.db.cursor.fetchone()

    def getByModeratorId(self, moderator_id):
        self.db.cursor.execute("SELECT * FROM orders WHERE moderator_id = %s", (moderator_id,))
        return self.db.cursor.fetchall()

    def getByStatus(self, status):
        self.db.cursor.execute('SELECT * FROM orders WHERE "status" = %s', [status])
        return self.db.cursor.fetchall()

    def getByCategoryId(self, category_id):
        self.db.cursor.execute("SELECT * FROM orders WHERE category_id = %s", (category_id,))
        return self.db.cursor.fetchall()

    def getByCategoryType(self, category_type):
        self.db.cursor.execute("SELECT * FROM orders WHERE category_id IN (SELECT id FROM categories WHERE category_type = %s)", (category_type,))
        return self.db.cursor.fetchall()

    def create(self, user_id, category_id, ceremony_date, single_person, photo_id, cheque_id):
        self.db.cursor.execute("INSERT INTO orders (user_id, category_id, ceremony_date, single_person, photo_id, cheque_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *",
                               (user_id, category_id, ceremony_date, single_person, photo_id, cheque_id))
        return self.db.cursor.fetchone()

    def setModeratorId(self, order_id, moderator_id):
        self.db.cursor.execute("UPDATE orders SET moderator_id = %s WHERE id = %s RETURNING *", (moderator_id, order_id))
        return self.db.cursor.fetchone()

    def completeOrder(self, order_id):
        self.db.cursor.execute("UPDATE orders SET status = %s WHERE id = %s RETURNING *", (OrderStatus.COMPLETED, order_id))
        return self.db.cursor.fetchone()

    def cancelOrder(self, order_id, reason):
        self.db.cursor.execute("UPDATE orders SET status = %s, cancel_reason = %s, canceled_at = NOW() WHERE id = %s RETURNING *", (OrderStatus.CANCELED, reason, order_id))
        return self.db.cursor.fetchone()