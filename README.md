# Binance Futures Testnet Trading Bot

## Features

- Market Orders
- Limit Orders
- BUY / SELL Support
- Input Validation
- Logging
- Error Handling

## Setup

pip install -r requirements.txt

## Configure

Create .env file

BINANCE_API_KEY=YOUR_KEY
BINANCE_SECRET_KEY=YOUR_SECRET

## Run Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

## Run Limit Order

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000

## Assumptions

- Binance Futures Testnet Account
- USDT-M Futures