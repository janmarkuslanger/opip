# opip
Use pip programmatically.

## Package

``` python
from opip import Package

my_package = Package('flask')

# install latest version
my_package.install()

# install specific version
my_package.install('1.0.0')

# get current version
my_package.get_version() # 1.0.0
```