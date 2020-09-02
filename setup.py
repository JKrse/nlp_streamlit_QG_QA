
from setuptools import setup, find_packages

setup(
    name="qa_qg_streamlit",
    version="1.0.0",
    author="Johannes Kruse",
    description="Question Answering Question Generation streamlit app",
    url="https://github.com/JKrse/nlp_streamlit_QG_QA",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "pandas",
        # Stramlit app
        "streamlit",
        # Download git repository
        "gitpython",
        # Preposseing
        "nltk",
        # for allennlp models
        "allennlp==1.0.0",
        # for allennlp models
        "allennlp-models==1.0.0",
        # for Transformers
        "transformers==3.0.0",
    ],
    python_requires=">=3.6.0"
)

import git
import os

if not os.path.exists(f"{os.getcwd()}/question_generation/"):
    git.Git(os.getcwd()).clone("https://github.com/patil-suraj/question_generation.git")




