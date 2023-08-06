from setuptools import setup

# Version
version = None
with open("hierarchical_ensemble_classifier/__init__.py", "r") as f:
    for line in f.readlines():
        line = line.strip()
        if line.startswith("__version__"):
            version = line.split("=")[-1].strip().strip('"')
assert version is not None, "Check version in hierarchical_ensemble_classifier/__init__.py"

setup(
name='hierarchical_ensemble_classifier',
    version=version,
    description='Customizable Scikit-Learn compatible hierarchical ensemble of classifiers models',
    url='https://github.com/jolespin/hierarchical_ensemble_classifier',
    author='Josh L. Espinoza',
    author_email='jespinoz@jcvi.org',
    license='BSD-3',
    packages=["hierarchical_ensemble_classifier"],
    install_requires=[
        "networkx >= 2",
        "clairvoyance_feature_selection >= 2023.2.17",
        "soothsayer_utils"
        'pandas >= 1.2.4',
        "numpy >= 1.13",
        "xarray >= 0.10.3",
        "matplotlib >= 2",
        "seaborn >= 0.10.1",
        "scipy >= 1.0",
        "scikit-learn >= 1.0",
        "soothsayer_utils >= 2022.6.24",
        "tqdm >=4.19",
      ],
)
