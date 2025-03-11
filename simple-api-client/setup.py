from setuptools import setup, find_packages

setup(
    name="simple-api-client",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Игорь Акимов,Егор Кузнецов",
    description="Простой клиент для работы с REST API",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/your_username/simple-api-client",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
