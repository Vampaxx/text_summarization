import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()




__version__ = "0.0.0"

REPO_NAME = "text_summarization"
AUTHOR_USER_NAME = "Vampaxx"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "arjunappu1001@gmail.com"


setuptools.setup(
    name                    = SRC_REPO,
    version                 = __version__,
    author                  = AUTHOR_USER_NAME,
    author_email            = AUTHOR_EMAIL,
    description             = "Text summarization is a crucial natural language processing task that involves condensing a given piece of text while retaining its essential information",
    long_description        = long_description,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"))


