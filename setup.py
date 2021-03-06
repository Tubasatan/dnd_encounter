import setuptools

# to update the version change the verison number in this file
# then run the following
# git tag <version number>
# git push --tags origin master


setuptools.setup(name='dnd_encounter',
                 version='0.4.2',
                 descripion='Tool to fill out a pdf with monster data',
                 url='https://github.com/Tubasatan/dnd_encounter',
                 author='Sebastian Antonsen',
                 author_email='sebastian.antonsen@gmail.com',
                 license='GPL',
                 packages=setuptools.find_packages(),
                 scripts=['bin/dnd-encounter'],
                 install_requires=['xmltodict', 'fdfgen'],
                 zip_safe=False,
                 include_package_data=True)
