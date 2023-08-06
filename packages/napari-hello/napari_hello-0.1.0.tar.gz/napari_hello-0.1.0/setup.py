from setuptools import setup

setup(
    name='napari_hello',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='My napari plugin',
    packages=['napari_hello'],
    install_requires=[
        'napari',
    ],
    entry_points={
        'napari.plugin': [
            'napari_hello = napari_hello',
        ],
    },
)
