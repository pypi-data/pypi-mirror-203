import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spiderYa",
    version="0.0.5",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    install_requires=[
        'anndata>=0.8.0',
        'cellrank>=1.5.2',
        'fa2>=0.3.5',
        'gseapy>=1.0.3',
        'h5py>=3.7.0',
        'igraph>=0.9.11',
        'leidenalg>=0.8.10',
        'louvain>=0.7.1',
        'matplotlib>=3.6.3',
        'matplotlib-venn>=0.11.7',
        'networkx>=2.8.8',
        'numba>=0.56.4',
        'numpy>=1.23.5',
        'pandas>=1.5.2',
        'plotly>=5.10.0',
        'pygco>=0.0.16',
        'scanpy>=1.9.1',
        'scgco>=1.1.2',
        'scikit-learn>=1.2.0',
        'scipy>=1.10.0',
        'scvelo>=0.2.5',
        'seaborn>=0.12.2',
        'sklearn>=0.0',
        'somde>=0.1.8',
        'somoclu>=1.7.5.1',
        'spaotsc>=0.2',
        'spatialde>=1.1.3',
        'stlearn>=0.4.8',
        'umap-learn>=0.5.3'
    ],
)