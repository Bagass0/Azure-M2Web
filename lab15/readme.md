# Lab 15: Implementing Azure DevOps for CI/CD Pipelines

## 1. Set up an Azure DevOps Organization and Project

### Azure DevOps Portal
1. Navigate to **Azure DevOps** at [dev.azure.com](https://dev.azure.com/).
2. Sign in with your credentials.
3. In the **Azure DevOps** dashboard, click on **New Organization** if you don’t have one yet.
4. Once your organization is created, click on **New Project**.
   - Give your project a name.
   - Choose visibility (private or public).
   - Click **Create** to finalize the project.

---

## 2. Create a Git Repository and Commit Code
```bash
   git clone <YourRepositoryURL>
   git add .
   git commit -m "Initial commit"
   git push origin master
``` 
```bash
# Create an Azure DevOps project via CLI (with DevOps extension installed)
az devops project create --name <ProjectName>

# Create a new Git repository
az repos create --name <RepoName>

# Clone the repository
git clone <YourRepositoryURL>

# Commit and push code
git add .
git commit -m "Initial commit"
git push origin master
``` 

## 3. Configure a CI Pipeline to Build the Application
```yml
trigger:
  branches:
    include:
      - master

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: UseNode@2
  inputs:
    versionSpec: '14.x'
  displayName: 'Install Node.js'

- script: |
    npm install
    npm run build
  displayName: 'Install dependencies and build'
``` 
```bash
# Create a service connection to Azure (if not already set up)
az devops service-endpoint azurerm create \
  --name <ConnectionName> \
  --resource-group <ResourceGroup> \
  --project <ProjectName>

# Create a pipeline via Azure CLI (YAML template required)
az pipelines create \
  --name <PipelineName> \
  --repository <RepoName> \
  --branch master \
  --yml-path azure-pipelines.yml
``` 

## 4. Set up a CD Pipeline to Deploy an App Template to Azure App Service
```yml
trigger:
  branches:
    include:
      - master

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: UseNode@2
  inputs:
    versionSpec: '14.x'
  displayName: 'Install Node.js'

- script: |
    npm install
    npm run build
  displayName: 'Install dependencies and build'
``` 
```bash
# Create a service connection to Azure (if not already set up)
az devops service-endpoint azurerm create \
  --name <ConnectionName> \
  --resource-group <ResourceGroup> \
  --project <ProjectName>

# Create a pipeline via Azure CLI (YAML template required)
az pipelines create \
  --name <PipelineName> \
  --repository <RepoName> \
  --branch master \
  --yml-path azure-pipelines.yml
``` 
