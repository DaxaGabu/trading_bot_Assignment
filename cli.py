import argparse

from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from bot.orders import (
    place_market_order,
    place_limit_order
)


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()

    try:

        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        print("\n===== ORDER REQUEST =====")
        print("Symbol:", symbol)
        print("Side:", side)
        print("Type:", order_type)
        print("Quantity:", quantity)

        if order_type == "MARKET":

            result = place_market_order(
                symbol=symbol,
                side=side,
                quantity=quantity
            )

        else:

            if not args.price:
                raise ValueError(
                    "Price is required for LIMIT orders"
                )

            price = validate_price(args.price)

            print("Price:", price)

            result = place_limit_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price
            )

        print("\n===== ORDER RESPONSE =====")
        print("Order ID:", result.get("orderId"))
        print("Status:", result.get("status"))
        print("Executed Qty:", result.get("executedQty"))

        if "avgPrice" in result:
            print("Avg Price:", result["avgPrice"])

        print("\n✅ Order Successful")

    except Exception as e:

        print("\n❌ Order Failed")
        print(e)


if __name__ == "__main__":
    main()