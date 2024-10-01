# Lab 1: Creating and Managing Azure Virtual Machines (Linux)

### Interface Azure

##### Création Ressource Group + VM
![Image 1](./2.png)
![Image 2](./3.png)
![Image 3](./4.png)
![Image 1](./1.png)
##### Connection ssh
![Image 2](./5.png)
##### Install tree
![Image 3](./6.png)

### Équivalent en Azure CLI

```bash
az vm create \
  --resource-group <VotreGroupeDeRessources> \
  --name <VotreNomDeVM> \
  --image UbuntuLTS \
  --admin-username <VotreNomUtilisateur> \
  --admin-password '<VotreMotDePasse>' \
  --size Standard_D2s_v3 \
  --public-ip-sku Standard
