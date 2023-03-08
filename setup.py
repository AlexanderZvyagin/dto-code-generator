from setuptools import setup
import cgdto

setup(
    name='cgdto',
    version = cgdto.version(),
    description='Code Generator of Data Transfer Objects',
    # url='https://github.com/shuds13/pyexample',
    author='Alexander ZVYAGIN',
    author_email='zvyagin.alexander@gmail.com',
    license='GPL',
    packages=['cgdto'],
    scripts=['scripts/cgdto'],
    install_requires=[],
    classifiers=[
        # 'Development Status :: 1 - Planning',
        # 'Intended Audience :: Science/Research',
        # 'License :: OSI Approved :: BSD License',  
        # 'Operating System :: POSIX :: Linux',        
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
    ],
)
