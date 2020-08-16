from cs50 import SQL

db = SQL("sqlite:///program.db")

def get_product(product_id):
    rows = db.execute("""
        SELECT p.name,
            c.name as "category_name",
            p.price,
            p.description
        FROM product p
        JOIN category c ON c.id = p.category_id
        where p.id = :product_id
        and p.active = 1
    """, product_id=product_id)

    if len(rows) < 1:
        return None

    return rows[0]

def get_product_images(product_id):
    rows = db.execute("""
        SELECT url, priority
        FROM product_image
        WHERE product_id = :product_id
        ORDER BY priority
    """, product_id=product_id)

    return rows

def get_top_products(num_products):
    rows = db.execute("""
        select p.name, pi.url, p.id
        from product p
        join product_image pi on p.id = pi.product_id
        where p.active = 1
        group by p.id, p.name
        having pi.priority = min(pi.priority)
        limit :num_products
    """, num_products=num_products)

    return rows
