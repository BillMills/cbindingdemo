import setuptools, subprocess
from distutils.command.install import install as _install

class install(_install):
    def run(self):
        subprocess.call(['make', 'clean', '-C', 'cqc'])
        subprocess.call(['make', '-C', 'cqc'])
        _install.run(self)

setuptools.setup(
    name="cqc",
    version="0.0.18",
    packages=setuptools.find_packages(),
    package_data={'cqc': ['cqc/cqc.so']},
    include_package_data=True,
    cmdclass={'install': install},
)
