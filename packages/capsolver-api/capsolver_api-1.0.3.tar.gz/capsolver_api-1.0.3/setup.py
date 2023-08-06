from setuptools import setup, find_packages

print(find_packages())

classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]

setup(
    name='capsolver_api',
    version='1.0.3',
    author='seadhy',
    author_email='seadhy@protonmail.com',
    description='capsolver python libary',
    long_description='i will write',
    long_description_content_type="text/markdown",
    url="https://github.com/seadhy/capsolver-api",
    project_urls={
        "Bug Tracker": "https://github.com/seadhy/capsolver-api/issues",
    },
    classifiers=classifiers,
    install_requires=["requests"],
    packages=['capsolver_api', 'capsolver_api.tasks', 'capsolver_api.recognitions'],
    include_package_data=True,
    python_requires=">=3",

)
