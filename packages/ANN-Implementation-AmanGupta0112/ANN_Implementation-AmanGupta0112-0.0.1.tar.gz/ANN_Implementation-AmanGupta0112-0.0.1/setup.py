import setuptools

# read the contents of README.md file
with open("README.md","r", encoding='utf-8') as f:
    long_description = f.read()

    
PROJECT_NAME = "ANN_Implementation"
USER_NAME = "AmanGupta0112"
setuptools.setup(
    name=f'{PROJECT_NAME}-{USER_NAME}',
    version='0.0.1',
    description='Simple ANN implementation using tensflow Dataset',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/{USER_NAME}/{PROJECT_NAME}',
    author=f'{USER_NAME}',
    author_email='guptaamanvns0542@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='Perceptron, OneNeuron',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    install_requires=[
        'tensorflow',
        'seaborn',
        'numpy',
        'pandas',
        'joblib',
        'matplotlib',
    ],
    python_requires='>=3.6',
)

# from setuptools import setup

# with open("README.md", "r", encoding="utf-8") as f:
#     long_description = f.read()

# setup(
#     name="src",
#     version="0.0.2",
#     author="Aman",
#     description="A small package for ANN Implementation",
#     long_description=long_description,
#     long_description_content_type="text/markdown",
#     url="https://github.com/c17hawke/ANN-implementation-DLCVNLP-demo",
#     author_email='guptaamanvns0542@gmail.com',
#     packages=["src"],
#     python_requires=">=3.7",
#     install_requires=[
#         "tensorflow",
#         "matplotlib",
#         "seaborn",
#         "numpy",
#         "pandas"
#     ]
# )
