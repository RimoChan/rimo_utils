import pickle
import hashlib
from pathlib import Path


def disk_cache(path):
    path = Path(path)
    if path.is_file():
        raise Exception('你不对劲')
    path.mkdir(parents=True, exist_ok=True)
    def q(func):
        name = func.__name__
        def 假func(*li, **d):
            s = pickle.dumps([name, li, d])
            md5 = hashlib.md5(s).hexdigest()
            名字 = f'{name}_{md5}'
            if (path/名字).is_file():
                with open(path/名字, 'rb') as f:
                    return pickle.loads(f.read())
            else:
                r = func(*li, **d)
                with open(path/名字, 'wb') as f:
                    f.write(pickle.dumps(r))
                return r
        return 假func
    return q
