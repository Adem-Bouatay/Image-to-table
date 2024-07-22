from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = 'Extracting timetable from image and converting it to JSON format.'
LONG_DESCRIPTION = 'A package that allows to extract timetables from images and converting them to JSON format using Gemini MM-LLM.'

# Setting up
setup(
    name="image-to-table",
    version=VERSION,
    author="Adem Bouatay",
    author_email="<adem.bouatay@eniso.u-sousse.tn>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['llama-index', 'llama-index-multi-modal-llms-gemini', 'pillow', 'tabulate'],
    keywords=['python', 'image', 'json', 'MM LLM', 'AI'],
    classifiers=[
        "Development Status :: Released",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
