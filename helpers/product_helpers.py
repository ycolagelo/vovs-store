from cs50 import SQL


def get_product(product_id):
    db = SQL("sqlite:///program.db")
    rows = db.execute("""
        SELECT p.name,
            c.name as "category_name",
            p.price,
            p.description,
            p.id
        FROM product p
        JOIN category c ON c.id = p.category_id
        where p.id = :product_id
        and p.active = 1
    """, product_id=product_id)

    if len(rows) < 1:
        return None

    return rows[0]


def get_product_images(product_id):
    db = SQL("sqlite:///program.db")
    rows = db.execute("""
        SELECT url, priority
        FROM product_image
        WHERE product_id = :product_id
        ORDER BY priority
    """, product_id=product_id)

    return rows


def get_top_products(num_products):
    db = SQL("sqlite:///program.db")
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


# Gets all active products along with 1 image for each. see above for example
def get_products():
    db = SQL("sqlite:///program.db")
    rows = db. execute("""
            select p.name, pi.url, p.id, p.price
            from product p
            join product_image pi on p.id = pi.product_id
            where pi.id IN(
                select id from product_image where product_id = p.id order by priority limit 1
            )
            and p.active = 1
    """)
    return rows


def get_purchased_products(user_id):
    db = SQL("sqlite:///program.db")
    rows = db.execute("""
        select p.name, p.price, p.id,  pi.url
        from product p
        join product_image pi on p.id = pi.product_id
        where p.id IN (
            select op.product_id
            from orders o
            join order_product op on o.id=op.order_id
            where user_id = :user_id
            group by product_id
        )
        and pi.id IN (
            select id from product_image where product_id = p.id order by priority limit 1
        )
        and p.active = 1;

    """, user_id=user_id)
    return rows


# def luhn(input):
#     digits = [int(c) for c in input if c.isdigit()]
#     checksum = digits.pop()
#     digits.reverse()
#     doubled = [2*d for d in digits[0::2]]
#     total = sum(d-9 if d > 9 else d for d in doubled) + sum(digits[1::2])
#     return (total * 9) % 10 == checksum
