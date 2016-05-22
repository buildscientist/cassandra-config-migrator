#!/usr/bin/env python

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


from cassandra import ConfigParser
from cassandra import ConfigWriter
from argparse import ArgumentParser
from argparse import FileType

def main():
    args = parse_arguments()
    configparser = ConfigParser(current_yaml=args.current_yaml_config,new_yaml=args.new_yaml_config)

    if (configparser.has_identical_config_keys()):
        raise RuntimeError("Configuration files have identical keys and values")

    if (configparser.has_identical_config_keys()):
        raise RuntimeError("Configures files have identical keys")

    configwriter = ConfigWriter(args.merged_yaml_config)
    merged_config = configparser.merge_config()
    configwriter.yaml_dump(merged_config)

def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("--current-yaml-config", dest="current_yaml_config", type=FileType(mode='rb'),required=True,help="The current YAML config file in use")
    parser.add_argument("--new-yaml-config",dest="new_yaml_config",type=FileType(mode='rb'),required=True,help="The new YAML config file to merge to")
    parser.add_argument("--merged-yaml-config",dest="merged_yaml_config",type=FileType(mode='wb'),required=True,help="The filename of the YAMl config containing the merged contents of old & new config")
    return parser.parse_args()



if __name__ == '__main__':
    main()