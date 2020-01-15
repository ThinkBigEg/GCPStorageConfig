# GCPStorageConfig
## package installation 
- install git 
```
sudo apt install git
```
- clone GCPStorageConfig package  
```
git clone https://github.com/ThinkBigEg/GCPStorageConfig.git
```
- installing library 
```
pip install /path/to/GCPStorageConfig/
```
## using api 
###1- Create a Role with sufficient priviledges
Create a new Role from [here](https://console.cloud.google.com/iam-admin/roles) and assign to it the following permissions:
  - storage.buckets.get
  - storage.buckets.list
  - storage.buckets.update
  - storage.objects.create
  - storage.objects.delete
  - storage.objects.get
  - storage.objects.list
  - storage.objects.update
  
### 2- Create a Service Account
Create a new Service Account, assign to it the custom role created in (1) and create a single 
JSON Service Account ```Key```. The JSON Key (file) shall be used by your applications in order to authenticate 
to GCP (more on that later). You can create a Service Account with a single key, 
from [here](https://console.cloud.google.com/apis/credentials), 
alternatively [this interface](https://console.cloud.google.com/iam-admin/serviceaccounts) can be used.

