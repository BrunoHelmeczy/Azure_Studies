#! /usr/bin/sh

# Create random string
guid=$(cat /proc/sys/kernel/random/uuid)
suffix=${guid//[-]/}
suffix=${suffix:0:18}

# Set env variables
RESOURCE_GROUP="rg-dp100-l${suffix}"
RESOURCE_PROVIDER="Microsoft.MachineLearning"
REGION="westeurope"
WORKSPACE_NAME="mlw-dp100-l${suffix}"
COMPUTE_INSTANCE="ci${suffix}"
COMPUTE_CLUSTER="aml-cluster"

# Register Azure ML resource provider in subscription
echo "1. Register the ML resource provider:"
az provider register --namespace $RESOURCE_PROVIDER

# Create resource group & workspace & set default
echo "2. Create Resource Group and set as default: " $RESOURCE_GROUP " at location: " $REGION
az group create --name $RESOURCE_GROUP --location $REGION
az configure --defaults group=$RESOURCE_GROUP

echo "3. Create an Azure ML Workspace: " $WORKSPACE_NAME
az ml workspace create --name $WORKSPACE_NAME 
az configure --defaults workspace=$WORKSPACE_NAME 

# Create compute instance
echo "4. Create compute instance with name: " $COMPUTE_INSTANCE
az ml compute create --name ${COMPUTE_INSTANCE} --size STANDARD_DS11_V2 --type ComputeInstance 

# # Create compute cluster
# echo "Creating a compute cluster with name: " $COMPUTE_CLUSTER
# az ml compute create --name ${COMPUTE_CLUSTER} --size STANDARD_DS11_V2 --max-instances 2 --type AmlCompute 

# # Create data assets
# echo "Create training data asset:"
# az ml data create --type uri_file --name "diabetes-data" --path ./data/diabetes.csv 