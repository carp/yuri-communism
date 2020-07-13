# yuri communism twitter bot 

bot that adds quotes on (anime) images. uses [facial detection](https://github.com/qhgz2013/anime-face-detector) to try to prevent text from getting over anime character's face

## steps

- `conda env create -f envs/environment.yml`
- `conda env create -f envs/environment-detect.yml`
- `conda activate yuribot `
- `python provision.py`
- setup [anime-face-detector](https://github.com/qhgz2013/anime-face-detector)
- move [anime-face-detector](https://github.com/qhgz2013/anime-face-detector) `models` to base
- `python bot.py`

![example image](https://pbs.twimg.com/media/EWa1e1wWsAA6Vt0?format=jpg)
