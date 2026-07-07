from bot.client import get_client

try:
    client = get_client()

    balance = client.futures_account_balance()

    print("✅ Connected Successfully!")

    for asset in balance:
        if asset["asset"] == "USDT":
            print("USDT Balance:", asset["balance"])

except Exception as e:
    print("❌ Connection Failed")
    print(e)