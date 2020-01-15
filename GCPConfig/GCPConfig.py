from GCPConfig.LoggingBase import LoggingBase


class GCPConfig(LoggingBase):
    def __init__(self):
        LoggingBase.__init__(self)

    def create_config(self, config_name, config_description="NA", max_trials=3):
        pass

    def delete_config(self, config_name, max_trials=3):
        pass

    def create_variable(self, config_name, variable_name, variable_value, max_trials=3):
        pass

    def create_date_variable(self, config_name, variable_name, date_value, max_trials=3):
        pass

    def update_date_variable(self, config_name, variable_name, date_value, max_trials=3):
        pass

    def delete_variable(self, config_name, variable_name, max_trials=3):
        pass

    def update_variable(self, config_name, variable_name, variable_value, max_trials=3):
        pass

    def get_variable_value(self, config_name, variable_name, max_trials=3):
        pass

    def get_date_variable(self, config_name, variable_name, max_trials=3):
        pass

    def get_float_variable(self, config_name, variable_name, max_trials=3):
        pass

