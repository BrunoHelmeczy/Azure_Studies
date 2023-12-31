# 1.2) Cloud Service Benefits

## Objectives:
	- Define Cloud Benefits of: 
		- High Availability; Scalability
		- Reliability & Predictability
		- Security & Governance
		- Manageability

## High Availability & Scalability
	- High Availability
		- Solution Architecting --> Consider Service availability guarantees
		- Uptime guarantees:
			- service-dependent
			- Part of SLAs
			- 100% - impractical --> 99%; 99.9%; 99.99...9%, etc.
				- Costly to get higher
	- Scalability 
		- Vertical (Up/Down): Increase/Decrease resource capabilities
			- Add/Subtract CPUs/RAM to VMs
		- Horizontal (In/Out): Add/Subtract Nr of Resources
			- Add/Take away extra VMs/Containers

## Reliability & Predictability
	- Reliability:
		- Def: Systems' Ability to recover & continue functioning
		- Azure well-architected framework pillar
		- Cloud:
			- Natural support for reliable/resilient infrastructure
			- Decentralized design:
				- Resource deployment around the globe - disaster recovery
			- App design can automatically take advantage of reliability
				- E.g. Automatically migrate to different regions
	- Predictability (Planning Ahead):
		- Azure well-architected framework pillar
		- Performance:
			- predict resource needs for good UX
			- Supporting cloud concepts:
				- Autoscaling - add resources when needed
				- Load Balancing - redirect/distribute overload to less stressed regions/areas
				- High Availability

		- Cost:
			- Predict & Monitor Cloud Spending
				- ensure efficient usage
				- data analytics for usage patterns/trends
			- E.g. Tools:
				- Total Cost of Ownership (TCO)
				- Pricing Calculator

## Security & Governance
	- Help to meet corporate/government standards:
		- e.g. Set Templates
		- update resources to new standards when needed
	- Cloud-based auditing:
		- flag non-compliant resources
		- suggest mitigation strategies
	- OpModel dependent: Automatic software pathcing/updates
	
	- Security:
		- Maximum Security Control: IaaS
			- Physical Resources provided only
			- I manage OSs, software, patches/maintenance
				- Auto-patching: PaaS/SaaS
		- Cloud providers well suited to handle DDoS attacks
			- DDoS: Distributed Denail of Service 

## Manageability
	- Things to manage:
		- Autoscaling
		- Template-based resource deployment --> no manual configs
		- Monitor resource health
		- replace failing resources
		- Metrics based auto-alerting
	
	- Mgmt tools for the above:
		- Web Portal
		- CLI
		- API calls
		- PowerShell



