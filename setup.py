from setuptools import find_packages, setup


setup(

    name = "mcqgenerator",
    version='0.0.1',
    author="prakashmani awasthi",
    author_email="awasthiprakashmani7@gmail.com",
    install_requires=["openai", "langchain", "PyPDF2", "streamlit", "python-dotenv"],
    packages=find_packages(),

)