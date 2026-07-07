from bot.validators import *

try:
    print(validate_symbol("BTCUSDT"))
    print(validate_side("BUY"))
    print(validate_order_type("MARKET"))
    print(validate_quantity(0.01))

    print("✅ Validation Passed")

except Exception as e:
    print("❌ Validation Failed")
    print(e)