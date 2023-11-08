[Question Bank](https://www.itexams.com/exam/AZ-900?)

* Note: These appear after you logged in

### 1) Multi-Choice - Support Plans

Company intends to subscribe to an Azure support plan. Plan must allow for new support requests to be opened.

Which of the following are support plans that will allow this? Answer by dragging the correct option from the list to the answer area.

- a. Basic
- b. Developer
- c. Standard
- d. Professional Direct
- e. Premier

Ans: All exc. Basic: b., c., d., e.

Exp: [Support Plans](https://azure.microsoft.com/en-us/support/plans/)

### 2)

Company datacenters in LA & NYC. Company has Azure subscription.

Configure the 2 datacenters as geo-clustered sites for site resiliency. Recommend an Azure storage redundancy option.

Data storage requirements:
- Data must be stored on multiple nodes.
- Data must be stored on nodes in separate geographic locations.
- Data can be read from the secondary location as well as from the primary location

Which of the following Azure stored redundancy options should you recommend?
- a. Geo-redundant storage
- b. Read-only geo-redundant storage
- c. Zone-redundant storage
- d. Locally redundant storage

Ans: b. 

Refs: [Storage Redundancy](https://docs.microsoft.com/en-us/azure/storage/common/storage-redundancy), [RA-GRS](https://docs.microsoft.com/en-us/azure/storage/common/storage-redundancy-grs#read-access-geo-redundant-storage)

Exp: 
- RA-GRS: allows higher read availability for storage account: 
    - provide read-only access to data replicated to 2nd location. 
    - Once enabled: 2nd location - use for higher availability - data not available in 1st region
    - +1: Opt-in feature - requires geo-replicated storage account

### 3) T/F - Support Plan

- Company's Azure subscription includes Basic support plan.

They would like to request an assessment of an Azure environment's design from Microsoft. This is, however, not supported by the existing plan. You want to make sure that the company subscribes to a support plan that allows this functionality, while keeping expenses to a minimum.

Solution: You recommend that the company subscribes to the Professional Direct support plan.
Does the solution meet the goal?
- a. Yes
- b. No

Ans: b. No - too expensive 

Ref: [Plans](https://azure.microsoft.com/en-gb/support/plans/)
- Azure Advisor; Helath Status & Notifications; Architecture Support - All Included in Basic


### 4) T/F - VMs

Note: The question is included in a number of questions that depicts the identical set-up. However, every question has a distinctive result. Establish if the solution satisfies the requirements.

You are tasked with deploying Azure virtual machines for your company. You need to make use of the appropriate cloud deployment solution.

Solution: You should make use of Software as a Service (SaaS).
Does the solution meet the goal?
- a. Yes
- b. No

Ans: b. No - Need a bunch of other stuff - e.g. deploy where, access/secure how


### 5) T/F - VMs

You are tasked with deploying Azure virtual machines for your company. You need to make use of the appropriate cloud deployment solution.

Solution: You should make use of Platform as a Service (PaaS).
Does the solution meet the goal?
- a. Yes
- b. No

Ans: b. No 

### 6) T/F - VMs

You are tasked with deploying Azure virtual machines for your company. You need to make use of the appropriate cloud deployment solution.

Solution: You should make use of Infrastructure as a Service (IaaS).
Does the solution meet the goal?
- a. Yes
- b. No

Ans: a. Yes 

### 7) Multi-Choice - Web App Hosting

Devs created 10 web apps to be hosted on Azure.
You need to determine which Azure web tier plan to host web apps. The web tier plan must meet the following requirements:
- The web apps will use custom domains.
- The web apps each require 10 GB of storage.
- The web apps must each run in dedicated compute instances.
- Load balancing between instances must be included.
- Costs must be minimized.

Which web tier plan should you use?
- a. Standard
- b. Basic
- c. Free
- d. Shared

Ans: b. Basic

Exp: Standard offers 50gb; Basic: 10gb

Ref: [Website Pricing](http://azure.microsoft.com/en-us/pricing/details/websites/)


### 8) T/F - 

You are planning to migrate a company to Azure. 
Each Company division will have an admin to manage the Azure resources used by their respective division.
You want to make sure that the Azure deployment you employ allows for Azure to be segmented for the divisions, while keeping administrative effort to a minimum.

Solution: You plan to make use of several Azure Active Directory (Azure AD) directories.
Does the solution meet the goal?
- a. Yes
- b. No

Ans: b. No

### 9) Multi-choice - Web App Hosting

Devs created a portal web app for users in the Miami branch office. 
Web app will be publicly accessible and used by the Miami users to retrieve customer and product information. The web app is currently running in an on-premises test environment.

You plan to host the web app on Azure.
You need to determine which Azure web tier plan to host the web app. The web tier plan must meet the following requirements:
- The website will use the miami.weyland.com URL.
- The website will be deployed to 2 instances.
- SSL support must be included.
- The website requires 12 GB of storage.
- Costs must be minimized.

Which web tier plan should you use?
- a. Standard
- b. Basic
- c. Free
- d. Shared

Ans: a. Standard - Exp [Azure Sub Service Limits](http://azure.microsoft.com/en-us/documentation/articles/azure-subscription-service-limits/)

### 10) T/F - Expenditure Models

Your company is planning to migrate all their VMs to an Azure pay-as-you-go subscription. The VMs are currently hosted on the Hyper-V hosts in a data center.
You are required to make sure the intended Azure solution uses the correct expenditure model.

Solution: You should recommend the use of the elastic expenditure model.
Does the solution meet the goal?
- a. Yes
- b. No

Ans: b. No

Exp: The correct expenditure model is "Operational" [Ref](https://stackoverflow.com/questions/70150448/difference-between-elastic-and-scalable-expenditure-model)

### 11) T/F - Expenditure Models

Your company is planning to migrate all their VMs to an Azure pay-as-you-go subscription. The VMs are currently hosted on the Hyper-V hosts in a data center.
You are required make sure that the intended Azure solution uses the correct expenditure model.

Solution: You should recommend the use of the scalable expenditure model.
Does the solution meet the goal?
- a. Yes
- b. No

Ans: a. No

Exp: The correct expenditure model is "Operational" [Ref](https://stackoverflow.com/questions/70150448/difference-between-elastic-and-scalable-expenditure-model)

### 12) T/F - Expenditure Models

Your company is planning to migrate all their virtual machines to an Azure pay-as-you-go subscription. The virtual machines are currently hosted on the Hyper-V hosts in a data center.
You are required make sure that the intended Azure solution uses the correct expenditure model.

Solution: You should recommend the use of the operational expenditure model.
Does the solution meet the goal?
- a. Yes
- b. No

Ans: a. Yes

Exp: The correct expenditure model is "Operational" [Ref](https://stackoverflow.com/questions/70150448/difference-between-elastic-and-scalable-expenditure-model)


### 13) T/F - AI

You are required to deploy an Artificial Intelligence (AI) solution in Azure.
You want to make sure that you are able to build, test, and deploy predictive analytics for the solution.

Solution: You should make use of Azure Cosmos DB.
Does the solution meet the goal?
- a. Yes
- b. No

Ans: b. No


### 14)
### 15)