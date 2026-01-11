import yfinance as yf
import json

def handler(event, context):
    # Get symbol from query params
    # event.body contains JSON if POST, event.queryString contains URL params
    params = event.get('queryStringParameters', {})
    symbol = params.get('symbol', 'AAPL')

    try:
        ticker = yf.Ticker(symbol)
        
        # Get History (for Graph) - Last 60 days
        hist = ticker.history(period="2mo", interval="1d")
        
        # Format data for Chart.js
        dates = hist.index.strftime('%Y-%m-%d').tolist()
        closes = hist['Close'].tolist()

        # Get Quote (for Price)
        info = ticker.info
        current_price = info.get('currentPrice') or 0
        prev_close = hist['Close'].iloc[-2] if len(hist) > 1 else current_price
        change = current_price - prev_close
        pct_change = (change / prev_close) * 100 if prev_close != 0 else 0

        response_data = {
            "symbol": symbol,
            "c": current_price,
            "d": change,
            "dp": pct_change,
            "chart": {
                "labels": dates,
                "data": closes
            }
        }

        return {
            'statusCode': 200,
            'body': json.dumps(response_data)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
