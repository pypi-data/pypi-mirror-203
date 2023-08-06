from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="roblox-dev",
    version="1.0.0",
    author="Danyamutit23",
    author_email="duaneskalanak@gmail.com",
    description="Модуль , позволяет управлять пользователем с помощью кода!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
 )

