from setuptools import setup, find_packages


VERSION = "1.0.1"
DESCRIPTION = 'JSON placeholder substitute tool'
LONG_DESCRIPTION = 'Substitute the placeholder "{{name}}" in JSON with the corresponding value from another JSON such as {"name": "Lorenzo"}. Project link: https://github.com/lorenzua02/json-replacer'

setup(
    # python_requires=">3.10",
    name="json-replacer",
    version=VERSION,
    author="Lorenzo Mogicato",
    author_email="<lorenzo.mogicato@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['json-replacer', 'json', 'json-token'],
    # classifiers=[
    #     "Development Status :: 1 - Planning",
    #     # "Intended Audience :: ILVOTeam",
    #     "Programming Language :: Python :: 3",
    #     "Operating System :: Unix",
    #     "Operating System :: MacOS :: MacOS X",
    #     "Operating System :: Microsoft :: Windows",
    # ]
)
