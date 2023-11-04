[Question Bank](https://www.itexams.com/exam/AZ-900?)


### 1) Match the cloud model to the correct advantage.
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

### 2) For each statements, select Yes if statement is true, and No otherwise.
NOTE: Each correct selection is worth one point.

- a. A company can extend a private cloud by adding its own physical servers to the public cloud: 
- b. To build hybrid cloud, you must deploy resources to the public cloud
- c. A Private cloud must be disconnected from the internet

Answer: a) False; b) True; c) True [Ref](https://azure.microsoft.com/en-gb/overview/what-are-private-public-hybrid-clouds/)


a) No - You cannot add physical servers to the public cloud. You can only deploy virtual servers in the public cloud. You can extend a private cloud by deploying virtual servers in a public cloud. This would create a hybrid cloud.

b) Yes - A hybrid cloud is a combination of a private cloud and public cloud. Therefore, to create a hybrid cloud, you must deploy resources to a public cloud.

c) No - It is not true that a private cloud must be disconnected from the Internet. Private clouds can be and most commonly are connected to the Internet. ג€Private cloudג€ means that the physical servers are managed by you. It does not mean that it is disconnected from the Internet.

### 3) Which type of cloud model is this?
You have 50 virtual machines hosted on-premises and 50 virtual machines hosted in Azure. The on-premises virtual machines and the Azure virtual machines connect to each other.

a. hybrid
b. private
c. public

Answer: a. Hybrid [Ref](https://azure.microsoft.com/en-gb/overview/what-is-hybrid-cloud-computing/)

### 4) For each statements, select Yes if statement is true, and No otherwise.
NOTE: Each correct selection is worth one point.

- a. A Platform as a service solution that hosts web apps in Azure provides full control of the OSs hosting the applications
- b. A Platform as a service solution that hosts web apps in Azure can be provided with additional memory by changing the pricing tier
- c. A Platform as a service solution that hosts web apps in Azure can be configured to automatically scale the number of instances based on demand

Ans: a) False; b) True; c) True

Exp: [Ref](https://azure.microsoft.com/en-gb/overview/what-is-paas/)

- a. No - A PaaS solution does not provide access to the operating system. The Azure Web Apps service provides an environment for you to host your web applications. Behind the scenes, the web apps are hosted on virtual machines running IIS. However, you have no direct access to the virtual machine, the operating system or IIS.

- b. Yes
- c. Yes - A PaaS solution that hosts web apps in Azure does provide the ability to scale the platform automatically, i.e. autoscale. Behind the scenes, the web apps are hosted on VMs running IIS. Autoscaling means adding more load balanced virtual machines to host the web apps.


### 5) 

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

### 6) 