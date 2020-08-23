from cs50 import SQL
from constants.all import FIXED_SHIPPING_COST, FIXED_HANDLING_COST, CART_STATE_ACTIVE, CART_STATE_COMPLETE

db = SQL("sqlite:///program.db")

# Assumption: User only has one cart in the DB.
# If we want to support multiple, we need to use the 'state'
# column in cart to determine if a cart is active or not


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
    db.execute("""
        insert into cart (user_id, state, created_date)
        values (:user_id, :state, datetime());
    """, user_id=user_id, state=CART_STATE_ACTIVE)


def get_cart(user_id):
    rows = db.execute("""
        SELECT id, user_id
        FROM cart
        WHERE user_id=:user_id
        state = :state
    """, user_id=user_id, state=CART_STATE_ACTIVE)
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
    """, cart_id=cart_id, product_id=product_id, state=CART_STATE_ACTIVE)
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


def get_full_cart(user_id):
    rows = db.execute("""
        select c.id, p.name, cp.quantity, pi.url, p.price, cp.product_id
        from cart c
        join cart_product cp on cp.cart_id = c.id
        join product p on p.id = cp.product_id
        join product_image pi on p.id = pi.product_id
        where pi.id IN (
            SELECT id from product_image where product_id = p.id order by priority limit 1
        )
        and c.user_id = :user_id
        and state = :state
    """, user_id=user_id, state=CART_STATE_ACTIVE)

    cart = {}
    cart['items'] = rows

    cart_id = -1
    if len(rows) > 0:
        cart_id = rows[0]["id"]
    cart["id"] = cart_id

    totalPrice = 0
    for row in rows:
        totalPrice += (row['price'] * row['quantity'])
    cart['subtotal'] = round(totalPrice, 2)
    cart['hst'] = totalPrice * 0.13
    cart['shipping'] = FIXED_SHIPPING_COST
    cart['handling'] = FIXED_HANDLING_COST
    cart['finalTotal'] = round(totalPrice + cart['hst'] +
                               cart['shipping'] + cart['handling'], 2)

    return cart


def clear_cart(cart_id):
    db.execute("""
        update cart set state = :state
        WHERE id=:cart_id
    """, cart_id=cart_id, state=CART_STATE_COMPLETE)
