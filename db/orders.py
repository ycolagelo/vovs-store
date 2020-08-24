from cs50 import SQL
from datetime import datetime


def get_orders_by_user(user_id):
    db = SQL("sqlite:///program.db")
    rows = db.execute("""
        select p.name as "product_name",
            o.id as "order_id",
            op.quantity,
            pi.url as "image_url",
            o.created_date,
            p.price,
            p.id as "product_id"
        from orders o
        join order_product op on o.id = op.order_id
        join product p on p.id = op.product_id
        join product_image pi on p.id = pi.product_id
        where pi.id IN (
            SELECT id from product_image where product_id = p.id order by priority limit 1
        )
        and user_id = :user_id
        order by order_id
    """, user_id=user_id)

    # group the rows by order
    orders = {}  # key is order_id
    for row in rows:
        order_id = row["order_id"]
        if order_id in orders:
            orders[order_id]["products"].append(row)
        else:
            orders[order_id] = {}
            orders[order_id]["order_id"] = row["order_id"]
            orders[order_id]["created_date"] = row["created_date"]

            # Add formatted date
            dt = datetime.strptime(
                row["created_date"], "%Y-%m-%d %H:%M:%S")
            orders[order_id]["created_date_formatted"] = dt.strftime(
                "%b %d %Y %H:%M")

            orders[order_id]["products"] = []
            orders[order_id]["products"].append(row)

    # Calculate order totals
    for order in orders.values():
        total = 0
        items = order["products"]
        for item in items:
            total += item["price"]

        order["total"] = total

    return orders
