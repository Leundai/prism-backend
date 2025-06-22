# Prism Backend - Project Memory

## Architecture Approach

### Phase 1: Initial Setup

- **API Gateway**: AWS API Gateway as entry point
- **Lambda Function**: Keep the Lambda function bare/minimal initially
- **Goal**: Establish basic request/response flow for testing and iteration

### Phase 2: Event Processing Integration

- **Queue/Event Service**: Add integration with either:
  - **SQS** (Simple Queue Service) - for reliable message queuing
  - **EventBridge** - for event-driven architecture patterns
- **Decision Point**: Choose between SQS vs EventBridge based on specific needs:
  - SQS: Better for simple message queuing, high throughput
  - EventBridge: Better for complex event routing, multiple targets

### Development Strategy

- Start simple with bare Lambda to validate API Gateway integration
- Gradually add complexity with queue/event processing
- Keep Lambda lightweight for easier debugging and faster cold starts
