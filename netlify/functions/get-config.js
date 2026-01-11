// netlify/functions/get-config.js

exports.handler = async (event) => {
  try {
    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      // Sending FINNHUB_KEY
      body: JSON.stringify({
        DEEPSEEK_KEY: process.env.DEEPSEEK_KEY,
        FINNHUB_KEY: process.env.FINNHUB_KEY
      })
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message })
    };
  }
};
