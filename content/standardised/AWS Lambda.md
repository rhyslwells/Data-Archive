---
aliases: []
category:
date modified: 1-08-2025
tags: []
---
AWS Lambda is a serverless computing service provided by Amazon Web Services (AWS) that allows you to run code without provisioning or managing servers. 

AWS Lambda is a powerful tool for building scalable, event-driven applications without the overhead of managing server infrastructure.

With AWS Lambda, you can execute your code in response to various events, such as HTTP requests via Amazon API Gateway, changes to data in an [[Amazon S3]] bucket, updates to a DynamoDB table, or messages arriving in an Amazon SQS queue.

Key features of AWS Lambda include:

1. **[[Event Driven Events]]**: AWS Lambda functions are triggered by events, which can come from a wide range of AWS services or custom applications.

2. **Automatic Scaling**: Lambda automatically scales your application by running code in response to each trigger. Your code runs in parallel and processes each trigger individually, scaling precisely with the size of the workload.

3. **Pay-as-You-Go**: You are charged based on the number of requests for your functions and the time your code executes. This means you only pay for the compute time you consume.

4. **No Server Management**: AWS Lambda abstracts the underlying infrastructure, so you don't need to manage servers, patch operating systems, or worry about scaling.

5. **Supports Multiple Languages**: AWS Lambda supports several [[programming languages]], including Python, Java, [[Node.js]], C#, Ruby, and Go, among others.

6. **Integration with AWS Services**: Lambda integrates seamlessly with other AWS services, allowing you to build complex, scalable applications.

Here's a simple example of how AWS Lambda might be used:

- You have an [[Amazon S3]]] where users upload images.
- An AWS Lambda function is triggered whenever a new image is uploaded.
- The Lambda function processes the image, such as generating thumbnails or extracting metadata.
- The processed data is then stored back in S3 or sent to another AWS service for further processing.