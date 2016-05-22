## Copyright 2014 Youssuf ElKalay
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from yaml import load

"""
A class that takes two YAML files and performs a set based diff and merge.
"""
class ConfigParser(object):
    def __init__(self,current_yaml,new_yaml):
        self.current_yaml_file = current_yaml
        self.new_yaml_file = new_yaml
        self.current_config = None
        self.new_config = None
        self.load_config()

    def load_config(self):
        self.current_config = load(self.current_yaml_file)
        self.new_config = load(self.new_yaml_file)

    def has_identical_config(self):
        """
        A symmetric difference of 0 between old and new config would mean both config files contain identical
        key value pairs
        """
        old_set = set(self.current_config)
        new_set = set(self.new_config)

        symmetric_difference = old_set ^ new_set
        if (len(symmetric_difference) > 0):
            return False

        return True

    def has_identical_config_keys(self):
        """
        A symmetric difference of 0 between old and new config keys would mean both config files contain identical keys.
        This could mean both config files are from identical versions of Cassandra
        """
        old_set_keys = set(self.current_config.keys())
        new_set_keys = set(self.new_config.keys())

        symmetric_difference = old_set_keys ^ new_set_keys
        if(len(symmetric_difference) > 0):
            return False

        return True

    def get_identical_config_keys(self):
        """
        The intersection of both sets
        """
        old_set_keys = set(self.current_config.keys())
        new_set_keys = set(self.new_config.keys())

        return new_set_keys & old_set_keys


    def get_new_config_keys(self):
        """
        new_config_set - old_config_set
        """
        old_set_keys = set(self.current_config.keys())
        new_set_keys = set(self.new_config.keys())

        return new_set_keys - old_set_keys


    def get_old_config_keys(self):
        """
        old_config_set - new_config_set
        These config keys are not available in the new versions config

        """

        old_set_keys = set(self.current_config.keys())
        new_set_keys = set(self.new_config.keys())

        return old_set_keys - new_set_keys

    def merge_config(self):
        """
        The union between the new config set and the intersection of both new and old sets
        """
        current_config = {}
        new_config = {}


        for key in self.get_identical_config_keys():
            current_config[key] = self.current_config.get(key)


        for key in self.get_new_config_keys():
            new_config[key] = self.new_config.get(key)


        return dict(current_config.items() + new_config.items())