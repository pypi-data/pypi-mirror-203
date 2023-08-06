from setuptools import find_packages
from setuptools import setup

from tools import common

common.init()
print(f'==== {"version": <11}: v{common.cmn_version}')

# @formatter:off
setup(
    description='Falcon Logger - twice as fast as standard python logger',
    keywords=['statistics', 'utility'],
    install_requires=[
        'pytest-ver',
    ],
    classifiers=[
        # Choose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3.9',
        common.cmn_classifier_license,
    ],

    # common attributes from here on
    name=common.cmn_mod_name,
    include_package_data=True,
    packages=find_packages(include=f'{common.cmn_mod_dir_name}*', ),
    version=common.cmn_version,
    license=common.cmn_license,
    long_description=common.cmn_long_desc,
    long_description_content_type=common.cmn_long_desc_type,
    author=common.cmn_author,
    author_email=common.cmn_email,
    url=common.cmn_homepage_url,
    download_url=common.cmn_download_url,
)
# @formatter:on

print('OK   GenBuildInfo completed successfully')
