# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['live_transcribe']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23,<2.0,!=1.24.0,!=1.24.1,!=1.24.2',
 'openai-whisper>=20230314,<20230315',
 'pasimple>=0.0.1,<0.0.2',
 'pulsectl>=22.3.2,<23.0.0']

entry_points = \
{'console_scripts': ['live-transcribe = live_transcribe:__main__']}

setup_kwargs = {
    'name': 'live-transcribe',
    'version': '0.1.2',
    'description': "Real-time audio transcription. Runs OpenAI's Whisper locally.",
    'long_description': 'Live Transcribe\n\nLive Transcribe is a Python package that provides live, real-time transcription based on OpenAI\'s Whisper. Works\noffline.\n\nCurrently, Live Transcribe supports only PulseAudio as an audio backend.\n\n# Installation\n\n1. **optional but highly recommended for low latency** Refer to the [Pytorch documentation guide](https://pytorch.org/)\n   to install Pytorch **with CUDA support**.\n1. `pip install live-transcribe`\n\n# Usage\n\nJust run:\n\n    python -m live_transcribe\n\nor\n\n    live_transcribe\n\nIf you want to transcribe from another audio device, than the default, use the `--device` option, e.g.:\n\n    live_transcribe --list-devices\n    live_transcribe --device "alsa_input.usb-046d_HD_Pro_Webcam_C920_8C0B5B0F-02.analog-stereo\n\nOn the first usage, the OpenAI\'s Whisper model will be downloaded and cached.\n\nSee `live_transcribe --help` for options.\n\n# Dependencies\n\nLive Transcribe has the following dependencies:\n\n    Python 3.8 or higher\n    OpenAI-Whisper\n    PulseAudio\n',
    'author': 'Tomasz Łakota',
    'author_email': 'tomasz.lakota@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
