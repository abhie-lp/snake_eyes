from setuptools import setup

setup(
    name="snake_eyes_cli",
    version="1.0",
    packages=["cli", "cli.commands"],
    include_package_data=True,
    install_requires=[
        "click"
    ],
    entry_points={
        "console_scripts": [
            "snake_eyes=cli.cli:cli",
        ]
    }
)
