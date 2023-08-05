from setuptools import setup

setup(
    name="AI-Summarizer",
    version="1.0.1",
    description="""AI Summarizer is a Python package that uses OpenAI's GPT-3.5 to summarize any given text.
    You can input some text describing what kind of information you are interested in. 
    When the text is too long it splits it logically into different sections, to make it simpler to summarise""",
    url="https://github.com/pietrosperoni/ai-summarizer",
    author="Pietro Speroni di Fenizio",
    author_email="aisummarizer@piespe.net",
    packages=["ai_summarizer"],
    install_requires=[
        "python-dotenv",
        "html2text",
        "openai",
        "tiktoken"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: Markup",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)