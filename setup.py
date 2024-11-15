from setuptools import setup, find_packages

setup(
    name="fig_code_test",  # Name of your package
    version="0.1.0",  # Initial version
    description="A package with code and figures for machine learning visualizations",
    author="Andre - based on  Jake Vanderplas",
    packages=find_packages(),  # Automatically finds the fig_code package
    install_requires=[  
    ],
    python_requires=">=3.10",  # Python version requirement if any
)