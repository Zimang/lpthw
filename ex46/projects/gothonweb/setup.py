try:
    from setuptools import setuptools
except ImportError:
    from distutils.core import setuptools

config={
    'description': 'My Project',
    'author': 'Zimang',
    'url': 'https://github.com/Zimang/lpthw/tree/master/ex46/projects/skeleton',
    'download_url': 'https://github.com/Zimang/lpthw/tree/master/ex46/projects/skeleton',
    'author_email': '3047247998@qq.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'gothonweb'
}
setup(**config)
