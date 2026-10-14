# EBS, AMI & Auto Scaling: The Complete Compute Picture 🏗️

> *Chapter 6 of the AWS Learning Journey. Pixel & Spoon is live. But live isn't the same as resilient. Rohit is about to find that out the hard way — and fix it properly.*

---

## Saturday Morning. 7:43am.

Rohit is making chai when his phone buzzes.

It's the founder.

> *"Hey — the server restarted last night during the maintenance window. All our test orders are gone. Is that normal?"*

Rohit stares at his phone.

He knows exactly what happened. The EC2 instance restarted. And when it did — the Node.js process came back up fresh. Clean slate. In-memory storage, wiped completely.

Every order placed during yesterday's testing session. Gone.

He types back:

> *"Yes. It's normal for now. I'll fix it today."*

He puts his phone down and opens his laptop.

Because "normal for now" is not good enough for a food delivery app that's about to go live.

---

## 🔍 Three Problems. One Chapter.

What Rohit realises over his chai is that Pixel & Spoon has not one problem — but three. And they're all connected.

```
Problem 1 → Data disappears when the server restarts
Problem 2 → If the server crashes, rebuilding takes hours
Problem 3 → One server can't handle a real traffic spike
```

Each problem has a solution. And each solution builds on the last.

This is the chapter where Pixel & Spoon stops being a demo and starts being infrastructure.

---

## 💾 Problem 1: Data Dies With the Server

Here's what's happening under the hood.

When Pixel & Spoon's Node.js app runs, orders are stored in a JavaScript array — in the server's RAM. RAM is fast. RAM is temporary. The moment the process stops — whether from a crash, a restart, or a deployment — that array is gone.

This is fine for learning. It's a disaster for production.

Rohit needs storage that survives independently of the server. Storage that exists even when the EC2 instance is stopped, restarted, or replaced.

That's **EBS** — Elastic Block Store.

---

### 🗄️ What Is EBS?

Think of EC2 as a laptop. When you buy a laptop, it comes with a hard drive — that's where your files live. You can also plug in an external hard drive — more storage, separate from the laptop itself.

EBS is that external hard drive. But for EC2.

```
Without EBS:

🖥️ EC2 Instance
   └── RAM (orders stored here)
        └── Server restarts → RAM cleared → orders gone 💀

With EBS:

🖥️ EC2 Instance
   └── RAM (app runs here)
   └── 📦 EBS Volume → /data/orders.json
        └── Server restarts → EBS untouched → orders safe ✅
```

An EBS volume is a network-attached storage device. It exists independently of any EC2 instance. You can attach it, detach it, and reattach it to a different instance. You can take snapshots of it for backup. You can resize it without stopping the instance.

![A laptop (EC2) on a desk with a USB external hard drive plugged into it (EBS volume). The laptop screen shows an app running. The hard drive has a small label: 'orders.json'. A second scene below shows the laptop lid closed (server stopped) but the hard drive still glowing, still intact.](image.png)


Rohit attaches an EBS volume to Pixel & Spoon's server. He updates the app to write orders to a JSON file on it instead of keeping them in memory.

Now when the server restarts — the orders are still there.

The founder's Saturday morning message will never happen again.

> 🛠️ **Hands-on:** Ready to attach an EBS volume and update Pixel & Spoon's app to use it?
> 👉 **[Ch 6.1 - Attaching and Using an EBS Volume  → (Read it here)](LINK)**

---

## 📸 Problem 2: Rebuilding From Scratch Takes Hours

EBS solves the data problem. But Rohit is thinking ahead.

What if the EC2 instance itself fails completely?

Not a restart. A complete failure. The instance is gone. He needs to launch a new one.

He'd have to:

- Launch a fresh EC2 instance
- Install Node.js
- Clone the repository
- Mount the EBS volume
- Configure the security groups
- Test everything

That's not minutes. That's hours. Hours during which Pixel & Spoon is completely down.

For a food delivery app — especially during lunch hour — that's unacceptable.

Rohit needs a way to stamp out a perfect, pre-configured server in minutes. Not from scratch. From a template.

That's **AMI** — Amazon Machine Image.

---

### 📷 What Is an AMI?

Remember Chapter 5 — when we launched the EC2 instance and chose Amazon Linux 2023 as the operating system? That was an AMI. A template that the instance was built from.

You can create your own.

Once Rohit has Pixel & Spoon's server perfectly configured — Node.js installed, app cloned, EBS mounted, security rules set — he takes a snapshot of the entire instance. That snapshot becomes a custom AMI — a **golden image**.

```
Current Server (perfectly configured):
🖥️ EC2: pixel-spoon-backend
   ├── Amazon Linux 2023
   ├── Node.js installed
   ├── pixel-and-spoon repo cloned (ch06-ebs)
   ├── EBS volume mounted
   └── Security groups configured

          ↓  Create AMI

📸 AMI: pixel-spoon-golden-v1
   └── Exact copy of the root volume, frozen in time

          ↓  Launch from AMI anytime

🖥️ New EC2 instance — pre-installed, pre-configured, ready in minutes
```

---

### 🤔 But Wait — What About the EBS Data Volume?

This is where it gets important to understand clearly.

When you create an AMI, AWS shows you a **Block Device Mapping** section. You'll see two volumes listed:

```
/dev/xvda  →  Root volume (OS, Node.js, app code)  ← always included
/dev/xvdf  →  pixel-spoon-data (orders.json)        ← your choice
```

Should you include `pixel-spoon-data` in the AMI?

**No. Here's why:**

```
❌ Including the data volume in the AMI means:

   Every new instance launched from this AMI gets a frozen
   snapshot of orders from the moment the AMI was created.
   
   That's stale data. Potentially hours or days old.
   Not the live orders.json from today.

✅ The correct approach:

   AMI captures the root volume only (OS + app code)
   pixel-spoon-data EBS volume is managed separately
   Reattach it to any new instance as needed
   Always has the latest live data
```

The AMI is a **template for the server itself**. The data volume is **live state that exists independently**. Keep them separate.

> 🎨 **Illustration prompt:**
> [Master Prompt] + *"A camera taking a photo of a server. The camera frame clearly includes the server (with Node.js and code icons) but excludes a separate hard drive sitting beside it (outside the frame, slightly blurred, labeled 'live data'). The developed polaroid shows only the server. Soft amber on camera flash. Vibe: intentional framing, clarity about what's captured."*
> 🔖 Watermark: srsoumyax11 | Ratio: 16:9

---

### ⚠️ The fstab Situation — Be Honest About This

Remember in Ch 6.1, we added an entry to `/etc/fstab` to auto-mount the EBS volume by UUID:

```
UUID=a1b2c3d4-e5f6-...   /data   ext4   defaults,nofail   0   2
```

That fstab entry **is captured in the AMI** — it's on the root volume.

Here's what happens when a new instance launches from the AMI:

```
Scenario A — Same pixel-spoon-data volume reattached:
   fstab UUID matches → auto mounts ✅ → /data available → app works ✅

Scenario B — No EBS volume attached:
   fstab UUID not found → nofail → server boots fine ✅
   but /data doesn't exist → app crashes trying to write orders ❌

Scenario C — New EBS volume attached:
   Different UUID → fstab doesn't recognise it → /data missing ❌
   Need to manually mount or update fstab
```

**The `nofail` option saves the server boot — but not the app.**

This is not a bug. This is the honest limitation of file-based storage in a scaled environment. The proper fix is a database that every instance connects to by hostname — no mounting, no UUIDs, no fstab. That's Chapter 10 (RDS).

For now — the AMI + original EBS volume reattached = recovery in minutes.

> 🛠️ **Hands-on:** Create Pixel & Spoon's golden image with the correct block device mapping:
> 👉 **[Ch 6.2 — Creating and Using an AMI → (Read it here)](LINK)**

---

## 📈 Problem 3: One Server Can't Handle Real Traffic

It's Tuesday afternoon. Rohit is about to close his laptop.

His phone buzzes. It's Aarav.

> *"Bro — check Twitter. Someone just mentioned Pixel & Spoon."*

Rohit opens Twitter.

A food blogger with 200,000 followers just posted:

> *"Just discovered @PixelandSpoon and honestly? The butter chicken bowl might be life. Everyone go order now 🍛"*

Rohit watches the EC2 CPU monitor.

```
2:14pm  →  CPU: 12%   (normal)
2:15pm  →  CPU: 34%   (spike starting)
2:16pm  →  CPU: 67%   (getting serious)
2:17pm  →  CPU: 89%   (danger zone)
2:18pm  →  CPU: 98%   (app slowing down)
2:19pm  →  Users start seeing slow load times
2:20pm  →  First timeout errors appear
```

One t3.micro. Thousands of users. The math doesn't work.

Rohit needs more servers. Right now. Not in 20 minutes — **right now**.

And when traffic dies down at 4pm — he needs those extra servers gone so Pixel & Spoon isn't paying for capacity it doesn't need.

That's **ELB + Auto Scaling**.

---

### ⚖️ What Is a Load Balancer?

A **load balancer** sits in front of your servers. Every incoming request hits it first. It decides which server handles it — distributing the load evenly.

```
Without ELB:

1000 users  →  🖥️ pixel-spoon-backend  →  💀 overwhelmed

With ELB:

                   ┌→  🖥️ Server 1  (healthy ✅)
1000 users  →  ELB ─→  🖥️ Server 2  (healthy ✅)
                   └→  🖥️ Server 3  (healthy ✅)
```

If one server goes down — ELB stops sending it traffic. The others pick up the slack. No human intervention.

Remember the `/health` endpoint built in Chapter 5?

```json
GET /health → { "status": "ok", "service": "pixel-spoon-backend" }
```

**ELB pings that endpoint every 30 seconds.** If a server stops returning `"status": "ok"` — ELB marks it unhealthy and removes it from rotation automatically.

That endpoint wasn't just for show. It was always meant for this moment.

---

### 📊 What Is Auto Scaling?

A load balancer distributes traffic. But it can't create new servers.

That's what an **Auto Scaling Group** (ASG) does.

You define the rules:

```
Minimum servers:   1   (always at least one running)
Maximum servers:   6   (never more than six)
Scale out when:    CPU > 70% for 2 minutes → add 1 server
Scale in when:     CPU < 30% for 5 minutes → remove 1 server
```

ASG needs to know what kind of server to launch. That's where the **Launch Template** comes in — a saved configuration that tells ASG exactly what to create: which AMI, which instance type, which key pair, which security group.

```
Launch Template
   ├── AMI: pixel-spoon-golden-v1    (from Ch 6.2)
   ├── Instance type: t3.micro
   ├── Key pair: pixelspoon-key
   └── Security group: pixel-spoon-backend
```

When the food blogger posts and CPU hits 89% — ASG reads the Launch Template, launches a new EC2 instance from the golden AMI, and registers it with the load balancer. Automatically. In minutes.

```
2:14pm  →  1 server    CPU: 12%  (normal)
2:16pm  →  1 server    CPU: 67%  ← ASG triggers, launches new instance
2:18pm  →  2 servers   CPU: 41%  ← load distributed
2:20pm  →  3 servers   CPU: 28%  ← stable
4:00pm  →  traffic drops  CPU: 8%  ← ASG triggers scale-in
4:05pm  →  2 servers   CPU: 11%
4:15pm  →  1 server    CPU: 9%   ← back to baseline
```

Scale up when needed. Scale down when not. Pay for exactly what you use.

This is the elastic in **Elastic** Compute Cloud — finally used the way it was designed.

> 🎨 **Illustration prompt:**
> [Master Prompt] + *"A horizontal load balancer bar at top, arrows flowing down to three servers below it evenly. Right side: a simple line graph showing CPU % rising with servers being added (arrows up), then dropping as servers are removed (arrows down). Soft orange on the load balancer bar. Vibe: balance, automatic response, elasticity."*
> 🔖 Watermark: srsoumyax11 | Ratio: 16:9

---

### ⚠️ The Shared Storage Problem

Sharp readers will notice something here.

If ASG launches three EC2 instances — each one needs the same orders. But EBS volumes attach to **one instance at a time**.

```
❌ What this means in practice:

User A → ELB → Instance 1 → EBS (has all orders) ✅
User B → ELB → Instance 2 → no EBS attached ❌
User C → ELB → Instance 3 → no EBS attached ❌

Instance 2 and 3 can't write or read orders at all.
```

This is a real architectural limitation. File-based storage on EBS doesn't scale horizontally. It was never designed to.

The fix isn't clever mounting tricks. The fix is a **shared database** — one RDS instance that all EC2 instances connect to by hostname. No mounting. No UUIDs. No fstab. Every instance queries the same data, always in sync.

```
✅ What Chapter 10 (RDS) fixes:

User A → ELB → Instance 1 ─┐
User B → ELB → Instance 2 ─┼→ RDS Database → same orders ✅
User C → ELB → Instance 3 ─┘
```

For now, Pixel & Spoon runs on a **single instance**. The load balancer, ASG, and Launch Template are fully configured and ready. We just need a real database before horizontal scaling works end to end.

> 🛠️ **Hands-on:** Set up the Launch Template, ELB, and Auto Scaling Group:
> 👉 **[Ch 6.3 — Launch Template, ELB & Auto Scaling → (Read it here)](LINK)**

---

## 🧩 How It All Connects

Step back and look at what Rohit built today.

```
📦 EBS Volume (pixel-spoon-data)
   └── Orders survive server restarts
   └── Managed separately from the AMI
   └── Reattached to any replacement instance

📸 AMI (pixel-spoon-golden-v1)
   └── Root volume only — OS, Node.js, app code
   └── fstab captured — data volume auto-mounts if reattached
   └── Launch Template uses this to stamp out new servers

🚀 Launch Template
   └── Tells ASG exactly what to launch
   └── AMI + instance type + key pair + security group

⚖️ ELB + Auto Scaling Group
   └── ELB distributes traffic, uses /health for checks
   └── ASG scales out on CPU spike using Launch Template
   └── ASG scales in when traffic drops
   └── Ready for RDS — shared storage solves sync problem
```

EBS gives data persistence.
AMI makes servers reproducible.
Launch Template makes ASG possible.
ELB + ASG makes the whole thing elastic.

Without any one piece — the others don't work properly.

---

## 🌅 Rohit Finally Sleeps

It's 11pm. Rohit closes his laptop.

The load balancer is routing. The auto scaling group is watching CPU. The EBS volume holds every order. The golden AMI is ready to stamp out new servers at a moment's notice. The Launch Template ensures every new server is identical to the last.

He sets his phone to Do Not Disturb.

For the first time since Pixel & Spoon launched — he's not worried about what happens while he sleeps.

That's what resilient infrastructure feels like.

---

## 🗺️ Where We Go From Here

**Ch 00** — ✅ The origin story

**Ch 01** — ✅ The world before AWS

**Ch 02** — ✅ Virtualization & Cloud Models

**Ch 03** — ✅ Welcome to AWS

**Ch 04** — ✅ IAM: The Gatekeeper of AWS

**Ch 04.1** — ✅ Creating IAM Users

**Ch 04.2** — ✅ Creating IAM Groups

**Ch 04.3** — ✅ Writing and Attaching IAM Policies

**Ch 04.4** — ✅ Creating IAM Roles

**Ch 05** — ✅ EC2: Your First Server

**Ch 05.1** — ✅ All Four Ways to Connect to EC2

**Ch 06** — ✅ EBS, AMI & Auto Scaling *(you are here)*

**Ch 06.1** — Attaching and Using an EBS Volume

**Ch 06.2** — Creating and Using an AMI (Golden Image)

**Ch 06.3** — Launch Template, ELB & Auto Scaling

**Ch 07** — AWS CLI: Stop Clicking, Start Typing

**Ch 08** — S3: Store Anything, Forever

**Ch 09** — S3 in Practice: Host a Real Website

**Ch 10** — RDS: Databases Without the Headache

**Ch 11** — DynamoDB: When SQL Isn't Enough

**Ch 12** — Cognito: Real Auth for Pixel & Spoon

**Ch 13** — Lambda: Code That Runs Itself

**Ch 14** — SNS & SQS: Making Services Talk to Each Other

**Ch 15** — CloudWatch: Know What's Happening Inside AWS

**Ch 16** — Secrets Manager: Store Secrets Safely

**Ch 17** — Route 53: Give Your App a Real Address

**Ch 18** — CloudFront: Deliver Fast, Everywhere

**Ch 19** — VPC: Your Private Corner of AWS

**Ch 20** — CloudFormation: Build Infrastructure With Code

**Ch 21** — Terraform: IaC Beyond AWS

**Ch 22** — ECS: Running Containers on AWS

**Ch 23** — EKS: Kubernetes on AWS

**Ch 24** — Billing & Pricing: Never Get a Surprise Bill

**Ch 25** — Capstone: Full Stack Pixel & Spoon on AWS

**Ch 26** — AWS vs Azure vs GCP: An Honest Comparison

**Ch 27** — What's Next: AWS Certifications Roadmap

---

### Before You Click Away.

Pixel & Spoon is resilient now. Data persists. Servers are reproducible. Traffic is handled automatically.

But Rohit has been doing everything through the AWS console — clicking, scrolling, filling in forms.

There's a faster way.

In Chapter 7, Aarav shows Rohit something that changes how they both work — the AWS CLI. Everything done in the last three chapters, now done in a single line from the terminal. The first step toward real automation.

👉 **[Chapter 7: AWS CLI — Stop Clicking, Start Typing → (Read it here)](LINK)**

---

*Resources I'm learning from:*
- *[roadmap.sh/aws](https://roadmap.sh/aws) — my learning roadmap*
- *[AWS Official Overview Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html) — straight from the source*

---

*#aws #cloud #ec2 #devops*
ENDOFFILE
echo "Done"