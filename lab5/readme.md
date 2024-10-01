# Lab 5: Implementing Azure SQL Databases

## 1. Déploiement d'une instance de base de données Azure SQL

### Interface Azure
![Image 1](./1.png)
![Image 2](./2.png)

### Équivalent en Azure CLI
```bash
az sql server create \
  --name <NomDuServeurSQL> \
  --resource-group <VotreResourceGroup> \
  --location <Emplacement> \
  --admin-user <NomAdmin> \
  --admin-password '<VotreMotDePasse>'

az sql db create \
  --resource-group <VotreResourceGroup> \
  --server <NomDuServeurSQL> \
  --name <NomDeLaBaseDeDonnées> \
  --service-objective S0
```

## 2. Configuration des règles de pare-feu pour permettre l'accès des clients

### Interface Azure
![Image 3](./3.png)
![Image 4](./4.png)

### Équivalent en Azure CLI
```bash
az sql server firewall-rule create \
  --resource-group <VotreResourceGroup> \
  --server <NomDuServeurSQL> \
  --name AllowClientIP \
  --start-ip-address <AdresseIPClient> \
  --end-ip-address <AdresseIPClient>
```

## 3. Importation de données dans la base de données

### Interface Azure
![Image 5](./5.png)

### Équivalent en Azure CLI
```bash
az sql db import \
  --admin-user <NomAdmin> \
  --admin-password '<VotreMotDePasse>' \
  --storage-uri <URIduFichierBacpac> \
  --name <NomDeLaBaseDeDonnées> \
  --resource-group <VotreResourceGroup> \
  --server <NomDuServeurSQL>
```
