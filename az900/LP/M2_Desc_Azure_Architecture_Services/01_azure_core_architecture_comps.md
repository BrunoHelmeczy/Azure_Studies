# 2.1) Azure Core Architectural Components

## Objectives:
	- Describe: 
        - Azure: 
            - Regions, Region Pairs, Sovereign Regions
            - Availability Zones
            - Datacenters
            - Resources; Resource Groups
        - Subscriptions
        - Mgmt Groups
        - Hierarchy for Resource Groups, Subcriptions, Mgmt Groups

 

## Microsoft Azure
- Expending Cloud Services - help to meet business needs
- Offers:
    - Freedom to:
        - Build; Manage; Deploy Apps 
        - on Global/Massive scale
        - Using Favorite Tools/Frameworks

### Azure Offering
- Future Proof
    - Continuous Innovation for Azure:
        - Support Dev. today + Future Visions
- Building on own Terms:
    - Many Options/Choices + Commitment 2 Open Source
        - Support for most Languages/Frameworks
        - Build How/Deploy Where you want to
- Seamlessly Hybrid
    - On-prem/Cloud-native/in-between

- Trust in Cloud:
    - Ground up security
    - Backed by expert teams
    - Proactive compliance 
    - Trusted by Enterprises/Governments/Startups

### What can I do with Azure
- 100+ services/offers:
    - e.g.:
        - run existing apps on VMs
        - Explore new software paradigms - intelligent bots; mixed reality
        - AI/ML services
            - also Vision/Hearing/Speech
        - Storage Solutions

- Common start:
    - Move existing app to VM - run in Azure
        - Good start - Cloud offers much more

## Get started with Azure Accounts

- ![Alt text](pics/account_resource_hierarchy.png)

- [Azure Portal Home Page](https://portal.azure.com/#home)

### Microsoft Learn Sandbox
- Temp Sandbox Env. to complete LP exercises
- Creates Temp Subscriptions
    - added to your Azure accounts
    - allows resource creation during Learn Modules
    - automatically cleans up temp resources after acompleting the module

- FYI:
    - can use Personal Subscription for exercies
    - Sandbox is preferred:
        - Create/Test azure resources for free!!!
    
## Explore Learn Sandbox

- 1) Use ***Powershell CLI***
    - Current Date: `Get-date`
    - Azure specific Commands:
        - Uses ***Azure CLI***: `az ...`
            - version test: `az version`

- 2) Use ***Bash CLI***
    - Switch to bash from Powershell CLI: `bash`
    - Current Date: `date`
    - Run Azure CLI commands: `az ...`
        - e.g. Upgrade Azure CLI: `az upgrade`
    - return to Powershell Mode: `pwsh`

- 3) Use Azure CLI Interactive Mode
    - Enter Interactive Mode: `az interactive`
        - this is Azure specific - no need for `az ` preposition
            - Version check: `version`
            - Upgrade: `upgrade`
            - Exit: `exit`

- 4) Use the Azure Portal
    - Option will show/pop-up for sandbox exercises
        - Use provided link
            - Keeps exercises free for user

## Azure Physical Infrastructure
- Important Terms: Regions; Availability Zones; Resources; Subscriptions, etc.
- 2 Core architectural Component Groups:
    - Physical Infrastructure
    - Mgmt Infrastructure

### Physical Infrastructure
- Start: DataCenter
    - Same as Large Corporate Datacenter
    - Facilities with Racks of Resources; Dedicated Power, Cooling; Networking Infra

- Azure: Datacenters around the globe
    - Inaccessible Directly
    - Grouped into: 
        - Azure Regions 
        - Availability Zones
    - Designed for Resilience/Reliability

### Regions
- Def: Geopraphical Area containing at least 1 datacenter that is nearby and networked together with low-latency network
    - TLDR:
        - Geographical Area
        - Contains 1/more datacenter
        - Is close by
        - Is connected with low-latency network
    - Azure:
        - Intelligent Resource Control/Assignment within Region
            - Ensure well-balanced workloads

- Upon Resource Deployment: Choosing regoin to be deployed on 
- +1s: 
    - Some Services/VM features - Region-specific Availability
    - Services without Region Selection:
        - Azure Active Directory
        - Azure Traffic Manager
        - Azure DNS

### Availability Zones
- Def: Physically separate datacenters within Azure Regions
    - Made up of 1+ datacenters with:
        - Independent Power; Cooling; Networking
- Set up to an Isolation Boundary
    - i.e. If/When 1 Zone goes down; other continues working
- Availability Zones:
    - Connected through high-speed, private fiber-optic networks:
    - Resilience Insurance:
        - 3+ Availability Zones per Region
            - Availability Zone Enabled Regions
    - Not all Azure Regions support Availability Zones

- ![Alt text](pics/regions_avail_zones.png)

- Usage in your Apps
    - Ensure Service/Data Redundancy:
        - Fail-Proof/Protect information
    - Own Infrastructure hosting setup:
        -  Create duplicate hardware environments --> Availability Zones
    - Co-Locate Compute; Storage; Network; Data Resources in Availability Zone
        - Then Replicate then in another
        - Cost associated with resource duplication
    - Primary Purpose: 
        - VMs; Managed Disks; Load Balancers; SQL DBs
        - 3 Categories:
            - Zonal Services:
                - Pin Resource to Specific Zone
            - Zone-Redundant Services:
                - Platform Replicated Automatically Across Zone
                    - e.g. Zone-Redundant Storage; SQL DBs
            - Non-Regional Services:
                - Always available from Azure Geopraphies
                - Resilient to Zone/Region-Wide Outages

    - Additional Resiliency --> Region Pairs

### Region Pairs
- TBC from [here](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/5-describe-azure-physical-infrastructure)
    - Regions Pairs section
