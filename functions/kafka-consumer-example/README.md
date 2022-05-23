# kafka-consumer-example
Creates a simple function that will consume messages from Kafka using a Kafka topic as an event source.

## Requirements
- Local Kafka scripts (for producing messages)
- Kafka setup in AWS (EC2 or MSK)
- AWS CLI
- AWS SAM
- Docker

## Setup
1. Setup a Kafka cluster in EC2 You can also use MSK, but will have to modify the template a bit. See guides in [References](#references)
2. Ensure you VPC is setup with a NAT Gateway or VPC endpoints for accessing Lambda, STS and Secrets Manager.
3. Create a .env file with all the necessary fields referenced in samconfig-template.toml
4. Run `make config` to generate your `samconfig.toml` file.
5. Run `make build` to have SAM build your image and template
6. Run `make deploy` to deploy your lambda function to AWS

If you make changes to your config, function or template, just run the specific `make` command or `make all` again.

## Usage
Generate config file
```shell script
make config
```

Build function image
```shell script
make build
```

Local invocation. This is to test how your function will handle an event.
```shell script
sam local invoke -e event.json
```

Deploy
```shell script
make deploy
```

Configure, Build and Deploy
```shell script
make all
```

Monitor lamdba logs in real-time
```shell script
sam logs --name lambdaconsumertest --stack-name lambda-consumer-test-sam --tail
```

## Event Format
```json
{
   "eventSource":"aws:kafka",
   "eventSourceArn":"arn:aws:kafka:sa-east-1:123456789012:cluster/vpc-2priv-2pub/751d2973-a626-431c-9d4e-d7975eb44dd7-2",
   "records":{
      "mytopic-0":[
         {
            "topic":"mytopic",
            "partition":0,
            "offset":15,
            "timestamp":1545084650987,
            "timestampType":"CREATE_TIME",
            "value":"SGVsbG8sIHRoaXMgaXMgYSB0ZXN0Lg==",
            "headers":[
               {
                  "headerKey":[
                     104,
                     101,
                     97,
                     100,
                     101,
                     114,
                     86,
                     97,
                     108,
                     117,
                     101
                  ]
               }
            ]
         }
      ]
   }
}

```

## Gotchas
- Your Subnet/VPC must have either a NAT Gateway or VPC Endpoints setup 
to allow access to Lambda, STS, and SecretsManager. These endpoints must be associated with the security groups associated with
the Kafka brokers.

## References
- [AWS::Lambda::EventSourceMapping](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html)
- [Using Lambda with self-managed Kafka] (https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html)
- [EventSource::SelfManagedKafka](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-selfmanagedkafka.html)
- [Setup Lambda with self-hosted Kafka in a VPC](https://aws.amazon.com/blogs/compute/setting-up-aws-lambda-with-an-apache-kafka-cluster-within-a-vpc/)
- [Using self-hosted Kafka as an event source for Lambda](https://aws.amazon.com/blogs/compute/using-self-hosted-apache-kafka-as-an-event-source-for-aws-lambda/)

