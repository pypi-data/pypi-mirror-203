from setuptools import setup

__version__ = "2.0.0"

setup(
    name='arrendatools_plantillas',
    version=__version__,
    description='Módulo de Python que aplica plantillas usando jinja 2. Además incluye algunos filtros adicionales como el convertir un número a palabras.',
    url='https://github.com/hokus15/ArrendaToolsPlantillas',
    author='hokus15',
    author_email='hokus@hotmail.com',
    license='MIT',
    packages=['arrendatools_plantillas', 'arrendatools_plantillas.filters'],
    install_requires=['num2words==0.5.12', 'jinja2==3.1.2', 'python-dateutil==2.8.2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
