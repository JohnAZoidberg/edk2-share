from distutils.core import setup
from setuptools import find_packages

setup(
    name="UefiDriverWizard",

    version="0.11",

    packages=find_packages(),

    entry_points={
      'gui_scripts': [
        'UefiDriverWizard = UefiDriverWizard.launch:main'
      ]
    },

    package_data = {
      '' : ['Logo.ico'],
    },

    url="https://github.com/tianocore/edk2-share/DriverDeveloper",

    description="UEFI Driver Wizard for EDKII",

    long_description="The UEFI Driver Wizard is designed to aid in the development of UEFI Drivers using the EDK II open source project as a development environment.",

    install_requires=[
      "wxPython",
    ],
)
