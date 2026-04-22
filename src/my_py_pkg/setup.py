from setuptools import find_packages, setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='niko',
    maintainer_email='niko.korosec1@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'timer_node = my_py_pkg.timer_node:main',
            'publisher_node = my_py_pkg.publisher_node:main',
            'subscriber_node = my_py_pkg.subscriber_node:main',
            'publisher_int32 = my_py_pkg.publisher_int32:main',
            'subscriber_int32 = my_py_pkg.subscriber_int32:main',
            'add_two_ints_server = my_py_pkg.add_two_ints_server:main',
            'add_two_ints_client = my_py_pkg.add_two_ints_client:main',
        ],
    },
)
