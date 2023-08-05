from setuptools import setup, find_packages

setup(
    name='sharewifi',
    version='1.0.1',
    description='Generate QR codes for sharing WiFi network credentials',
    url='https://github.com/4NK1T/sharewifi',
    author='Ankit Pandey',
    author_email='ashuankitpandey@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'sharewifi=sharewifi.sharewifi:main'
        ]
    },
    install_requires=[
        'qrcode',
        'click',
        'cffi',
        'pycparser',
        'pynacl'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities'
    ],
)
