import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gold-miner-ui",
    version="1.0",
    author="Wes Hardaker",
    author_email="opensource@hardakers.net",
    description="A UI (alpha) plugin that produces a live graph when using gold-mine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/isi-apropos/gold-mine-ui",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "gold-miner",
        "PyQt5",
        "pyqtgraph",
        "matplotlib",
        "multikeygraph",
        "jinja2",
        "roc_utils",
        "pyaml",
    ],
    entry_points={
        "console_scripts": [
            "gold-mine-auditor = apropos.goldmine.tools.auditor:main",
            "gold-mine-tande = apropos.goldmine.tools.tande:main",
            "gold-mine-fingerprint = apropos.goldmine.tools.fingerprinter:main",
        ]
    },
    python_requires=">=3.6",
    test_suite="nose.collector",
    tests_require=["nose"],
    package_data={
        "apropos.goldmine.reports": [
            "template.md",
            "summary-template.md",
            "template.html",
            "header.html",
            "navbar.html",
            "navbar-summary.html",
            "report.css",
            "hardhat.svg",
            "cancel.svg",
            "check.svg",
        ],
    },
)
