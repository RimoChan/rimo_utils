import logging

import chardet


def good_open(path, mode='r', encoding=None):
    if mode == 'r' and encoding is None:
        with open(path, 'rb') as f:
            a = chardet.detect(f.read())
            if a['encoding'] == 'GB2312':
                a['encoding'] = 'GBK'
        if a['confidence'] < 0.75:
            try:
                open(path).read()
            except UnicodeDecodeError:
                logging.warning(f'没能自动识别「{path}」的编码，尝试用utf8编码打开。')
                return open(path, encoding='utf8')
            else:
                logging.warning(f'没能自动识别「{path}」的编码，尝试用默认编码打开。')
                return open(path)
        else:
            return open(path, encoding=a['encoding'])
    return open(path, mode=mode, encoding=encoding)
