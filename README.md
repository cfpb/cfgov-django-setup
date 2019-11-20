# cfgov-setup

This package provides a central home for our logic for building front-end assets as part of the Python build process (for example, when generating a [wheel](https://pypi.python.org/pypi/wheel)), which has until now simply been duplicated everywhere. Open source examples:

https://github.com/cfpb/complaint/blob/v1.2.3/setup.py#L20
https://github.com/cfpb/retirement/blob/0.5.0/setup.py#L20

We've also added a crucial check that allows front-end build failures to propogate up to Python. They previously ignored the result of `subprocess.call` and happily continued even if the frontend build failed.


## Dependencies

- Python 2.7

## Installation

Edit your package's 'setup.py' to require this module at build-time (`setup_requires=['cfgov-setup']`), and set the 'do_frontend_build' keyword in the setup arguments. [This pull request](https://github.com/cfpb/complaint/pull/10) demonstrates the kind of changes to make.

## Testing

To lint and run the unit tests you will need to:

1. Install Tox in a virtualenv or your local Python environment: `pip install tox`
2. Run tox: `tox`

## Open source licensing info
1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)
3. [CFPB Source Code Policy](https://github.com/cfpb/source-code-policy/)
