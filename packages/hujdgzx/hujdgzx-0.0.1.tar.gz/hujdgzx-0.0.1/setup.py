from setuptools import setup, find_packages
import os


setup(
    name='hujdgzx',
    packages=find_packages(),
    include_package_data=True,
    version="0.0.1",
    description='A free and open-source SMS,Call & Mail bombing application',
    long_description="A free and open-source SMS,Call & Mail bombing application",
    long_description_content_type="text/markdown",
    author='TheSpeedX',
    author_email='ggspeedx29@gmail.com',
    url='https://github.com/TheSpeedX/gtfr',
    download_url="https://github.com/TheSpeedX/gtfr/archive/pypi.zip",
        keywords=['android', 'spam', 'sms', 'mail', 'gtfr',
                  'call', 'bomb', 'termux', 'bomber', 'spammer'],
    classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
            'Environment :: Console',
    ],
    install_requires=["requests"],
    license='GPL',
    entry_points={
            'console_scripts': [
                'hujdgzx = hujdgzx.kl:main',
            ],
    },
    python_requires='>=3.5'
)
