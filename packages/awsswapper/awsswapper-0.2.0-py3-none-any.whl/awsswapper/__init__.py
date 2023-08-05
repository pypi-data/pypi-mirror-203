import configparser
import subprocess
from os.path import expanduser

import boto3

from cliar import Cliar


class Swapper(Cliar):
    """Change AWS accounts using AWS configure profiles"""

    def swap(self, profile: str, region: str = "") -> None:
        """Set this profile as the default profile in ~/.aws/credentials"""

        path = expanduser("~/.aws/credentials")

        config = configparser.ConfigParser()
        config.read(path)

        config["default"] = config[profile]

        with open(path, 'w') as configfile:
            config.write(configfile)

        if region:
            subprocess.check_call(["aws", "configure", "set", "region", region])

        sts = boto3.client("sts")
        print(sts.get_caller_identity())

    def list_profiles(self) -> None:
        """List available AWS profiles"""

        path = expanduser("~/.aws/credentials")

        config = configparser.ConfigParser()
        config.read(path)

        profiles = config.sections()
        for profile in profiles:
            if profile != "default":
                print(profile)


def main():
    Swapper().parse()
