# 2.2) Azure Compute & Networking Services

## 2.2.1) Intro

### Objectives:
 
- Compare:
	- Compute Types - inc. Container Instances, VMs, Functions
- Describe: 
	- VM options - Inc. VMs, VM Scale Sets; Availability Sets, Azure Virtual Desktop
	- Resource Req.s for VMs
	- App hosting options - Inc. Azure Web Apps, Containers, VNs
	- Virtual Networking - Inc. use case for Azure Virtual Networks, Azure virtual subnets, peering, Azure DNS, VPN Gateway, Express Route
- Define:
	- Public/Private Endpoints

## 2.2.2) Virtual Machines

- Endless Customization - like PC

- Use Cases:
	- Use Custom:
		- OS Ctrl
		- Run Software
		- Hosting Config
	- 

- IaaS offering - Virtualized Server
	- Must Config; Update; Maintain all software
	- Create from scratch 
	- Use pre-built images:
	- Image: 
		- Template used to create VM
		- Can include: OS, Dev. Tools (SDKs); Web Hosting Env.s

### Scale VMs

- Single VMs: 
	- Sep. for Testing; Dev; Minor Tasks
- VM group (cluster)s:
	- High-avail; Scalability; Redundancy
	- Mgmt in Azure: 
		- Scale Sets
		- Availability Sets

	- Scale Sets
		- Create & Manage group of same VMs - Load-balanced
		- Alternate version:
			- create many VMs 
			- ensure identical configs
			- setup network routing params for efficiency
			- resource utilization - monitor need to scale up/down
		- Using Scale set:
			- centrally manage; config; update; scale many VMs
				- scaling: demand/schedule-based
			- automatic load-balancing
		- good choice for Compute, Big Data, Container Workloads

	- Availability Sets
		- Support to build resilient, high-avail env.s
		- Ensure VMs - loss-prevention fr network/power failures: 
			- Stagger updates
			- boast varied power/network connectivity
		- VM Grouping ways:
			- Update domain:
				- VM group to be rebooted at same time
				- enables updates 1 update domain at a time
				- update process with 30m recovery window before next update domain
			- Fault domain:
				- VM group by common power source & network switch
				- Default Availability Set: Split VMs into 3 Fault Domains
					- connected t odifferent physical sources
		- No extra cost of availability set:
			- costs derived from VMs created

- VM Use Cases:
	- Testing & Development
		- quick & easy OS/app config creation
	- Running Applications in Cloud
		- easier/cheaper vs old-school infra setup
		- handle demand fluctuations - inc. 0 demand setup
		- pay-as-you-go/use
	- Extending Data Center To Cloud
		- e.g. run SharePoint in VM
	- Disaster Recovery
		- fall-over/back on VMs

	- Moving to Cloud via VMs
		- Fr Phys. Server --> Cloud - i.e. Lift & Shift
			- still need to maintain VM

- Provisioning Choices:
	- Size - Purpose; Nr Cores; RAM
	- Storage Disks - HDD; SSD
	- Networking - Virt. Netw.; Public IP; Port Config

## 2.2.3) Exercise: Create a VM



## 2.2.4) Azure Virtual Desktop
## 2.2.5) Containers
## 2.2.6) Azure Functions
## 2.2.7) App Hosting Options
## 2.2.8) Azure Virtual Networking
## 2.2.9) Exercise: Config Network Access
## 2.2.10) Aure VPNs
## 2.2.11) Azure ExpressRoute
## 2.2.12) Azure DNS
