from setuptools import setup, find_packages

with open("README.rst", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="openai-chat-parser",
    version="0.1.0",
    description="Download, extract, and parse OpenAI chat conversation archives",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/photon-platform/openai_chat_parser",
    packages=find_packages(),
    install_requires=["python-slugify"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={
        "console_scripts": [
            "openai-chat-parser=openai_chat_parser.__main__:main",
        ],
    },
)

