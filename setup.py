from setuptools import setup, find_packages

with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name="hf_utils",
    version="0.0.1",
    description="huggingface_hub utils",
    author="ddPn08",
    packages=find_packages(),
    install_requires=install_requirements,
    entry_points={
        "console_scripts": [
            "hf_utils=hf_utils.core:main",
        ]
    },
)