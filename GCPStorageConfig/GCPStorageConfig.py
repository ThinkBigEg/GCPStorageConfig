from GCPStorageConfig.LoggingBase import LoggingBase
from google.cloud import storage
import datetime

"""
This is a util class that supports creating/updating/deleting 
Applications configuration variables, and it meant to be a replacement 
for GCPRuntimeConfig since its currently in beta.

This class is based on Google Cloud Storage
    - All Configurations have a base_directory which is stored in a GCP bucket 
    - A Configuration is simply a sub-directory in the base_directory
    - A Configuration variable is a file in the Configuration directory 
    - A Configuration variable Value is a value written in the configuration variable file
"""


class GCPStorageConfig(LoggingBase):
    """
    Requires setting the Environment Variable GOOGLE_APPLICATION_CREDENTIALS to the .json path of a
    service account that have access to the projects runtime config
    """

    def __init__(self, project_name, bucket_name, root_config="config", date_format='%y.%m.%d %H:%M:%S'):

        """

        :param project_name: the name of the GCP project
        :param bucket_name: the name of the GCP Cloud Storage bucket where all configuration will reside. this bucket
        need to pre-exist on GCP Cloud Storage
        :param root_config: the name of the base_directory to be created in the bucket, under which all configuration
        sub-directories will reside
        :param date_format: date format for storing date values
        """

        LoggingBase.__init__(self)
        self.project_name = project_name
        self.bucket_name = bucket_name
        self.root_config = root_config
        self.date_format = date_format

        self.storage_client = storage.client.Client()
        self.bucket = self.storage_client.get_bucket(self.bucket_name)

        self.logger.info("init GCPStorageConfig")

    def _create_blob_from_string(self, location, value, max_trials):
        blob = self.bucket.blob(location)
        for i in range(max_trials):
            try:
                if blob.exists(self.storage_client):
                    self.logger.info("blob {} already exists".format(location))
                    return True
                else:
                    self.logger.info("creating blob {}".format(location))
                    blob.upload_from_string(value)
                    return True
            except Exception as e:
                self.logger.error("error occurred {} retrying ".format(e))
        return False

    def _delete_blob(self, location, max_trials):

        config = self.bucket.blob(location)
        for i in range(max_trials):
            try:
                if config.exists(self.storage_client):
                    self.bucket.delete_blob(location, self.storage_client)
                    self.logger.info("blob {} is deleted".format(location))
                    return True
                else:
                    self.logger.info("blob {} does not exist".format(location))
                    return True
            except Exception as e:
                self.logger.error("error occurred {} retrying ".format(e))
        return False

    def create_config(self, config_name, max_trials=3):

        """
        only create config (folder in google bucket)
        :param config_name: str
        :param max_trials: int
        :return: bool
        """
        location = "{}/{}/".format(self.root_config, config_name)
        return self._create_blob_from_string(location, location, max_trials)

    def delete_config(self, config_name, max_trials=3):
        """

        :param config_name:
        :param max_trials:
        :return: bool
        """
        location = "{}/{}/".format(self.root_config, config_name)
        return self._delete_blob(location, max_trials)

    def create_variable(self, config_name, variable_name, variable_value, max_trials=3):
        """
        only creates variable file in GCP storage
        Note if variable exists: nothing will be done ... use update_variable to update an existing variable
        :param config_name: str
        :param variable_name: str
        :param variable_value: str
        :param max_trials: int
        :return: bool
        """
        location = "{}/{}/{}.txt".format(self.root_config, config_name, variable_name)
        return self._create_blob_from_string(location, str(variable_value), max_trials)

    def delete_variable(self, config_name, variable_name, max_trials=3):
        """
        delete variable (file in GCP storage)
        :param config_name: str
        :param variable_name: str
        :param max_trials: int
        :return: bool
        """
        location = "{}/{}/{}.txt".format(self.root_config, config_name, variable_name)
        return self._delete_blob(location, max_trials)

    def update_variable(self, config_name, variable_name, variable_value, max_trials=3):
        self.delete_variable(config_name, variable_name, max_trials=max_trials)
        self.create_variable(config_name, variable_name, variable_value, max_trials=max_trials)
        return True

    def get_variable(self, config_name, variable_name, max_trials=3):

        """
        :param config_name: str
        :param variable_name: str
        :param max_trials: int
        :return: str variable value
        """
        location = "{}/{}/{}.txt".format(self.root_config, config_name, variable_name)
        config_variable = self.bucket.blob(location)
        for i in range(max_trials):
            try:
                # if config variable exists
                if config_variable.exists(self.storage_client):
                    self.logger.info("reading variable {}/{}".format(config_name, variable_name))
                    # read config variable as string no need to download its file
                    variable_value = config_variable.download_as_string(self.storage_client)
                    # returning variable value
                    return variable_value.decode('utf-8')
                else:
                    # if configuration or variable does not exist: return None
                    return None
            except Exception as e:
                self.logger.error("error occurred while reading config variable: {}/{} error : {}"
                                  .format(config_name, config_variable, e))
        return None

    def create_date_variable(self, config_name, variable_name, date_value, max_trials=3):
        # parsing date object to a string
        date_str = date_value.strftime(self.date_format)
        return self.create_variable(config_name, variable_name, date_str, max_trials)

    def update_date_variable(self, config_name, variable_name, date_value, max_trials=3):
        # parsing date object to a string
        date_str = date_value.strftime(self.date_format)
        return self.update_variable(config_name, variable_name, date_str, max_trials)

    def get_date_variable(self, config_name, variable_name, max_trials=3):
        date_string = self.get_variable(config_name, variable_name, max_trials)
        if date_string:
            return datetime.datetime.strptime(date_string, self.date_format)
        else:
            return None

    def get_float_variable(self, config_name, variable_name, max_trials=3):
        float_string = self.get_variable(config_name, variable_name, max_trials)
        if float_string:
            return float(float_string)
        else:
            return None
