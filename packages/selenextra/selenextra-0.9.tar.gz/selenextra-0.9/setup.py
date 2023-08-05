from setuptools import setup, find_packages

setup(
    name='selenextra',
    version='0.9',
    description='Bringing additional features to Selenium',
    author='Tat Nguyen Van',
    author_email='nguyenvantat1182002@gmail.com',
    url='https://github.com/nguyenvantat1182002/SeleneXtra',
    packages=find_packages(),
    install_requires=[
        'scipy',
        'undetected_chromedriver',
        'selenium-wire'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
