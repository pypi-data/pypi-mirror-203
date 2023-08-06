import setuptools
from pathlib import Path


long_desc = Path('README.md').read_text('utf-8')
setuptools.setup(
    name='helloworldplayerlili',
    version='0.0.3',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(
        exclude=['mocks', 'tests']
    )
)
