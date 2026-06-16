from setuptools import setup, find_packages

setup(
    name="claude-skills",
    version="2.1.0",
    description="Claude Skills Library - 6900+ battle-tested skills across 34 domains",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ssrjkk/claude-skills",
    author="ssrjkk",
    license="MIT",
    packages=find_packages(),
    scripts=[
        "scripts/validate-skills.py",
        "scripts/validate-all.py",
        "scripts/deep-validate.py",
        "scripts/detect_anti_patterns.py",
        "scripts/generate-catalog.py",
        "scripts/generate_index.py",
        "scripts/list-skills.py",
        "scripts/test_examples.py",
    ],
    python_requires=">=3.9",
    install_requires=[
        "pyyaml>=6.0",
        "colorama>=0.4.6",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
    ],
)
