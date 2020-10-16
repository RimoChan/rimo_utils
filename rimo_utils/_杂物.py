import logging

import chardet


def good_open(path):
    with open(path, 'rb') as f:
        a = chardet.detect(f.read())
        if a['encoding'] == 'GB2312':
            a['encoding'] = 'GBK'
    if a['confidence'] < 0.5:
        try:
            logging.warning(f'没能自动识别「{path}」的编码，尝试用默认编码打开。')
            open(path).read()
            return open(path)
        except:
            logging.warning(f'沒能自動識別「{path}」的编码，尝试用utf8编码打开。')
            return open(path, encoding='utf8')
    else:
        return open(path, encoding=a['encoding'])
