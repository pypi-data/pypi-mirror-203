import setuptools

with open("README.md", encoding="utf8") as readme:
    long_description = readme.read()

setuptools.setup(
    name="askpyro",
    packages=setuptools.find_packages(),
    version="1.69",
    license="MIT",
    description="Easy conversation handler for pyrogram mtproto library :)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Abishnoi69",
    author_email="asau2725@gmail.com",
    url="https://github.com/Abishnoi69/askpyro",
    keywords=["askpyr", "python-pakage", "ask-pyro", "Abishnoi"],
    project_urls={
        "Tracker": "https://github.com/Abishnoi69/askpyro/issues",
        "Community": "https://t.me/AbishnoiMF",
        "Source": "https://github.com/Abishnoi69/askpyro",
        "Documentation": "https://github.com/Abishnoi69/askpyro/wiki",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
