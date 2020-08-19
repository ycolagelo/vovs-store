from cs50 import SQL

db = SQL("sqlite:///program.db")

def is_product_in_cart(cart_id, product_id):
    rows = db.execute("""
        select id
        from cart_product
        where cart_id=:cart_id
        and product_id=:product_id
    """, cart_id=cart_id, product_id=product_id)
    if len(rows) > 0:
        return True
    else:
        return False

def create_cart(user_id):
    rows = db.execute("""
        insert into cart (user_id, state, created_date)
        values (:user_id, 0, datetime());
    """, user_id=user_id)

def get_cart(user_id):
    rows = db.execute("""
        SELECT id, user_id, state
        FROM cart
        WHERE user_id=:user_id;
    """, user_id=user_id)
    if len(rows) > 0:
        return rows[0]
    else:
        # Cart does not exist, create one
        create_cart(user_id)
        # Then call itself to return the new id
        return get_cart(user_id)

def get_cart_count(cart_id, product_id):
    rows = db.execute("""
        select quantity
        from cart_product
        where cart_id = :cart_id
        and product_id = :product_id
    """, cart_id=cart_id, product_id=product_id)
    if len(rows) != 1:
        return 0
    return rows[0]['quantity']

def update_cart_count(cart_id, product_id, new_count):
    # make sure to check if the qty < 1 (i.e. removed)
    if new_count < 1:
        # Delete
        db.execute("""
            delete from cart_product
            where product_id=:product_id
            and cart_id=:cart_id
        """, product_id=product_id, cart_id=cart_id)
    else:
        # Update
        db.execute("""
            update cart_product
            set quantity=:new_count
            where product_id=:product_id
            and cart_id=:cart_id
        """, product_id=product_id, cart_id=cart_id, new_count=new_count)

# count: the amount you are incrementing/decrementing the product
def add_update_cart(product_id, new_count, user_id):
    cart = get_cart(user_id)

    # Check if product exists in the cart already
    if is_product_in_cart(cart['id'], product_id):
        # if yes, UPDATE the count of the product in the cart
        update_cart_count(cart['id'], product_id, new_count)
    else:
        # if no, INSERT the new product into the cart
        db.execute("""
            insert into cart_product (cart_id, product_id, quantity)
            values (:cart_id, :product_id, :quantity)
        """, cart_id=cart['id'], product_id=product_id, quantity=new_count)


def get_image_for_product_cart(product_id):
    db.execute(""" 
            Select url from product_image where product_id=:product_id
    """, product_id = product_id)
    
def get_product_price(prodct_id):
    db.execute("""
            select price from product where id=:product_id
    """)

    