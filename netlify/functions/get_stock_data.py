import yfinance as yf
import json
import os

def handler(event, context):
    # Determine symbol from query param
    # Netlify passes query params in event.queryStringParameters
    try:
        # Try to parse query string
        # Standard URL: ?symbol=AAPL
        # Netlify Proxy: event.queryStringParameters
        params = event.get('queryStringParameters', {})
        
        if 'symbol' not in params:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing symbol parameter'})
            }
        
        symbol = params['symbol'][0].upper() # Ensure uppercase

        print(f"Fetching data for {symbol}...")

        ticker = yf.Ticker(symbol)
        
        # Get History (for Graph) - Last 3 months (Daily data)
        # Using 'period' instead of specific dates for speed
        hist = ticker.history(period="3mo", interval="1d")
        
        # Format data for Chart.js
        # We reverse it so the latest date is last (standard chart flow)
        hist = hist.iloc[::-1]
        
        dates = hist.index.strftime('%Y-%m-%d').tolist()
        closes = hist['Close'].tolist()
        opens = hist['Open'].tolist()
        highs = hist['High'].tolist()
        lows = hist['Low'].tolist()
        
        # Prepare response
        response_data = {
            "symbol": symbol,
            "chart": {
                "labels": dates,
                "data": closes
            }
        }

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(response_data)
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
