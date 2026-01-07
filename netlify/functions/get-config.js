// netlify/functions/get-config.js
exports.handler = async (event) => {
  return {
    statusCode: 200,
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    },
    body: JSON.stringify({
      DEEPSEEK_KEY: process.env.DEEPSEEK_KEY,
      POLYGON_KEY: process.env.POLYGON_KEY
    })
  };
};