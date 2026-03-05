# Nmap Beginner Guide: The Most Important Commands for 2026

Nmap is the first tool every cybersecurity learner needs to master. It's
free, powerful, and used in virtually every penetration test. I first used
it on TryHackMe and it completely changed how I understood network
reconnaissance.

This guide covers everything a beginner needs to get productive with Nmap
fast.

## What is Nmap?

Nmap (Network Mapper) is a free, open-source tool for network discovery and
security auditing. It tells you:
- What devices are on a network
- What ports are open on those devices
- What services are running on those ports
- What operating system a device is running

It's pre-installed on Kali Linux and available free on Windows, Mac, and Linux.

## Installing Nmap

### Kali Linux (already installed)
```bash
nmap --version
```

### Ubuntu/Debian
```bash
sudo apt install nmap
```

### Windows
Download the installer from [nmap.org](https://nmap.org/download.html) — free.

## The Most Important Nmap Commands

### 1. Basic Port Scan
The simplest scan — checks the 1000 most common ports:
```bash
nmap 10.10.10.1
```
Use this first on any TryHackMe or HackTheBox machine to get a quick overview.

### 2. Scan All Ports
The basic scan only checks 1000 ports. This checks all 65,535:
```bash
nmap -p- 10.10.10.1
```
Slower but you won't miss anything. Always run this if the basic scan
looks empty.

### 3. Service and Version Detection
Find out exactly what software is running on each open port:
```bash
nmap -sV 10.10.10.1
```
This is how you find outdated software versions that might be vulnerable.

### 4. OS Detection
My personal favorite — tells you what operating system the target is running:
```bash
nmap -O 10.10.10.1
```
Knowing the OS immediately narrows down what exploits might work. I use
this on almost every TryHackMe machine I attack.

Combined with service detection:
```bash
nmap -O -sV 10.10.10.1
```

### 5. Default Script Scan
Runs Nmap's built-in scripts to find common vulnerabilities automatically:
```bash
nmap -sC 10.10.10.1
```

### 6. The All-in-One Scan (Most Used)
This is the command I use most — combines OS detection, version detection,
scripts, and traceroute:
```bash
nmap -A 10.10.10.1
```
It's slower but gives you everything in one shot. Perfect for CTFs and
TryHackMe rooms.

### 7. Aggressive + All Ports (Full Recon)
When you want a complete picture of a target:
```bash
nmap -A -p- 10.10.10.1
```
Warning: this is noisy and slow. Use it in lab environments, not on
real engagements where stealth matters.

### 8. Fast Scan
When you just need quick results:
```bash
nmap -F 10.10.10.1
```
Scans only the 100 most common ports instead of 1000.

### 9. Scan Multiple Targets
Scan a whole network range:
```bash
nmap 10.10.10.0/24
```
Or a list of specific IPs:
```bash
nmap 10.10.10.1 10.10.10.2 10.10.10.3
```

### 10. Save Output to File
Always save your results — you'll want to refer back to them:
```bash
nmap -A 10.10.10.1 -oN results.txt
```

## Nmap Cheat Sheet

| Command | What it Does |
|---------|-------------|
| `nmap <ip>` | Basic scan (1000 ports) |
| `nmap -p- <ip>` | Scan all 65,535 ports |
| `nmap -sV <ip>` | Service/version detection |
| `nmap -O <ip>` | OS detection |
| `nmap -sC <ip>` | Default scripts |
| `nmap -A <ip>` | All of the above combined |
| `nmap -F <ip>` | Fast scan (100 ports) |
| `nmap -oN file.txt <ip>` | Save output to file |

## My Recommended Workflow for TryHackMe/CTFs

When I start a new TryHackMe machine I always run scans in this order:

**Step 1 — Quick overview:**
```bash
nmap -F 10.10.10.1
```

**Step 2 — Full recon:**
```bash
nmap -A -p- 10.10.10.1 -oN full-scan.txt
```

**Step 3 — Review results and plan next steps**

This two-step approach saves time — the fast scan gives you something
to work with immediately while the full scan runs in the background.

## Practice Nmap for Free

The best way to learn Nmap is hands-on practice:

- **TryHackMe** — has a dedicated Nmap room in the Jr Penetration Tester
  path. [Start free →](https://tryhackme.com)
- **HackTheBox** — Starting Point machines are great for practicing recon
- **Your own lab** — Set up a free local lab with VirtualBox and
  Metasploitable, or use a
  [DigitalOcean VPS](https://m.do.co/c/a2644c2e88b4) for $4/mo

## Important: Only Scan What You Own or Have Permission to Scan

Running Nmap against systems you don't own or have explicit permission to
test is illegal in most countries. Always practice on:
- TryHackMe or HackTheBox machines
- Your own local VMs
- Systems you have written permission to test

## Final Thoughts

Nmap is one of those tools that takes 10 minutes to learn the basics and
years to master fully. Start with `-A` and `-p-` for your TryHackMe rooms
and you'll have everything you need for the first few months.

As you advance, look into Nmap Scripting Engine (NSE) — there are hundreds
of scripts for finding specific vulnerabilities automatically.

---
*All commands tested in personal lab environments and TryHackMe rooms.
Some links are affiliate links which help support this site at no cost
to you.*
*All commands tested in personal lab environments and TryHackMe rooms.
Some links are affiliate links which help support this site at no cost
to you.*
