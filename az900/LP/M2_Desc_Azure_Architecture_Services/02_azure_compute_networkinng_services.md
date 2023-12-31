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
- Create Linux VM & Install nginx
	- 1) in Cloud Shell, run:

	```
	az vm create \
		--resource-group learn-abcbde15-1967-42e2-bc65-2014db8841d1 \
		--name my-vm \
		--public-ip-sku Standard \
		--image Ubuntu2204 \
		--admin-username azureuser \
		--generate-ssh-keys
	```
	- Line-by-Line:
		- l1: create VM
		- l2: inside Resource Group: `learn-abcbde15-1967-42e2-bc65-2014db8841d1`
		- l3: with Name: `my-vm`
		- l4: with Public IP SKU: `Standard`
		- l5: Based on Image: `Ubuntu2204`
		- l6: My Username: `azureuser`
		- l7: With access setup via `generate-ssh-keys`

	- Install NginX:

	```
	az vm extension set \
		--resource-group learn-abcbde15-1967-42e2-bc65-2014db8841d1 \
		--vm-name my-vm \
		--name customScript \
		--publisher Microsoft.Azure.Extensions \
		--version 2.1 \
		--settings '{"fileUris":["https://raw.githubusercontent.com/MicrosoftDocs/mslearn-welcome-to-azure/master/configure-nginx.sh"]}' \
		--protected-settings '{"commandToExecute": "./configure-nginx.sh"}'
	```

	- Line-by-Line:
		- l1: run `az vm extension set`
		- l2: inside resource group `learn-abcbde15-1967-42e2-bc65-2014db8841d1`
		- l3: on VM named: `my-vm`
		- l4: a script named `customScript`
		- l5: published by Microsoft Azure
		- l6: version 2.1
		- l7: use the URL above (see script [here](https://raw.githubusercontent.com/MicrosoftDocs/mslearn-welcome-to-azure/master/configure-nginx.sh))
		- l8: execute the command `./configure-nginx.sh`

	- Raw `./configure-nginx.sh` script:

	```
	#!/bin/bash

	sudo apt-get update 				# Update apt cache.

	sudo apt-get install -y nginx		# Install Nginx.

	# Set the home page.
	echo "<html><body><h2>Welcome to Azure! My name is $(hostname).</h2></body></html>" | sudo tee -a /var/www/html/index.html
	```

- TBD: update network config for acces in `2.2.9`

## 2.2.4) Azure Virtual Desktop
- VM type
- Desktop/App virtualization service on Cloud:
	- use cloud-hosted Windows from anywhere - ~VDI
- works with:
	- all devices/OS
	- apps for remote desktops; modern browsers

- Seperate Data/Apps & Hardware
	- Apps running in cloud - reduce data-leakage risk
- Isolated User Sessions 



### Security Enhancement
- Microsoft Entra ID - Centralized Secu Mgmt 4 Users' Desktops
- MFA 4 Secure sign-ins
- Data Security: RBACs

### Multi-Sess Windows 10/11 Deployment
- Azure VD - Windows 10/11 Enterprise multi-session
	- Only Client-based OS to enable multi-session in 1 VM
	- +1s:
		- vs Windows Server-based OSs:
			- More Consistent UX
			- Broader App Support

## 2.2.5) Containers
- VMs: 1 OS / VM --> Containers: Many APP instances on 1 VM/host machine

### Container Def (vs VMs):
- Virtualization Environment
- 1 Physical/Virtual Host/Machine --> Many Containers
- No OS Mgmt in Containers
- VM: Connectable/Manageable OS instance
- Container: Lightweight; Desinged for dynamic creation/scaling/stopping
- VM Scale up: Possible --> Containers: More Agile
	- Designed for dynamic demand
	- Quick restart (crash recovery; hardware problem)

- Azure: Docker Supoprt

### Containers vs VMs
- Azure Container Instances 
	- fastest/simplest container running in Azure
	- No VM Mgmt; Other Services Adoption
	- PaaS offering 
	- Upload containers; service runs containers for you

- Azure Container Apps
	- Similar to container instances 
		- Quick startup; No Container Mgmt; PaaS offering 
		- +1s: Load Balancing/Scaling 

- Azure Kubernetes Service
	- Container Orchestration Service:
		- Container Lifecycle Mgmt

	- Container Fleet Deployment: AKS 
		- Simple; Efficient fleet Mgmt

### Container Use-Cases
- microservice architecture-based Solutions
	- Break solutions into small independent pieces
	- E.g.: 1-1 Container for Website Front End; Back End; Storage
		- App Modularization: 
			- logical sections 
			- Independent maintainence/scaling/updates
-

Imagine your website back-end has reached capacity but the front end and storage aren't being stressed
- With containers, you could scale the back end separately to improve performance
- If something necessitated such a change, you could also choose to change the storage service or modify the front end without impacting any of the other components
-

## 2.2.6) Azure Functions
## 2.2.7) App Hosting Options
## 2.2.8) Azure Virtual Networking
## 2.2.9) Exercise: Config Network Access
## 2.2.10) Aure VPNs
## 2.2.11) Azure ExpressRoute
## 2.2.12) Azure DNS
