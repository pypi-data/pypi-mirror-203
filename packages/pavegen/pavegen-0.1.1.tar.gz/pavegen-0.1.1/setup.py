from setuptools import setup, find_packages

setup(
    name='pavegen',
    version='0.1.1',
    packages=find_packages(),
    data_files=[('pavegen', ['model.pth'])],
    install_requires=[
        'numpy',
        'torch',
        'torchvision',
        'matplotlib',
        'Pillow',
    ],
    author='Armstrong Aboah',
    author_email='aboah1994@gmail.com',
    description='A short description of your package',
    # slong_description=open('README.md').read(),
    # long_description_content_type='text/markdown',
    # url='https://github.com/your-username/my_package',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)





