from setuptools import setup, find_packages

setup(
    name='nex_ai',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your dependencies here, or keep them in requirements.txt
        # 'requests',
        # 'scikit-learn',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='AI for Decentralized Crypto Intelligence',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/nex-ai-project', # Replace with your project's URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
