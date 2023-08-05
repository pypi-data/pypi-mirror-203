import setuptools as st

st.setup(
    name                          = "UnMythwareTool",
    version                       = "0.0.1",
    description                   = "A Kill Mythware Tool.",
    long_description              = open("README.md", 'r', encoding="utf-8").read(),
    long_description_content_type = "text/markdown",
    author                        = "SmallWaterSnake",
    author_email                  = "hzk201312@163.com",
    scripts                       = ["src\\UMT\\__init__.py", "src\\UMT\\_umt.py"],
    requires                      = [
            "psutil",
            "setuptools",
    ],
    packages                      = st.find_packages(),
    classifiers                   = [
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
    ]
)
