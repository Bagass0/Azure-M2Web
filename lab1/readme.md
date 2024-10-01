# Lab 1: Creating and Managing Azure Virtual Machines (Linux)

### Interface Azure

![Image 1](./2.png)
![Image 2](./3.png)
![Image 3](./1.png)
![Image 1](./4.png)
![Image 2](./6.png)
![Image 3](./5.png)

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
