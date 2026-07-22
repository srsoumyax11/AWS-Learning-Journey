# AWS Learning Journey — Series Roadmap
> Last updated: July 2026
> This is a living document. Update as the series grows.

---

## 🟢 Published

**Ch 00 — Before You Learn AWS: The Story Behind the Cloud**
The origin story. Why does AWS exist at all? Hook readers with the food app analogy. Covers the pain of the old world at a high level. Sets the tone for the whole series — storytelling first, jargon never.
https://dev.to/srsoumyax11/before-you-learn-aws-the-story-behind-the-cloud-2bed

**Ch 01 — The World Before AWS: Computers, Servers & The Internet**
Fast-moving backstory chapter. What is a computer, a server, the internet, a data center — just enough to understand the problem. Ends with the three core failures of the old world: slow to scale, brutally expensive, yours to maintain.
https://dev.to/srsoumyax11/the-world-before-aws-computers-servers-the-internet-3m0

---

## 🔵 Planned — Foundation

**Ch 02 — Virtualization & Cloud Models: The Missing Bridge**
The technical "how" behind cloud computing. How one physical machine became many virtual ones (hypervisors, Type 1 vs Type 2). Then IaaS vs PaaS vs SaaS explained simply. This chapter makes EC2 make sense before we even open AWS.
https://dev.to/srsoumyax11/virtualization-cloud-models-the-missing-bridge-f60

**Ch 03 — Welcome to AWS: Infrastructure, Console & Free Tier**
First look inside AWS. Global infrastructure — Regions, Availability Zones, Edge Locations and why they matter. Console orientation so readers don't panic when they log in. Free tier explained clearly — what's free, for how long, and how to not get a surprise bill.

https://dev.to/srsoumyax11/welcome-to-aws-infrastructure-console-free-tier-2909

**Ch 04 — IAM: The Gatekeeper of AWS**
Security before everything. What IAM is, why the root account should be locked away immediately, users vs groups vs roles vs policies. MFA setup. Shared Responsibility Model — what AWS secures vs what you secure. Every reader must finish this before touching any other service.

---

## 🔵 Planned — Compute

**Ch 05 — EC2: Your First Server in the Cloud**
The flagship AWS service. Rohit provisions the server, Aarav deploys the code. Launch a virtual server, understand instance types, configure security groups and key pairs. Connect via EC2 Instance Connect. Introduces the Pixel & Spoon Node.js app and the series GitHub repo.

**Ch 05.1 — All Four Ways to Connect to EC2**
Hands-on companion. EC2 Instance Connect (browser), SSH on Mac/Linux, SSH on Windows (icacls method), SSM Session Manager, EC2 Serial Console. Decision table for which to use when.

**Ch 06 — EBS, AMI & Auto Scaling: The Complete Compute Picture**
Three services, one resilience story. EBS for persistent storage that survives server restarts. AMI to create a golden image of the configured server. ELB + ASG to handle traffic spikes automatically. Pixel & Spoon goes from one fragile server to a resilient, scalable setup.

---

## 🔵 Planned — CLI & Developer Tools

**Ch 07 — AWS CLI: Stop Clicking, Start Typing**
The leap from console to command line. Install and configure the AWS CLI. Run real commands — launch an instance, list S3 buckets, check IAM users. Why this matters for automation and real-world work. Readers finish feeling like they levelled up.

---

## 🔵 Planned — Storage

**Ch 08 — S3: Store Anything, Forever**
Simple Storage Service. Buckets, objects, permissions, storage classes. Versioning. Lifecycle rules. Meera uploads Pixel & Spoon's menu item photos and cook profile images to S3.

**Ch 09 — S3 in Practice: Host a Real Website**
Hands-on project chapter. Deploy a static site to S3 with a custom domain via Route 53. Ties S3 + Route 53 together. Readers finish with something live on the internet they built themselves.

---

## 🔵 Planned — Databases

**Ch 10 — RDS: Databases Without the Headache**
Relational Database Service. Why managed databases exist. Set up an RDS instance (PostgreSQL), connect it to Pixel & Spoon's ordering system. Migrate orders from in-memory storage to a real database. Automated backups, scaling, multi-AZ for reliability.

**Ch 11 — DynamoDB: When SQL Isn't Enough**
NoSQL on AWS. What DynamoDB is, when to use it instead of RDS. Power Pixel & Spoon's menu search with DynamoDB for fast key-value lookups. Sets up the SQL vs NoSQL comparison clearly.

---

## 🔵 Planned — Auth

**Ch 12 — Cognito: Real Auth for Pixel & Spoon**
User registration and login done the AWS way. Amazon Cognito user pools, JWT tokens, protected routes. Replace Pixel & Spoon's hardcoded admin password with proper role-based auth. Cooks get accounts and manage their own menu items. Customers see their order history. This is where the placeholder auth comments from Ch 05 finally get filled in.

---

## 🔵 Planned — Serverless & Messaging

**Ch 13 — Lambda: Code That Runs Itself**
Serverless computing. Write a function, trigger it with an event, pay only when it runs. Real example — Pixel & Spoon's pincode delivery checker as a Lambda function. No server needed for a simple lookup.

**Ch 14 — SNS & SQS: Making Services Talk to Each Other**
Messaging services. SNS sends Pixel & Spoon's order confirmation SMS/email. SQS processes order status updates asynchronously. Why microservices need decoupling — explained through the ordering flow.

---

## 🔵 Planned — Monitoring & Security

**Ch 15 — CloudWatch: Know What's Happening Inside AWS**
Monitoring and logging. Metrics, alarms, log groups. Pixel & Spoon's founder gets an analytics dashboard. Set up an alarm for high EC2 CPU. You can't run production workloads blind — this chapter fixes that.

**Ch 16 — Secrets Manager & Parameter Store: Store Secrets Safely**
How to handle passwords, API keys, and config values in AWS. Replace Pixel & Spoon's hardcoded database credentials and config values with Secrets Manager. Never hardcode again.

---

## 🔵 Planned — Networking

**Ch 17 — Route 53: Give Your App a Real Address**
DNS on AWS. Domain registration, hosted zones, routing policies. Give Pixel & Spoon a real domain instead of a raw IP address.

**Ch 18 — CloudFront: Deliver Fast, Everywhere**
AWS's CDN. Pixel & Spoon's menu images delivered via CloudFront edge locations — fast for users everywhere. HTTPS via ACM certificate. The browser stops showing "Not Secure."

**Ch 19 — VPC: Your Private Corner of AWS**
Virtual Private Cloud — the networking foundation of everything on AWS. Subnets (public vs private), route tables, internet gateways, security groups vs NACLs. Rohit puts Pixel & Spoon's database in a private subnet — unreachable from the internet.

---

## 🔵 Planned — Infrastructure as Code

**Ch 20 — CloudFormation: Build Infrastructure With Code**
Stop clicking, start declaring. Write a CloudFormation template that creates real AWS resources. Stacks, updates, rollbacks. Why IaC matters for consistency and repeatability.

**Ch 21 — Terraform: IaC Beyond AWS**
Brief intro to Terraform — what it is, how it differs from CloudFormation, why teams use it. Write a simple Terraform config that provisions an EC2 instance. Sets readers up for the broader DevOps world.

---

## 🔵 Planned — Containers

**Ch 22 — ECS: Running Containers on AWS**
Elastic Container Service. What containers are, ECS concepts — clusters, tasks, services. Fargate vs EC2 launch types. Deploy Pixel & Spoon as a containerised app.

**Ch 23 — EKS: Kubernetes on AWS**
Elastic Kubernetes Service. What Kubernetes is and when you need it over ECS. Nodes, pods, deployments. Intentionally kept accessible — this is an intro, not a Kubernetes course.

---

## 🔵 Planned — Cost & Billing

**Ch 24 — AWS Pricing & Billing: Never Get a Surprise Bill**
How AWS actually charges. On-demand vs reserved vs spot instances. The Free Tier in detail. Cost Explorer walkthrough. Set up billing alerts and budgets. Every beginner's biggest fear — addressed head on.

---

## 🔵 Planned — Capstone & Big Picture

**Ch 25 — Build Something Real: Full Stack Pixel & Spoon on AWS**
Capstone project. Everything from the series comes together — EC2, EBS, S3, RDS, Lambda, SNS, CloudWatch, Secrets Manager, Route 53, CloudFront, VPC, Cognito. Readers finish with a production-grade app and a portfolio project.

**Ch 26 — AWS vs Azure vs GCP: An Honest Comparison**
Not a sales pitch. A clear, fair look at where each cloud provider is strong, what the ecosystem looks like, and how to think about choosing. High search traffic chapter — pulls in readers from outside the series.

**Ch 27 — What's Next: AWS Certifications Roadmap**
Which cert to go for first (Cloud Practitioner vs Solutions Architect). What each covers. How this series maps to exam topics. Study tips and recommended resources. The closing chapter — sends readers off with a clear next step.

---

## 🟡 Bonus Chapters (future)

**Bonus A — DNS Deep Dive with Practicals**
How DNS actually works under the hood. Goes deeper than Route 53. Practical examples — trace a domain lookup step by step.

**Bonus B — SSL/TLS & HTTPS Explained**
How encryption works, what certificates are, how to configure HTTPS for a web app on AWS using ACM (AWS Certificate Manager).

**Bonus C — AWS Amplify: Full Stack the Fast Way**
Deploy a full-stack web app with Amplify. Frontend + backend + CI/CD pipeline. Good for readers coming from a frontend background.

**Bonus D — AWS Well-Architected Framework**
The 6 pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimisation, Sustainability. The mental model behind how AWS expects you to build.

**Bonus E — Amazon Cognito Deep Dive**
Goes beyond the Ch 12 intro. Social login (Google, Facebook), MFA flows, custom triggers with Lambda, federating with corporate identity providers.

---

## 📋 Quick Index

| Ch | Title | Status |
|----|-------|--------|
| 00 | Before You Learn AWS | ✅ Published |
| 01 | The World Before AWS | ✅ Published |
| 02 | Virtualization & Cloud Models | 🔵 Planned |
| 03 | Welcome to AWS | 🔵 Planned |
| 04 | IAM | 🔵 Planned |
| 04.1 | Creating IAM Users | 🔵 Planned |
| 04.2 | Creating IAM Groups | 🔵 Planned |
| 04.3 | Writing IAM Policies | 🔵 Planned |
| 04.4 | Creating IAM Roles | 🔵 Planned |
| 05 | EC2: Your First Server | 🔵 Planned |
| 05.1 | All Four Ways to Connect to EC2 | 🔵 Planned |
| 06 | EBS, AMI & Auto Scaling | 🔵 Planned |
| 07 | AWS CLI | 🔵 Planned |
| 08 | S3 | 🔵 Planned |
| 09 | S3 Project — Static Website | 🔵 Planned |
| 10 | RDS | 🔵 Planned |
| 11 | DynamoDB | 🔵 Planned |
| 12 | Cognito: Real Auth for Pixel & Spoon | 🔵 Planned |
| 13 | Lambda | 🔵 Planned |
| 14 | SNS & SQS | 🔵 Planned |
| 15 | CloudWatch | 🔵 Planned |
| 16 | Secrets Manager | 🔵 Planned |
| 17 | Route 53 | 🔵 Planned |
| 18 | CloudFront | 🔵 Planned |
| 19 | VPC | 🔵 Planned |
| 20 | CloudFormation | 🔵 Planned |
| 21 | Terraform | 🔵 Planned |
| 22 | ECS | 🔵 Planned |
| 23 | EKS | 🔵 Planned |
| 24 | Pricing & Billing | 🔵 Planned |
| 25 | Capstone Project | 🔵 Planned |
| 26 | AWS vs Azure vs GCP | 🔵 Planned |
| 27 | Certifications Roadmap | 🔵 Planned |
| B-A | DNS Deep Dive | 🟡 Bonus |
| B-B | SSL/TLS & HTTPS | 🟡 Bonus |
| B-C | AWS Amplify | 🟡 Bonus |
| B-D | Well-Architected Framework | 🟡 Bonus |
| B-E | Cognito Deep Dive | 🟡 Bonus |