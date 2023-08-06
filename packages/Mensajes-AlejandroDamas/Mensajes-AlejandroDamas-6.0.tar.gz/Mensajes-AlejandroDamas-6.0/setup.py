from setuptools import setup, find_packages

setup(
    name='Mensajes-AlejandroDamas',
    version='6.0',
    description='Un paquete para saludar y despedir',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Alejandro Damas Pablos',
    author_email='hola@damas.py',
    url='https://www.damas.py',
    license_files=['LICENSE'],
    packages=find_packages(),
    scripts=[],
    test_suits='tests',
    install_requires=[paquete.strip()
                      for paquete in open("requirements.txt").readlines()],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Utilities'
    ]
)
