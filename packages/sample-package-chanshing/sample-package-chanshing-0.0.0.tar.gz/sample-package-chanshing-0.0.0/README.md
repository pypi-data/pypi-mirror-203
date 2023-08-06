# Sample PyPI package + GitHub Actions + Versioneer

## How to use this template

1. Click on the *Use this template* button to get a copy of this repository.
1. Rename *src/sample_package* folder to your package name &mdash; *src/* is where your package must reside.
1. Go through each of the following files and rename all instances of *sample-package* or *sample_package* to your package name. Also update the package information such as author names, URLs, etc.
    1. setup.py
    1. pyproject.toml
    1. \_\_init\_\_.py
1. Install `versioneer` and `tomli`, and run `versioneer`:

    ```console
    $ pip install tomli
    $ pip install versioneer
    $ versioneer install
    ```
    Then commit the changes produced by `versioneer`. See [here](https://github.com/python-versioneer/python-versioneer/blob/master/INSTALL.md) to learn more.
1. Setup your PyPI credentials. See the section *Saving credentials on Github* of [this guide](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/).
