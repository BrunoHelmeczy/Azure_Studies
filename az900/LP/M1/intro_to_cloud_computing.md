# 1.1) Intro 2 Cloud Computing

## Objectives:
  - Define: 
    - Cloud computing
    - cloud models (public, private, hybrid)
  - Describe:
    - Shared responsibility Model
    - consumption-based model
  - Compare cloud pricing models

## Cloud Computing:
    - Compute services delivery over internet
    - Compute Services:
        - Common IT Infrastructure: VMs, Storage, DBs, Networking
    - Other Cloud Services:
        - IoT, ML, AI
    - Delivered over Internet --> No Physical contraints (Load Balancing/adjustment)

## Shared Responsibility Model
    - Corp Data Center - Company Responsibilities:
        - Maintain/Replace - Physical space; Servers; IT Infrastructure; Software; Patching
        - Ensure - Security
    - Shared Resp. --> Between Cloud Providers & Consumers:
        - Provider: 
            - Physical Security, Power, Cooling, Network connectivity
        - Consumer:
            - Data Stored; Access Security
        - Many Details --> Context dependent:
            - SQL DB --> Provider: DB Maintenance; Consumer: Data ingested
            - DB inside a VM --> Consumer: Data Ingested; DB Maintenance 
    - Constant Resp.s:
        - Consumer: Data Stored in Cloud; Devices/Accounts/IDs allowed to connect
        - Provider: Physical Datacenter/Network/Host

    - Model Types:
        - IaaS (Infra as a Service):
            - Most Resp. on Consumer
            - Provider Resp.s:
                - Phys. Sec.; Power, Connectivity 
        - PaaS (Infra as a Service):
            - Resp.s similarly distributed
        - SaaS (Infra as a Service):
            - Provider Resp.s:
                - Most Resp.s on Provider

![Bla](pics/shared_resp_models.png)

## Cloud Models
    - Private; Public; Hybrid

    - Private Cloud:
        - Evolution from On-Prem/Corp. Datacenter
        - Cloud used by 1 entity
        - Greatest Company/IT Departmental Control
        - Most Costly
        - Can be hosted: on-prem/dedicated datacenter (also 3rd part potentially)
    - Public Cloud:
        - Built; Controlled; Maintained by 3rd Party (Azure, GCP, AWS)
        - Anyone can purchase cloud services (access/use resources)
        - Key difference: General Public Availability
    - Hybrid Cloud:
        - 

