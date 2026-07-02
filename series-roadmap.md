# AWS Learning Journey — Series Roadmap
> Last updated: June 2026
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
https://dev.to/srsoumyax11/iam-the-gatekeeper-of-aws-111b



https://dev.to/srsoumyax11/pixel-spoon-hands-on-creating-your-first-iam-user-2lg3


---

## 🔵 Planned — Compute

**Ch 05 — EC2: Your First Server in the Cloud**
The flagship AWS service. Launch a virtual server, understand instance types, configure security groups and key pairs. Connect to it. Understand what you're actually paying for. First hands-on chapter — readers should finish with a running EC2 instance.

**Ch 06 — EBS: Storage That Sticks to Your Server**
EC2 needs a hard drive — that's EBS. What it is, how to attach and detach volumes, snapshots for backup, different volume types and when to use them.

**Ch 07 — AMI: Clone Your Server Like a Pro**
Amazon Machine Images. What they are, how to create one from a configured EC2 instance, how to use them to spin up identical servers instantly. The concept of a "golden image."

**Ch 08 — ELB & ASG: Handle Traffic Without Breaking a Sweat**
Two services, one big idea — high availability. Elastic Load Balancer distributes traffic across multiple servers. Auto Scaling Group adds or removes servers automatically based on demand. Together they solve the "app goes viral" problem from Ch 01.

---

## 🔵 Planned — CLI & Developer Tools

**Ch 09 — AWS CLI: Stop Clicking, Start Typing**
The leap from console to command line. Install and configure the AWS CLI. Run real commands — launch an instance, list S3 buckets, check IAM users. Why this matters for automation and real-world work. Readers finish feeling like they levelled up.

---

## 🔵 Planned — Storage

**Ch 10 — S3: Store Anything, Forever**
Simple Storage Service. Buckets, objects, permissions, storage classes. Versioning. Lifecycle rules. The scale of S3 and why it's one of AWS's most used services.

**Ch 11 — S3 in Practice: Host a Real Website**
Hands-on project chapter. Take a simple HTML/CSS site and deploy it to S3 with a custom domain via Route 53. Ties S3 + Route 53 together. Readers finish with something live on the internet they built themselves.

---

## 🔵 Planned — Databases

**Ch 12 — RDS: Databases Without the Headache**
Relational Database Service. Why managed databases exist. Set up an RDS instance (MySQL or PostgreSQL), connect to it, understand automated backups, scaling, and multi-AZ for reliability.

**Ch 13 — DynamoDB: When SQL Isn't Enough**
NoSQL on AWS. What DynamoDB is, when to use it instead of RDS, tables and keys, basic read/write operations. Keeps it conceptual — enough to know when to reach for it.

---

## 🔵 Planned — Serverless & Messaging

**Ch 14 — Lambda: Code That Runs Itself**
Serverless computing. Write a function, trigger it with an event, pay only when it runs. No servers to manage. Simple real example — a function triggered by an S3 upload or an API call.

**Ch 15 — SNS & SQS: Making Services Talk to Each Other**
Messaging services. SNS (notifications, fan-out) vs SQS (queues, decoupling). Why microservices need these. Simple analogy-driven explanation with a practical example tying back to Lambda.

---

## 🔵 Planned — Monitoring & Security

**Ch 16 — CloudWatch: Know What's Happening Inside AWS**
Monitoring and logging. Metrics, alarms, log groups. Set up an alarm that notifies you when EC2 CPU is too high. You can't run production workloads blind — this chapter fixes that.

**Ch 17 — Secrets Manager & Parameter Store: Store Secrets Safely**
How to handle passwords, API keys, and config values in AWS. Never hardcode credentials. Practical setup — store a database password in Secrets Manager and retrieve it in code.

---

## 🔵 Planned — Networking

**Ch 18 — Route 53: Give Your App a Real Address**
DNS on AWS. Domain registration, hosted zones, routing policies (simple, weighted, geolocation, failover). Connects naturally to the S3 website project from Ch 11.

**Ch 19 — CloudFront: Deliver Fast, Everywhere**
AWS's CDN. How it caches content at edge locations globally so users get fast responses regardless of where they are. Set up a CloudFront distribution in front of an S3 bucket.

**Ch 20 — VPC: Your Private Corner of AWS**
Virtual Private Cloud — the networking foundation of everything on AWS. Subnets (public vs private), route tables, internet gateways, security groups vs NACLs. This is the chapter that makes AWS networking stop feeling like magic.

---

## 🔵 Planned — Infrastructure as Code

**Ch 21 — CloudFormation: Build Infrastructure With Code**
Stop clicking, start declaring. Write a CloudFormation template that creates real AWS resources. Understand stacks, updates, rollbacks. Why IaC matters for consistency and repeatability.

**Ch 22 — Terraform: IaC Beyond AWS**
Brief intro to Terraform — what it is, how it differs from CloudFormation, why teams use it. Write a simple Terraform config that provisions an EC2 instance. Sets readers up for the broader DevOps world.

---

## 🔵 Planned — Containers

**Ch 23 — ECS: Running Containers on AWS**
Elastic Container Service. What containers are (brief, no Docker deep dive), ECS concepts — clusters, tasks, services. Fargate vs EC2 launch types. Deploy a simple containerised app.

**Ch 24 — EKS: Kubernetes on AWS**
Elastic Kubernetes Service. What Kubernetes is and when you need it over ECS. Nodes, pods, deployments. Intentionally kept accessible — this is an intro, not a Kubernetes course.

---

## 🔵 Planned — Cost & Billing

**Ch 25 — AWS Pricing & Billing: Never Get a Surprise Bill**
How AWS actually charges. On-demand vs reserved vs spot instances. The Free Tier in detail. Cost Explorer walkthrough. Set up billing alerts and budgets. Every beginner's biggest fear — addressed head on.

---

## 🔵 Planned — Capstone & Big Picture

**Ch 26 — Build Something Real: Full Stack App on AWS**
Capstone project. Build and deploy a simple full-stack application using EC2 + S3 + RDS + Route 53 + CloudFront. Everything from the series comes together. Readers finish with a portfolio project.

**Ch 27 — AWS vs Azure vs GCP: An Honest Comparison**
Not a sales pitch. A clear, fair look at where each cloud provider is strong, what the ecosystem looks like, and how to think about choosing. High search traffic chapter — pulls in readers from outside the series.

**Ch 28 — What's Next: AWS Certifications Roadmap**
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

---

## 📋 Quick Index

| Ch | Title | Status |
|----|-------|--------|
| 00 | Before You Learn AWS | ✅ Published |
| 01 | The World Before AWS | ✅ Published |
| 02 | Virtualization & Cloud Models | ✅ Published |
| 03 | Welcome to AWS | 🔵 Planned |
| 04 | IAM | 🔵 Planned |
| 05 | EC2 | 🔵 Planned |
| 06 | EBS | 🔵 Planned |
| 07 | AMI | 🔵 Planned |
| 08 | ELB & ASG | 🔵 Planned |
| 09 | AWS CLI | 🔵 Planned |
| 10 | S3 | 🔵 Planned |
| 11 | S3 Project — Static Website | 🔵 Planned |
| 12 | RDS | 🔵 Planned |
| 13 | DynamoDB | 🔵 Planned |
| 14 | Lambda | 🔵 Planned |
| 15 | SNS & SQS | 🔵 Planned |
| 16 | CloudWatch | 🔵 Planned |
| 17 | Secrets Manager | 🔵 Planned |
| 18 | Route 53 | 🔵 Planned |
| 19 | CloudFront | 🔵 Planned |
| 20 | VPC | 🔵 Planned |
| 21 | CloudFormation | 🔵 Planned |
| 22 | Terraform | 🔵 Planned |
| 23 | ECS | 🔵 Planned |
| 24 | EKS | 🔵 Planned |
| 25 | Pricing & Billing | 🔵 Planned |
| 26 | Capstone Project | 🔵 Planned |
| 27 | AWS vs Azure vs GCP | 🔵 Planned |
| 28 | Certifications Roadmap | 🔵 Planned |
| B-A | DNS Deep Dive | 🟡 Bonus |
| B-B | SSL/TLS & HTTPS | 🟡 Bonus |
| B-C | AWS Amplify | 🟡 Bonus |
| B-D | Well-Architected Framework | 🟡 Bonus |
