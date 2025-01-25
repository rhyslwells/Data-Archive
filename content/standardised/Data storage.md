---
title: 
tags: 
aliases: 
category:
---

- Storage underpins every aspect of Data Engineering
    - ingestion, transformation, queries
- Many Cloud Computing Services already exists [**AWS, GCP, Azure**]
    - Pick the one your company uses

|Storage|Description|
|---|---|
|Object Stores|Gold standard for data lakes|

Inherently key-values stores

Ideal for unstructured data such as images, audio, text | | Relational Databases | The most widely deployed DB in the world is not PostgreSQL or MySQL…it’s SQLite! Surprise surprise

Often times the solution to most Data Engineering problems

Extremely fast lookup time |


## Amazon S3 buckets (onedrive essentially)

Amazon Simple Storage Service (S3) is a versatile ==object storage solution== known for its scalability, data availability, security, and performance.

Stands for Simple Storage Service.

**What is Amazon S3?**

It's an object storage service, allowing you to upload and store various types of objects, including images, text, videos, and more. S3's structure resembles that of a typical file system, with folders, subfolders, and files. Notably, it's extremely cost-effective, with storage costs starting at only 0.023 cents per GB, and it offers high durability with data replicated across three availability zones.

**Why is Amazon S3 Useful?**

1. **Cost-Effective Storage**: S3 provides cheap, reliable storage for objects of any type.
2. **Low Latency, High Throughput**: It offers fast access to your data, making it suitable for hosting static websites.
3. **Integration with AWS Services**: S3 can be integrated with other AWS services like SNS, SQS, and Lambda for powerful event-driven applications.
4. **Lifecycle Management**: S3 offers lifecycle management to automatically transition data to lower-cost storage tiers based on access patterns.

**Step-by-Step Walkthrough in the AWS Console**

1. **Creating a Bucket**: Start by navigating to the AWS Management Console and selecting S3. Create a bucket with a unique name and choose the region closest to your application.
2. **Uploading a File**: Once the bucket is created, upload a file using the console. You can add metadata and set permissions as needed.
3. **Exploring Settings**: Dive into bucket settings to configure options like versioning, logging, encryption, and lifecycle management. Block public access to ensure data security.

**Additional Features**

1. **Transfer Acceleration**: Accelerate data transfer to and from S3 using optimized network paths.
2. **Events**: Configure event notifications to trigger actions in response to S3 events like object creation or deletion.
3. **Requester Pays**: Enable Requester Pays to allow bucket owners to pass on data transfer costs to requesters.