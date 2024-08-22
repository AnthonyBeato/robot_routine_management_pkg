from setuptools import find_packages, setup

package_name = 'robot_routine_management_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=[
        'setuptools',
        'rclpy',
        'geometry_msgs',
        'socket'
    ],
    zip_safe=True,
    maintainer='robot',
    maintainer_email='axba0001@ce.pucmm.edu.do',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'stop_robot_node = robot_routine_management_pkg.stop_robot:main',
        ],
    },
)
