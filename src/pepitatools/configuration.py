"""
Provide global configuration
"""
# Imports
# Standard Library Imports

# External Imports

# Local Imports

__all__ = ["Configuration"]

# Create a singleton metaclass
class Singleton(type):
    """Implementation of singleton as a metaclass"""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Override an inheriting class' call."""
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# Create a configuration Class
class Configuration(metaclass=Singleton):
    """
    Global Configuration Object
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.absolute_max_infection = 26249
        self.absolute_min_infection = 431
        self.absolute_max_ototox = 26249
        self.absolute_min_ototox = 431
        self.channel_main_ototox = 1
        self.channel_main_infection = 0
        self.channel_subtr_ototox = 0
        self.channel_subtr_infection = 1
        self.filename_replacement_delimiter = "|"
        self.filename_replacement_brightfield_infection = "CH2|CH4"
        self.filename_replacement_brightfield_ototox = "CH1|CH4"
        self.filename_replacement_mask_infection = "CH2|mask"
        self.filename_replacement_mask_ototox = "CH1|mask"
        self.filename_replacement_subtr_infection = "CH2|CH1"
        self.filename_replacement_subtr_ototox = "CH1|CH2"
        self.log_dir = "/path/to/log/dir"

    @property
    def absolute_max_infection(self):
        return self.absolute_max_infection

    @absolute_max_infection.setter
    def absolute_max_infection(self, value):
        self.absolute_max_infection = value

    @property
    def absolute_min_infection(self):
        return self.absolute_min_infection

    @absolute_min_infection.setter
    def absolute_min_infection(self, value):
        self.absolute_min_infection = value

    @property
    def absolute_max_ototox(self):
        return self.absolute_max_ototox

    @absolute_max_ototox.setter
    def absolute_max_ototox(self, value):
        self.absolute_max_ototox = value

    @property
    def absolute_min_ototox(self):
        return self.absolute_min_ototox

    @absolute_min_ototox.setter
    def absolute_min_ototox(self, value):
        self.absolute_min_ototox = value

    @property
    def channel_main_ototox(self):
        return self.channel_main_ototox

    @channel_main_ototox.setter
    def channel_main_ototox(self, value):
        self.channel_main_ototox = value

    @property
    def channel_main_infection(self):
        return self.channel_main_infection

    @channel_main_infection.setter
    def channel_main_infection(self, value):
        self.channel_main_infection = value

    @property
    def channel_subtr_ototox(self):
        return self.channel_subtr_ototox

    @channel_subtr_ototox.setter
    def channel_subtr_ototox(self, value):
        self.channel_subtr_ototox = value

    @property
    def channel_subtr_infection(self):
        return self.channel_subtr_infection

    @channel_subtr_infection.setter
    def channel_subtr_infection(self, value):
        self.channel_subtr_infection = value

    @property
    def filename_replacement_delimiter(self):
        return self.filename_replacement_delimiter

    @filename_replacement_delimiter.setter
    def filename_replacement_delimiter(self, value):
        self.filename_replacement_delimiter = value

    @property
    def filename_replacement_brightfield_infection(self):
        return self.filename_replacement_brightfield_infection

    @filename_replacement_brightfield_infection.setter
    def filename_replacement_brightfield_infection(self, value):
        self.filename_replacement_brightfield_infection = value

    @property
    def filename_replacement_brightfield_ototox(self):
        return self.filename_replacement_brightfield_ototox

    @filename_replacement_brightfield_ototox.setter
    def filename_replacement_brightfield_ototox(self, value):
        self.filename_replacement_brightfield_ototox = value

    @property
    def filename_replacement_mask_infection(self):
        return self.filename_replacement_mask_infection

    @filename_replacement_mask_infection.setter
    def filename_replacement_mask_infection(self, value):
        self.filename_replacement_mask_infection = value

    @property
    def filename_replacement_mask_ototox(self):
        return self.filename_replacement_mask_ototox

    @filename_replacement_mask_ototox.setter
    def filename_replacement_mask_ototox(self, value):
        self.filename_replacement_mask_ototox = value

    @property
    def filename_replacement_subtr_infection(self):
        return self.filename_replacement_subtr_infection

    @filename_replacement_subtr_infection.setter
    def filename_replacement_subtr_infection(self, value):
        self.filename_replacement_subtr_infection = value

    @property
    def filename_replacement_subtr_ototox(self):
        return self.filename_replacement_subtr_ototox

    @filename_replacement_subtr_ototox.setter
    def filename_replacement_subtr_ototox(self, value):
        self.filename_replacement_subtr_ototox = value

    @property
    def log_dir(self):
        return self.log_dir

    @log_dir.setter
    def log_dir(self, value):
        self.log_dir = value
