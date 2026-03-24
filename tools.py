def calculator_tool(query):
    try:
        result = eval(query)
        return f"Result is {result}"
    except:
        return "Sorry, I cannot calculate that."


def order_status_tool(order_id):
    orders = {
        "123": "Shipped",
        "456": "Out for delivery",
        "789": "Delivered"
    }

    return orders.get(order_id, "Order not found")