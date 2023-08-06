import os
import platform
from setuptools import setup
from setuptools.command.build import build


class UnsupportedPython(RuntimeError):
    pass


class BuildCommand(build):
    def run(self):
        if os.getenv('ALLOW_UNSUPPORTED_PYTHON', None) is None:
            raise UnsupportedPython(
                'One or more packages do not support your version of Python ('
                + platform.python_version() + '). The installation will stop '
                'now. To force installation, set the ALLOW_UNSUPPORTED_PYTHON '
                'environment variable to any value. This may result in a '
                'broken package environment.')
        return super().run()


setup(cmdclass={'build': BuildCommand})
