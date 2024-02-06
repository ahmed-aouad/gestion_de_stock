
import mysql.connector

class Product:
    def __init__(self, db_config):
        self.db_config = db_config

    def connect_to_db(self):
        return mysql.connector.connect(**self.db_config)

    def add_product(self, name, description, price, quantity, id_category):
        db = self.connect_to_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)",
                       (name, description, price, quantity, id_category))
        db.commit()
        db.close()

    def update_product(self, product_id, name, description, price, quantity):
        db = self.connect_to_db()
        cursor = db.cursor()
        cursor.execute("UPDATE product SET name=%s, description=%s, price=%s, quantity=%s WHERE id=%s",
                       (name, description, price, quantity, product_id))
        db.commit()
        db.close()

    def delete_product(self, product_id):
        db = self.connect_to_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM product WHERE id=%s", (product_id,))
        db.commit()
        db.close()

    def get_all_products(self):
        db = self.connect_to_db()
        cursor = db.cursor()
        cursor.execute("SELECT product.id, product.name, description, price, quantity, category.name AS category_name FROM product JOIN category ON product.id_category = category.id")
        products = cursor.fetchall()
        db.close()
        return products

