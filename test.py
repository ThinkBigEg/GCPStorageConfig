# import GCPStorageConfig
from GCPStorageConfig.GCPStorageConfig import GCPStorageConfig


# initialize GCPStorageConfig --
project_name = ''  # existing GCP project
bucket_name = ''  # existing GCP project Cloud Storage bucket
config_root = ''  # root directory for all configurations 

## __init__(project_name, bucket_name, root_config="config", date_format='%y.%m.%d %H:%M:%S')
gsc = GCPStorageConfig(project_name, bucket_name, config_root)

# Creating a Configuration --
# placeholder to contain configuration variables
## create_config(config_name, max_trials=3)
gsc.create_config("test")

# Creating a Configuration Variable --
# Note: if the variable already exists, it will not be updated
## create_variable(config_name, variable_name, variable_value, max_trials=3)
gsc.create_variable("test", "my_var", "my_value")

# Get a Configuration Variable --
## get_variable(config_name, variable_name, max_trials=3)
print(gsc.get_variable("test", "my_var"))

# Update a Configuration Variable --
# Note: if the variable does not exist, it will be created
## update_variable(config_name, variable_name, variable_value, max_trials=3)
gsc.update_variable("test", "my_var", "my_value2")
print(gsc.get_variable("test", "my_var"))

# Delete a Configuration Variable --
##  delete_variable(config_name, variable_name, max_trials=3)
gsc.delete_variable("test", "my_var")


# Dealing with dates --
import datetime

## create_date_variable(config_name, variable_name, date_value, max_trials=3)
gsc.create_date_variable("test", "my_date_var", datetime.datetime.now())

## update_date_variable(config_name, variable_name, date_value, max_trials=3)
gsc.update_date_variable("test", "my_date_var", datetime.datetime.now().replace(hour=10))

## get_date_variable(config_name, variable_name, max_trials=3)
print(gsc.get_date_variable("test", "my_date_var"))

gsc.delete_variable("test", "my_date_var")

# Deleting a Configuration -- 
# removes the configuration and all its variables
## delete_config(config_name, max_trials=3)
gsc.delete_config("test")
