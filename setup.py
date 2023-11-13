import setuptools

setuptools.setup(
    include_package_data=True,
    name='math_quiz',
    version='0.0.1',
    description='jeevithpavithran24 python module',
    url='https://github.com/JeevithPavithran/jeevithpavithran24.git',
    author='jeevithpavithran24',
    author_email='contact@jeevithpavithran24.com',
    packages=setuptools.find_packages(),
    install_requires=['pandas', 'pytest'
    ],
    long_description='jeevithpavithran24 python module',
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
    ],
)
