from setuptools import setup, find_packages

setup(
    name="neuroseg",
    version="0.1.0",
    packages=find_packages(),
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    description="A PyTorch-based framework for deep learning in neuroscience"
)
