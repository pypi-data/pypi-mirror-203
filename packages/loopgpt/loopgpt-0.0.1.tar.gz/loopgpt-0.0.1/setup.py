from setuptools import setup
import os

package_name = "loopgpt"


install_requires = open("requirements.txt", "r").readlines()

if __name__ == "__main__":
    setup(
        install_requires=install_requires,
        packages=[package_name],
        name=package_name,
        version="0.0.1",
        description="Modular Auto-GPT Framework",
        entry_points={"console_scripts": ["loopgpt = loopgpt.loops.cli:main"]},
    )
