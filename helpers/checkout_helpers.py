from cs50 import SQL
from helpers.cart_helpers import add_update_cart, get_full_cart, clear_cart
from constants.all import TRAN_TYPE_PURCHASE

# payment_info: { postal_code: string, cc_number: number, cc_name, cc_expiry, cvv }


def place_order(user_id, payment_info):
    db = SQL("sqlite:///program.db")
    cart = get_full_cart(user_id)
    order_id = db.execute("""
        insert into orders (created_date, user_id) 
        values (datetime(), :user_id)
   """, user_id=user_id)

    # Insert into orders (and order_product)/ oders=created date at user_id/ oder-product=quantity
    for cart_item in cart["items"]:
        db.execute("""
            insert into order_product (order_id, product_id, quantity)
            values (:order_id, :product_id, :quantity)
        """, order_id=order_id, product_id=cart_item["product_id"], quantity=cart_item["quantity"])

    # insert into tran
    db.execute("""
        insert into tran (amount, date, type, order_id)
        values (:amount, datetime(), :type, :order_id)
    """, amount=cart["finalTotal"], type=TRAN_TYPE_PURCHASE, order_id=order_id)

    # clear/empty the cart (implement and call clear_cart() in cart_helpers)
    clear_cart(cart["id"])

    # validate Credit card


def validate_credit_cart(credit_card):
    return True
