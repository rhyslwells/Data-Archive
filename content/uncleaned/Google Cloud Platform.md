Compute engine

1. **Overview**: Google Cloud Platform is a suite of cloud computing services offered by Google. It provides a range of services including computing, storage, and application development that run on Google hardware.

2. **Compute Engine**: This is GCP's Infrastructure as a Service (IaaS) offering, which allows users to run virtual machines on Google's infrastructure. It provides scalable, high-performance virtual machines with flexible configurations.

3. **Features of Compute Engine**:
   - **Custom Machine Types**: Allows you to create virtual machines with custom configurations to fit your specific needs.
   - **Preemptible VMs**: Cost-effective, short-lived instances suitable for batch jobs and fault-tolerant workloads.
   - **Sustained Use Discounts**: Automatic discounts for running workloads for a significant portion of the billing month.
   - **Per-second Billing**: Charges are calculated per second, allowing for cost savings on workloads that do not require full-hour usage.

4. **Use Cases**: Compute Engine is suitable for a variety of use cases, including web hosting, data processing, and running large-scale applications.

5. **Integration with Other GCP Services**: Compute Engine integrates seamlessly with other GCP services like Google Kubernetes Engine, Cloud Storage, and BigQuery, allowing for a comprehensive cloud solution.

bigtable

app engine

bigquerry 

GCP cloud storage

GCP SQL

GCP CICD

[[Firebase]]

Resources:
[Introduction to Google Cloud](https://www.youtube.com/watch?v=IeMYQ-qJeK4)

[[Google Cloud Platform]]
see youtube vid of what this is
there is generic repo for this.

For me at a later date: Setup up my own GCP example.

When demand for compute increases: 
- scaling horizontally (adding more servers) or vertically (adding memory or cpu)
- scaling horizontally is preferable. 

With many severs need to do [[load balancing]]:
- there are many roles this can take and it does.

[[Relational Database]]
- uses In memory-cache: pre database

Want to cache images/ local data near the user instead of accessing the service.

There are cloud versions of all these based on the level of specifisity needed.