#kafka-consumer-example

Creates a simple function that will consume messages from Kafka using a Kafka topic as an event source.

## Requirements
- Local Kafka scripts (for producing messages)
- Kafka setup in AWS (EC2 or MSK)

## Setup
Follow these guides to setup your VPC and Kafka cluster:
- https://aws.amazon.com/blogs/compute/using-self-hosted-apache-kafka-as-an-event-source-for-aws-lambda/
- https://aws.amazon.com/blogs/compute/setting-up-aws-lambda-with-an-apache-kafka-cluster-within-a-vpc/

Create a `samconfig.toml` file for easy deployment.
## Usage

Produce a message to the Kafka topic (run inside kafka bin folder)
```shell script
./kafka-console-producer.sh --bootstrap-server $KAFKA_ADDRESS --topic $TOPIC
```

Monitor lamdba logs in real-time
```shell script
aws logs tail "/aws/lambda/your-lambda-name" --follow
```

Local invocation
```shell script
sam local invoke -e event.json
```

Build
```shell script
sam build
```

Deploy
```shell script
sam deploy --resolve-image-repos --resolve-s3
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

- Your VPC/Subnets must have either a NAT Gateway or VPC Endpoints setup 
to allow access to Lambda, STS, and SecretsManager.

## References
[AWS::Lambda::EventSourceMapping](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html)

