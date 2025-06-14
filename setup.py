from setuptools import setup, find_packages

package_name = 'llm_agent_project'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(), # THIS searches from the current dir
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    include_package_data=True,
    package_data={
        'llm_agent_project': ['config/*.yaml'],
    },
    zip_safe=True,
    maintainer='suriya',
    maintainer_email='k.s.suriya0902@gmail.com',
    description='LLM-Powered Autonomous Agent for Robotics Simulation',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'run_agent = llm_agent_project.scripts.main:main'
        ],
    },
)

