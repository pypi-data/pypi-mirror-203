import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="anoens",
    version="0.8",
    author="Simon Klüttermann",
    author_email="Simon.Kluettermann@gmx.de",
    description='Companion Module to my Paper "Evaluating and Comparing Heterogeneous Ensemble Methods for Unsupervised Anomaly Detection" (2023, IJCNN). Provides method to combine the scores of multiple anomaly detectors into an ensemble.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/psorus/anoens/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
    install_requires=[
        "numpy",
        "scipy",
        "sklearn"
      ],
    download_url='https://github.com/psorus/anoens/archive/0.8.tar.gz',
    
)  
