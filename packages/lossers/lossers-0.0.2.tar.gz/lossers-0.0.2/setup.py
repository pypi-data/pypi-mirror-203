from setuptools import setup, find_packages

setup(
  name = 'lossers',
  packages = find_packages(),
  version = '0.0.2',
  license='MIT',
  description = 'ML Loss Function',
  author = 'JiauZhang',
  author_email = 'jiauzhang@163.com',
  url = 'https://github.com/JiauZhang/lossers',
  long_description_content_type = 'text/markdown',
  keywords = [
    'artificial intelligence',
    'loss function',
    'deep learning',
  ],
  install_requires=[
  ],
  classifiers=[
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)