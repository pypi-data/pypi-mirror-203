from setuptools import setup

setup(
    name='rrb_package',
    version='0.1.1',
    author='Rahul Bhoyar',
    author_email='rahulbhoyaroffice@gmail.com',
    description='My first pip installabe package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rahulbhoyar1995/rrb_package',
    packages=['rrb_package'],
    install_requires=[
        # Dependencies go here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
