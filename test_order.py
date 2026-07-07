from bot.orders import place_market_order

try:
    result = place_market_order(
        symbol="BTCUSDT",
        side="BUY",
        quantity=0.001
    )

    print("✅ Order Placed")

    print("Order ID:", result["orderId"])
    print("Status:", result["status"])

except Exception as e:
    print("❌ Order Failed")
    print(e)