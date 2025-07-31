from setuptools import setup

setup(name='lasotuvi',
      version='0.1.2',
      description='Chương trình an sao tử vi mã nguồn mở',
      url='https://github.com/doanguyen/lasotuvi',
      author='doanguyen',
      author_email='dungnv2410@gmail.com',
      license='MIT',
      packages=['lasotuvi'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      install_requires=[
        "attrs>=23.1.0",
        "ephem>=4.1",
        "more-itertools>=10.0",
        "mypy>=1.7",
        "pluggy>=1.3",
        "py>=1.11.0",
        "pytest>=8.0",
        "six>=1.16.0",
        "typed-ast>=1.5.5"
      ],
      zip_safe=False)
