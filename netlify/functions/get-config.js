// netlify/functions/get-config.js

exports.handler = async (event) => {
  try {
    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      // CHANGED: Sending TWELVEDATA_KEY instead of POLYGON_KEY
      body: JSON.stringify({
        DEEPSEEK_KEY: process.env.DEEPSEEK_KEY,
        TWELVEDATA_KEY: process.env.TWELVEDATA_KEY
      })
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message })
    };
  }
};
