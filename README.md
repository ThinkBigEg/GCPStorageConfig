# GCPStorageConfig

GCPStorageConfig is a library that lets you define and store configuration data 
as a hierarchy of key value pairs in Google Cloud Platform - Cloud Storage. 
You can use these key value pairs as a way to:
- Dynamically configure services
- Communicate service states
- Send notification of changes to data
- Share information between multiple tiers of services

This library provides a simple and convenient replacement to [GCP's Runtime Configuration](https://cloud.google.com/deployment-manager/runtime-configurator/)
feature which is currently in Beta. More information on the rational behind the development 
of this library can be found in this detailed [blog post]().


## Package installation

- Clone this repository
```
git clone https://github.com/ThinkBigEg/GCPStorageConfig.git
```

- Change branches for python 3.x 
```
cd /path/to/GCPStorageConfig/
git checkout dev
``` 

- Change branches for python 2.x
 ```
cd /path/to/GCPStorageConfig/
git checkout dev_python_2_7
```

- Install
```
pip install /path/to/GCPStorageConfig/
```

## Pre-requisites
This package interacts with your GCP Project - Cloud Storage. It needs to use a GCP 
Service Account with sufficient permissions

###1- Create a Role with sufficient privileges
Create a new Role from [here](https://console.cloud.google.com/iam-admin/roles) 
and assign to it the following permissions:
  - storage.buckets.get
  - storage.buckets.list
  - storage.buckets.update
  - storage.objects.create
  - storage.objects.delete
  - storage.objects.get
  - storage.objects.list
  - storage.objects.update
  
### 2- Create a Service Account and assign to it the created role 
Create a new Service Account, assign to it the custom role created in (1) and 
create a single JSON Service Account ```Key```. The JSON Key (file) shall be used 
by your applications in order to authenticate to GCP. You can create a Service Account 
with a single key, from [here](https://console.cloud.google.com/apis/credentials), 
alternatively [this interface](https://console.cloud.google.com/iam-admin/serviceaccounts) can be used. 
Make sure to download the ```json``` Service Account key file to your machine.


## Using the API

### 1- Export your key file
```
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json
```

### 2- Write your application 


#### import GCPStorageConfig
```python
from GCPStorageConfig.GCPStorageConfig import GCPStorageConfig
```

#### initialize GCPStorageConfig
```python
project_name = ''  # existing GCP project
bucket_name = ''  # existing GCP project Cloud Storage bucket
config_root = ''  # root directory for all configurations 

## __init__(project_name, bucket_name, root_config="config", date_format='%y.%m.%d %H:%M:%S')
gsc = GCPStorageConfig(project_name, bucket_name, config_root)
```

#### Creating a Configuration
placeholder to contain configuration variables
```python
## create_config(config_name, max_trials=3)
gsc.create_config("test")
```

#### Creating a Configuration Variable
Note: if the variable already exists, it will not be updated
```python
## create_variable(config_name, variable_name, variable_value, max_trials=3)
gsc.create_variable("test", "my_var", "my_value")
```

#### Get a Configuration Variable
```python
## get_variable(config_name, variable_name, max_trials=3)
print(gsc.get_variable("test", "my_var"))
```

#### Update a Configuration Variable
Note: if the variable does not exist, it will be created
```python
## update_variable(config_name, variable_name, variable_value, max_trials=3)
gsc.update_variable("test", "my_var", "my_value2")
print(gsc.get_variable("test", "my_var"))
```

#### Delete a Configuration Variable
```python
## delete_variable(config_name, variable_name, max_trials=3)
gsc.delete_variable("test", "my_var")
```

#### Dealing with dates
```python
import datetime

## create_date_variable(config_name, variable_name, date_value, max_trials=3)
gsc.create_date_variable("test", "my_date_var", datetime.datetime.now())

## update_date_variable(config_name, variable_name, date_value, max_trials=3)
gsc.update_date_variable("test", "my_date_var", datetime.datetime.now().replace(hour=10))

## get_date_variable(config_name, variable_name, max_trials=3)
print(gsc.get_date_variable("test", "my_date_var"))

gsc.delete_variable("test", "my_date_var")
```

#### Deleting a Configuration
```python
# removes the configuration and all its variables
## delete_config(config_name, max_trials=3)
gsc.delete_config("test")
```