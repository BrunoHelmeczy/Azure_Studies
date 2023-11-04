[Question Bank](https://www.itexams.com/exam/AZ-900?)

* Note: These appear when you didn't login


### 1) Match the cloud model to the correct advantage - Private, Public, Hybrid
Instructions: To answer, drag the appropriate cloud model from the column on the left to its advantage on the right. Each cloud model may be used once, more than once, or not at all.
NOTE: Each correct match is worth one point
Select and Place:

Cloud Models: 
1) Hybrid
2) Private
3) Public
Advantages:

- a. No required CapEx
- b. Complete control over security
- c. Choice to use on-prem or cloud-based resources

Ans: 3a; 2b; 1c

Exp: 
a) Public Cloud - With a public cloud, there is no capital expenditure on server hardware etc. You only pay for cloud resources that you use as you use them.

b) Private Cloud - A private cloud exists on premises, so you have complete control over security.

c) Hybrid Cloud - A hybrid cloud is a mix of public cloud resources and on-premises resources. Therefore, you have a choice to use either.

### 2) Yes if true, No otherwise - Private, Public, Hybrid
NOTE: Each correct selection is worth one point.

- a. A company can extend a private cloud by adding its own physical servers to the public cloud: 
- b. To build hybrid cloud, you must deploy resources to the public cloud
- c. A Private cloud must be disconnected from the internet

Answer: a) False; b) True; c) True [Ref](https://azure.microsoft.com/en-gb/overview/what-are-private-public-hybrid-clouds/)


a) No - You cannot add physical servers to the public cloud. You can only deploy virtual servers in the public cloud. You can extend a private cloud by deploying virtual servers in a public cloud. This would create a hybrid cloud.

b) Yes - A hybrid cloud is a combination of a private cloud and public cloud. Therefore, to create a hybrid cloud, you must deploy resources to a public cloud.

c) No - It is not true that a private cloud must be disconnected from the Internet. Private clouds can be and most commonly are connected to the Internet. ג€Private cloudג€ means that the physical servers are managed by you. It does not mean that it is disconnected from the Internet.

### 3) Which type of cloud model is this? - Private, Public, Hybrid
You have 50 virtual machines hosted on-premises and 50 virtual machines hosted in Azure. The on-premises virtual machines and the Azure virtual machines connect to each other.

a. hybrid
b. private
c. public

Answer: a. Hybrid [Ref](https://azure.microsoft.com/en-gb/overview/what-is-hybrid-cloud-computing/)

### 4) Yes if true, No otherwise. - PaaS
NOTE: Each correct selection is worth one point.

- a. A Platform as a service solution that hosts web apps in Azure provides full control of the OSs hosting the applications
- b. A Platform as a service solution that hosts web apps in Azure can be provided with additional memory by changing the pricing tier
- c. A Platform as a service solution that hosts web apps in Azure can be configured to automatically scale the number of instances based on demand

Ans: a) False; b) True; c) True

Exp: [Ref](https://azure.microsoft.com/en-gb/overview/what-is-paas/)

- a. No - A PaaS solution does not provide access to the operating system. The Azure Web Apps service provides an environment for you to host your web applications. Behind the scenes, the web apps are hosted on virtual machines running IIS. However, you have no direct access to the virtual machine, the operating system or IIS.

- b. Yes
- c. Yes - A PaaS solution that hosts web apps in Azure does provide the ability to scale the platform automatically, i.e. autoscale. Behind the scenes, the web apps are hosted on VMs running IIS. Autoscaling means adding more load balanced virtual machines to host the web apps.


### 5) PaaS, SaaS, IaaS

Note: Question part of a series presenting the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

Your company plans to migrate all its data and resources to Azure. The company's migration plan states that only Platform as a Service (PaaS) solutions must be used in Azure. You need to deploy an Azure environment that meets the company migration plan.

Solution: You create Azure virtual machines, Azure SQL databases, and Azure Storage accounts.

Does this meet the goal?

Ans: No

Exp: 

PaaS: 
- complete dev- & deployment cloud env & includes infrastructure, e.g.:
    - servers, storage, networking
    - +1s: middleware, development tools, BI services, DB Mgmt systems, etc.
- designed to support complete web app lifecycle: building, testing, deploying, managing, updating

VMs:
- examples of IaaS: instant computing infrastructure, provisioned & managed via internet

Ref: [PaaS](https://azure.microsoft.com/en-us/overview/what-is-paas/), [IaaS](https://azure.microsoft.com/en-us/overview/what-is-iaas/)

### 6) PaaS, SaaS, IaaS

Company plans to deploy several custom apps to Azure. Apps will provide invoicing services to companys' customers. Each app will have several prerequisite apps & services installed.
You need to recommend a cloud deployment solution for all the applications.

What should you recommend?
- A. SaaS
- B. PaaS
- C. laaS

Ans: C. IaaS

Exp: 

**IaaS**: instant computing infrastructure, provisioned and managed over the internet: 
- Azure manages infrastructure
- you purchase, install, configure, manage own software

Incorrect Answers:
- **A:** SaaS: allows users to connect to and use cloud-based apps over the Internet: 
    - e.g.: email, calendaring, office tools. 
    - In this scenario: need to run own apps -->  infrastructure required

- **B:** PaaS: complete cloud development-; deployment environment:
    - includes infrastructure: servers, storage, networking + middleware, dev tools, BI services, DB Mgmt systems, and more. 
    - Designed to support complete web app lifecycle: building, testing, deploying, managing, and updating.

Ref: [IaaS](https://azure.microsoft.com/en-us/overview/what-is-iaas/), [SaaS](https://azure.microsoft.com/en-us/overview/what-is-saas/), [PaaS](https://azure.microsoft.com/en-us/overview/what-is-paas/)

### 7) Yes if True, Otherwise No - OpEx/CapEx

- a. Building a data center infrastructure is an example of operational expenditure cost
- b. Monthly salaries of technical personnel are an example of operational expenditure costs
- c. Leasing software is an example of operational expenditure costs

Ans: a. No; b. Yes; c. Yes

Exp:
- a. No: Investing into Buidling data center = Capital Expenditure
- b. Yes: Operational Expenditure: Ongoing costs (cost of operations) - e.g. staff salaries
- c. Yes: OpEx = Ongoing costs. 1-time software purchase = CapEx; but leasing = OpEx

### 8) Complete the Sentence: Cosmos DB

Azure Cosmos DB is an example of ............. offering.

- a. PaaS
- b. IaaS
- c. Serverless
- d. SaaS


Ans: a. PaaS Ref: [Cosmos DB](https://docs.microsoft.com/en-us/azure/cosmos-db/database-security)

### 9) Yes if True, Otherwise No - PaaS, SaaS, IaaS

- a. Using SaaS, you must apploy software updates
- b. Using IaaS, you must install the software that you want to use
- c. Azure Backup: Example of PaaS

Ans: a. No; b. Yes; c. Yes

Exp: [IaaS](https://azure.microsoft.com/en-us/overview/what-is-iaas/), [SaaS](https://azure.microsoft.com/en-us/overview/what-is-saas/), [PaaS](https://azure.microsoft.com/en-us/overview/what-is-paas/)

### 10) Yes if True, Otherwise No - Resource Groups

- a. You can create a resource group inside of another resource group
- b. Az Azure VM can be in multiple resource groups
- c. A resource group can contain resources from multiple Azure regions

Ans: a. No; b. No; c. Yes

Exp: 

- a. No
- b. No - Each resource can exist in only one resource group.
- c. Yes - Resources from multiple different regions can be placed in a resource group. The resource group only contains metadata about the resources it contains

Refs: [Resource Groups Overview](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-overview), [Effective Res. Mgmt in Res. Groups](https://www.codeisahighway.com/effective-ways-to-delete-resources-in-a-resource-group-on-azure/)


### 11) Yes if True, Otherwise No - DB types

- a. MS SQL Server 2019 installed on Azure VM is example of PaaS
- b. Azure SQL Database is example of PaaS
- c. Azure Cosmos DB is example of SaaS

Ans: a. No; b. Yes; c. No

Ref: [SQL IaaS vs PaaS](https://docs.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview), [Cosmos DB Account DB Containers](https://docs.microsoft.com/en-us/azure/cosmos-db/account-databases-containers-items), [Cosmos DB Overview](https://www.red-gate.com/simple-talk/cloud/azure/overview-of-azure-cosmos-db) 


### 12) Complete Sentence: MS SQL Server

MS SQL Server DB hosted in the cloud and has software updates managed by azure is an example of ..........

- a. DRaaS: Disaster Recovery as a Service 
- b. IaaS
- c. PaaS
- d. SaaS

Ans: c. PaaS Ref: [SQL IaaS vs PaaS](https://docs.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview)

### 13) Scenario-based - PaaS, IaaS, SaaS offerings

Your company plans to migrate all its data and resources to Azure.
The company's migration plan states that only Platform as a Service (PaaS) solutions must be used in Azure.
You need to deploy an Azure environment that meets the company's migration plan.

What should you create?

- a. VMs, SQL databases, & Storage accounts.
- b. an App Service & VMs that have MS SQL Server installed.
- c. an App Service & SQL databases.
- d. storage accounts & web server in VMs

Ans: c.

Exp: 
- App Service & SQL DBs: PaaS solution example.
- VMs - IaaS
- Storage Accounts - PaaS 

### 14) SaaS

What does a customer provide in a SaaS model?
- a. application data
- b. data storage
- c. compute resources
- d. application software

Ans: a. App Data

Exp: 
- SaaS: complete software solution purchased on pay-as-you-go basis from cloud provider. 
    - rent app usage for org + users connect via Internet 
    - Underlying infra, middleware, app software & data located at service provider data center
    - Provider manages hardware; software:
        - +1: with appropriate SLA, ensure app & data availability; security

### 15) Yes if True, Otherwise No - PaaS, IaaS, SaaS offerings

- a. Azure Files - IaaS
- b. DNS Server running on VM - PaaS
- c. Microsoft Intune - SaaS

Ans: a. Yes, b. Yes, c. Yes

Exp: [IaaS](https://azure.microsoft.com/en-us/overview/what-is-iaas/), [SaaS](https://azure.microsoft.com/en-us/overview/what-is-saas/), [PaaS](https://azure.microsoft.com/en-us/overview/what-is-paas/)


