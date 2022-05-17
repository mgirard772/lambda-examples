# AWS Lambda Examples

Examples of various types of Lambdas and deployment methods

## Requirements

- AWS CLI
- AWS SAM CLI
- Docker

## Commands

Create a function template (run inside functions folder)
```shell script
sam init --runtime python3.9 --dependency-manager pip --app-template hello-world --name hello-world-image --package-type Image
```

## References
[Using image support with SAM](https://aws.amazon.com/blogs/compute/using-container-image-support-for-aws-lambda-with-aws-sam/)


