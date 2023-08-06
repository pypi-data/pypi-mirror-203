# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['usody_sanitize', 'usody_sanitize.schemas']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0']

entry_points = \
{'console_scripts': ['sanitize = usody_sanitize.cmd_client:run_cmd']}

setup_kwargs = {
    'name': 'usody-sanitize',
    'version': '0.1.0b6',
    'description': 'A tool to securely erase/wipe data on disks HDD and SSD with a proper sanitization process.',
    'long_description': '# Usody Sanitize\n\n> Under development.\n\nThis tool securely erases disks by performing a certificate-based validation of\nthe wipe process. It ensures that the data on the disk is completely and \nirrecoverably erased, protecting sensitive information from being recovered. \nThe tool uses industry-standard wiping methods to securely erase the data on \nthe disk, making it impossible to recover. The tool also generates a \ncertificate of sanitize process that can be used to verify the authenticity of the wipe\nprocess. This tool is perfect for businesses and individuals who need to\nsecurely and permanently remove sensitive data from their disks.\n\n## Todo\n\n- Test the command with more errors on erasures.\n- Better command output handler.\n- Improve the export of the erasures into json files.\n\n## Installation\n\nInstall the package from the official PyPi repository:\n\n<div class="termy">\n\n```console\n$ pip install usody_sanitize\n\n---> 100%\n```\n\n</div>\n\n## Usage\n\nYou can use this module via terminal or calling it from an external code.\n\n### Terminal client\n\nErase a single disk using the default method: \n\n```bash\nusody_sanitize -v /dev/sda  \n```\n\n\n## Issues\n\n### hdparm Error: The running kernel lacks CONFIG_IDE_TASK_IOCTL support for this device\n\nWhen trying to run the command \n`hdparm --user-master u --security-erase UsodyPassword /dev/sdX`, an error\nmessage was encountered:\n\n    The running kernel lacks CONFIG_IDE_TASK_IOCTL support for this device.\n\nA return code of 22 from the `hdparm` command generally indicates \nthat the command completed successfully, but some features may not have been \nfully supported on the device being used. This can happen if the device does \nnot fully comply with the ATA standard, or if the device is a SCSI drive rather\nthan an ATA drive. It may also indicate that the specific options used in the\ncommand are not supported on the device.\n\nThis error message is indicating that the kernel (the core part of the \noperating system) does not have support for the IDE task IOCTL feature, which\nis required to run the `hdparm` command.\n\nThe `hdparm` command is used to configure and retrieve information about ATA \nhard drives, and the specific option used in the command (`--user-master u \n--security-erase UsodyPassword`) is used to erase the security settings on the\ndrive. Because the kernel does not have the necessary support, the command\ncannot be executed.\n\nTo enable the CONFIG_IDE_TASK_IOCTL support in the kernel, it must be \nrecompiled with this option enabled. The process for doing this will depend on\nthe specific distribution of Linux being used, but generally the steps are:\n\n1. Download the source code for the current kernel version.\n2. Extract the source code and navigate to the root directory.\n3. Run `make menuconfig` or `make xconfig` to open the kernel configuration\nmenu.\n4. Search for the option `CONFIG_IDE_TASK_IOCTL` and enable it.\n5. Save the configuration and exit the menu.\n6. Run make to compile the kernel with the new configuration.\n7. Install the new kernel, and reboot the system to use it.\n\nIt\'s important to note that recompiling the kernel is a complex and delicate\nprocess and it\'s recommended to have experience with Linux kernel compilation.\n\n#### What is `CONFIG_IDE_TASK_IOCTL`\n\nIs a kernel configuration option that enables support for the IDE task file\nregister IOCTLs in the Linux kernel. The IDE task file register is a set of\nregisters on an IDE (Integrated Drive Electronics) hard drive that are used to\ncontrol the drive\'s operations.\n\nWhen this feature is enabled, the kernel provides an interface for user-space \nprograms, such as `hdparm`, to access these registers and perform various \noperations on the hard drive, such as reading and setting parameters, \nperforming security commands, and reading SMART data.\n\nIf this feature is not enabled, the `hdparm` command will not be able to access \nthe task file register and will not be able to perform certain operations on \nthe drive, such as security commands or SMART data.\n\nIt\'s worth noting that this feature is not only specific to `hdparm`, but also \nother utilities that can access the task file register, such as smartctl and \nhdparam will also be affected by the state of this feature.\n\nIt\'s also worth noting that this feature is specific to ATA drives and will not\nhave any effect on SCSI drives.\n',
    'author': 'blkpws',
    'author_email': 'me@blkpws.xyz',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/usody/sanitize',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
