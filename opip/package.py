from typing import Optional
import subprocess
import os
from opip.constants import PIP_EXECUTE_ITEMS


FNULL = open(os.devnull, 'w')


class Package:
    __slots__ = ('name',)

    def __init__(self,name :str) -> None:
        self.name = name

    def install(self, version: Optional[str] = None) -> bool:
        pip_package = self.name + ('' if not version else '=={}'.format(version))

        try:
            subprocess.check_call(
                [*PIP_EXECUTE_ITEMS, 'install', pip_package],
                stdout=FNULL,
                stderr=subprocess.STDOUT
            )
            return True
        except subprocess.CalledProcessError:
            return False

    def get_version(self) -> Optional[str]:
        process = subprocess.Popen([*Package.PIP_EXECUTE_ITEMS, 'freeze'], stdout=subprocess.PIPE)
        packages = process.communicate()[0].decode('utf-8').split('\n')
        for package in packages:
            if package == '':
                continue

            (name, version) = package.split('==')

            if name == self.name:
                return version

    


