from setuptools import setup

setup(
    name="hf_utils",
    version="0.0.1",
    description="huggingface_hub utils",
    author="ddPn08",
    packages=["hf_utils", "hf_utils.commands"],
    install_requires=[
        "huggingface_hub",
        "fire",
    ],
    entry_points={
        "console_scripts": [
            "hf_utils=hf_utils.core:main",
        ]
    },
)
