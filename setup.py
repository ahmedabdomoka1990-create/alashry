from setuptools import setup, find_packages

setup(
    name='Alashry',
    version='0.1.0',
    author='Your Name',  # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    description='A short description of the Alashry application',
    packages=find_packages(),
    install_requires=[
        # List your project's dependencies here.
        # Example:
        # 'numpy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)