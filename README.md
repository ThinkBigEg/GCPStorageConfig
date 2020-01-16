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
- change branches for python 3.6 ```git checkout dev``` 
- change branches for python 2.7 ``` git checkout dev_python_2_7```

- installing library 
```
pip install /path/to/GCPStorageConfig/
```
## using api 
###1- Create a Role with sufficient privileges at least 
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

### 3- export your key 
```
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json
```
### 4 package specification
#### 1- name : GCPConfig
- ##### PACKAGE CONTENTS: 
    - ##### GCPConfig
    - ##### GCPStorageConfig
    - ##### LoggingBase
 ### 5- classes specification
1. ### name: LoggingBase
    - #### Description: Any application that runs through the system extends LoggingBase class
    - #### methods 
        -  #### def __init__(self):

2. ### name: GCPConfig
    - #### Description: abstract Class config base class 
    - ### methods 
        - ##### def __init__(self):
        - ##### def create_config(self, config_name, config_description="NA", max_trials=3):
            - params : 
                - config_name :   str configration name 
                - config_description : str configration 
                - max_trials: int number of trails to create config 
            - return : boolean (cteated - faild)
        - ##### def delete_config(self, config_name, max_trials=3):
            - params : 
                - config_name :   str configration name 
                - max_trials: int number of trails to create config 
            - return boolean (deleted - faild)
        - ##### def create_variable(self, config_name, variable_name, variable_value, max_trials=3):
            - params : 
                - config_name :   str configration name 
                - variable_name : str variable name  
                - variable_value : str value
                - max_trials: int number of trails to create config 
            - return : boolean (cteated - faild)
        - ##### def create_date_variable(self, config_name, variable_name, date_value, max_trials=3):
            - params : 
                - config_name :   str configration name 
                - variable_name : str variable name  
                - variable_value : date value
                - max_trials: int number of trails to create config 
            - return : boolean (cteated - faild)
        - ##### def update_date_variable(self, config_name, variable_name, date_value, max_trials=3):
            - params : 
                - config_name :   str configration name 
                - variable_name : datetime variable name  
                - variable_value : date value
                - max_trials: int number of trails to create config 
            - return : boolean (updated - faild)
        - ##### def delete_variable(self, config_name, variable_name, max_trials=3):
            - params : 
                - config_name :   str configration name 
                - variable_name : str variable name  
                - max_trials: int number of trails to create config 
            - return : boolean (deleted - faild)
        - ##### def update_variable(self, config_name, variable_name, variable_value, max_trials=3):
            - params : 
                - config_name :   str configration name 
                - variable_name : str variable name  
                - variable_value : str value
                - max_trials: int number of trails to create config 
            - return : boolean (updated - faild)
        - ##### def get_variable_value(self, config_name, variable_name, max_trials=3):
            - params : 
                - config_name :   str configration name 
                - variable_name : str variable name  
                - max_trials: int number of trails to create config 
            - return : str value
        - ##### def get_date_variable(self, config_name, variable_name, max_trials=3):
            - params : 
                - config_name :   str configration name 
                - variable_name : str variable name  
                - max_trials: int number of trails to create config 
            - return : datetime value
        - ##### def get_float_variable(self, config_name, variable_name, max_trials=3):
            - params : 
                - config_name :   str configuration name 
                - variable_name : str variable name  
                - max_trials: int number of trails to create config 
            - return : datetime value
3. ### name : GCPStorageConfig
    - extends: GCPConfig
    - description : extends GCPConfig functionality by using GCP storage as its storage space 
