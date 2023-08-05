import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="qolpy",
    version="0.1.1",
    description="A suite of random but useful functions that are aimed at giving you 'piece of cake' level comfortability",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lewisjr/qolpy.git",
    project_urls={
        "Bug Tracker": "https://github.com/lewisjr/qolpy/issues",
    },
    author = "Cerebrus Inc | Lewis Mosho Jr",
    author_email = "lewis@cerebrus.dev",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Typing :: Typed"
    ],
    packages=["qolpy", "qolpy.colour", "qolpy.date", "qolpy.number", "qolpy.string"],
    include_package_data=True,
    install_requires=["typing"],
    package_dir={"": "src"},
    python_requires=">=3.0",
)