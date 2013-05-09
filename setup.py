#!/usr/bin/python

from setuptools import setup


if __name__ == "__main__":
    setup(
        name="irnetproxy",
        version="1.0",
        license="BSD",

        description="A network proxy for RedRat irNetBox MK-III infra-red blaster modules.",
        author="Steve Stagg",
        author_email="stestagg@gmail.com",
        url="http://github.com/stestagg/irnetproxy",

        
        py_modules=['irnetproxy'],

        entry_points={'console_scripts': ['irnetproxy = irnetproxy:main']},
        data_files=[('share/irnetproxy', ['README.md'])],

        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
        ]

    )
