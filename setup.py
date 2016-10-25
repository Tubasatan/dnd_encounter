import setuptools


setuptools.setup(name='dnd_encounter',
                 version='0.3.1',
                 descripion='Tool to fill out a pdf with monster data',
                 url='https://github.com/Tubasatan/dnd_encounter',
                 author='Sebastian Antonsen',
                 author_email='sebastian.antonsen@gmail.com',
                 license='GPL',
                 packages=setuptools.find_packages(),
                 scripts=['bin/dnd-encounter'],
                 zip_safe=False,
                 include_package_data=True)
