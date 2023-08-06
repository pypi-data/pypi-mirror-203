from setuptools import setup

setup(
	name = "mymlcustomtools",
	version = "0.0.1",
	description = """
	A package with frequently and useful functions for machine learning
	""",
	author = "Gustavo Exel",
	author_email = "gustavoexelgpe@gmail.com",
	url = "https://pypi.org/project/mymlcustomtools/",
	packages = ["mymlcustomtools"],
	zip_safe = False,
)

# py setup.py sdist 		# compiles/builds the package
# pip install .				# locally installs the package for testing
# twine upload dist/* 		# uploads package to PyPI