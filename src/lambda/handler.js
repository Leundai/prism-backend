/**
 * Basic Lambda function handler for API Gateway
 * Phase 1: Minimal implementation for request/response flow
 */

exports.handler = async (event, context) => {
    console.log('Event:', JSON.stringify(event, null, 2));
    console.log('Context:', JSON.stringify(context, null, 2));

    try {
        // Extract basic request information
        const {
            httpMethod,
            path,
            queryStringParameters,
            body,
            headers
        } = event;

        // Basic response structure
        const response = {
            statusCode: 200,
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS'
            },
            body: JSON.stringify({
                message: 'Hello from Prism Lambda!',
                requestInfo: {
                    method: httpMethod,
                    path: path,
                    timestamp: new Date().toISOString()
                }
            })
        };

        return response;

    } catch (error) {
        console.error('Error:', error);
        
        return {
            statusCode: 500,
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            body: JSON.stringify({
                error: 'Internal Server Error',
                message: error.message
            })
        };
    }
};