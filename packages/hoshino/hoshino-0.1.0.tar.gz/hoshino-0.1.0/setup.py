from setuptools import setup, find_packages

setup(
    name='hoshino',
    version='0.1.0',
    description='A personal Python app',
    author='sitomao',
    author_email='you@example.com',
    packages=find_packages(),
    install_requires=[
        'requests>=2.26.0'
    ],
    tests_require=[
        'pytest>=6.2.5',
        'pytest-cov>=3.0.0'
    ],
    entry_points={
        'console_scripts': [
            'hoshino=hoshino.main:main'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9'
    ],
)
