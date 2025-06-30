# Todo App with Flask and AWS Lambda

## Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app locally:
```bash
python app.py
```

## Testing
Run tests with:
```bash
python -m unittest tests/test_app.py
```

## Deployment to AWS Lambda
1. Create ECR repository:
```bash
aws ecr create-repository --repository-name todo-app
```

2. Configure GitHub Secrets:
   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_REGION

3. Push to main branch triggers deployment

## CI/CD Pipeline
- Builds Docker image on push to main
- Pushes image to Amazon ECR
- Updates AWS Lambda function
