import os
from setuptools import setup, find_packages

# 读取 README.md 并确保正确的编码
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="trellis-standard-template",
    version="1.0.0",
    description="Standard Trellis template for AI-assisted development across all platforms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="whoami",
    author_email="whoami@example.com",
    url="https://github.com/adminlove520/standard-trellis-template",
    project_urls={
        "Repository": "https://github.com/adminlove520/standard-trellis-template",
        "Issues": "https://github.com/adminlove520/standard-trellis-template/issues",
    },
    packages=find_packages(),
    package_data={
        "trellis_standard": ["template/*", "template/spec/*"],
    },
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.9",
    keywords=[
        "trellis",
        "ai",
        "claude",
        "openclaw",
        "hermes",
        "cursor",
        "template",
        "coding-standard"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development",
        "Topic :: Software Development :: Code Generators",
    ],
    entry_points={
        "console_scripts": [
            "trellis-init-standard=trellis_standard.cli:main",
        ],
    },
)
