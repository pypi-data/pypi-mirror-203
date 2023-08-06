from setuptools import setup, find_packages
import os


# requirements = os.popen("/usr/local/bin/pipreqs main --print").read().splitlines()



setup(
    name='Video_Audio_Image_Downloader',
    version='0.0.5',
    author='Sridhar',
    author_email='dcsvsridhar@gmail.com',
    description="In this tool is used to Download the Youtube Video,Audio and Any type of Google and other site's Images",
    packages=find_packages(),
    url='https://git.selfmade.ninja/SRIDHARDSCV/audio_video_image_downloder-1',
    # install_requires=requirements,
    entry_points={
        'console_scripts': [
            'Downloader=source.source:main',
        ],
    },
)
