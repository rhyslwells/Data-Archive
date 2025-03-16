Leader have aspiration however due to bad quality data not feasible.

Prevention: Caught at the source
Remediation: Observability, alerting, Complex ETL, erosion of trust
Failure: failure on opportunity cost, unable to meet business goals

the sooner we handle it the cheaper and easier it is 

Example: Software engineer: unit tests, wan to prevent bugs in production, observaility tools do help 

![[Pasted image 20250312161721.png|500]]

### Upstream breaking schema changes

Root cause analysis: [[Documentation]]
- 5 Y's
- Fishbone diagram: start at issue at head
- ![[Pasted image 20250312162034.png]]
- People and ownership: Who is entering the data: the source data

Why should product people (people producing the data) take on responsibility of the data quality? Do they understand how it is being used and how it generates value.

Data driven value - need to motivate it. 

Change management 
- Communication, knowledge


[[Data Contract]]

[[Change management]] - git repo

Build the interface from the data contract. 

![[Pasted image 20250312163351.png]]


![[Pasted image 20250312163618.png|800]]

Questions:

Q: If the data producers are not data teams, but business users. For example dumping data in google sheet or excel. With issues in naming conventions. Any suggestions for these type of data producers?
A: How to apply same patterns. Agreement on structure. Alerting and automating the change management. 

[[Data Observability]]



