from setuptools import setup, find_packages

setup(
    name="trellis-standard-template",
    version="1.0.0",
    description="Standard Trellis template for AI-assisted development across all platforms",
    long_description=open("README.md").read(),
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
    install_requires=[],
    python_requires=">=3.9",
    license="MIT",
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
