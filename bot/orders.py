from bot.client import get_client
from bot.logging_config import logger

client = get_client()


def place_market_order(symbol, side, quantity):
    try:
        logger.info(
            f"MARKET Order Request: {symbol} {side} {quantity}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"Response: {response}")

        return response

    except Exception as e:
        logger.error(f"Market Order Error: {str(e)}")
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        logger.info(
            f"LIMIT Order Request: {symbol} {side} {quantity} @ {price}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"Response: {response}")

        return response

    except Exception as e:
        logger.error(f"Limit Order Error: {str(e)}")
        raise