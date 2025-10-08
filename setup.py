from setuptools import find_packages, setup

setup(
    name="ITSupportAssistant",
    version="0.0.1",
    author="baskaran",
    author_email="baskaran.marichetty76@gmail.com",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain ','langchain-openai','datasets','pypdf','python-dotenv','fastapi','deepeval']
)
