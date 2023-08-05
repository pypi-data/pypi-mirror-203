from setuptools import setup

setup(
    name='sharewifi',
    version='1.0.5',
    author='Ankit Pandey',
    author_email='ashuankitpandey@gmail.com',
    description='A package to generate QR codes for WiFi networks',
    url='https://github.com/4NK1T/sharewifi',
    py_modules=['sharewifi'],
    install_requires=[
        'qrcode',
        'click',
        'cffi',
        'pycparser',
        'pynacl'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Utilities',
    ],
    entry_points={
        'console_scripts': [
            'sharewifi = sharewifi:generateQR',
        ],
    },
)
