from setuptools import setup, find_packages
# from dailytools import __version__

__version__ = "1.0.1"

setup(
    name='dailywheels',
    version=__version__,
    packages=['dailytools', 'dailytools.audio',
            'dailytools.encrypt'],
    package_dir = {
    'dailytools': 'dailytools',
    'dailytools.audio': 'dailytools/audio',
    'dailytools.encrypt': 'dailytools/encrypt'},
    install_requires=[
        'chardet',
        'gmssl',
        'eyed3',
        'baidu-aip',
        'wave',
        'AudioSegment'
    ],

    author='K2_AI_lab Niuhongfei',
    author_email='niuhongfei1@gmail.com',
    description='Common Audio Tools including TTS, Encrypt, Log, Audio Exception',
    keywords='tts,encrypt,logger,audio exception',
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',

        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    include_package_data=True,
    exclude_package_date={'':['.gitignore', "__pycache__/", ".DS_Store"]}
)
