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
