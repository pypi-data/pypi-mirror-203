from setuptools import setup, find_packages

VERSION = "0.0.7"

setup(
    name="megabots",
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        "langchain",
        "tiktoken",
        "unstructured",
        "fastapi",
        "faiss-cpu",
        "pdfminer.six",
    ],
    author="Megaklis Vasilakis",
    author_email="megaklis.vasilakis@gmail.com",
    description="Create a question answering over docs bot with one line of code.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/momegas/megabots",
    classifiers=[
        # Choose appropriate classifiers from
        # https://pypi.org/classifiers/
        "Development Status :: 4 - Beta"
    ],
)
