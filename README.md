# Prism Backend

AWS Serverless backend using API Gateway and Lambda functions.

## Phase 1: Basic Setup

### Prerequisites
- AWS CLI configured
- SAM CLI installed
- Node.js 18+ installed

### Local Development
```bash
# Build the application
npm run build

# Start local API Gateway
npm run local

# Test single function locally
npm run test
```

### Deployment
```bash
# First time deployment (guided)
npm run deploy

# Subsequent deployments
npm run deploy-dev
```

### Architecture
- **API Gateway**: Entry point for all HTTP requests
- **Lambda Function**: Handles all routes with basic response
- **Stage**: Development stage configured for testing

### Testing
Once deployed, test the API:
```bash
curl https://your-api-gateway-url/dev/
```