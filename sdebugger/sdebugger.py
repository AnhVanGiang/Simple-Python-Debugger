from functools import wraps
import time
import logging


class Decorators:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    @classmethod
    def timecheck(cls, clss: object) -> object:
        """
        Show running function and its arguments with elapsed time
        :param clss: object
        :return: object
        """
        @wraps(clss)
        def decorate(func):
            @wraps(func)
            def check(*args, **kwargs):
                now = time.time()
                if len(args) == 0:
                    arguments = kwargs
                else:
                    arguments = args
                logging.info(msg='Running function "{}" with arguments: {}'.format(func.__name__, arguments))
                out = func(*args, **kwargs)
                logging.info(msg='Elapsed time: {} for function {}'.format(time.time() - now, func.__name__))
                return out
            return check

        for key, val in clss.__dict__.items():
            if hasattr(val, '__call__') and not key.startswith('__') and not key.endswith('__'):
                setattr(clss, key, decorate(val))
        return clss

    @classmethod
    def typecheck(cls, clss: object) -> object:
        """
        Check type annotations with arguments types
        :param clss: object
        :return: object
        """
        def typec(func):
            @wraps(func)
            def check(*args, **kwargs):
                types = func.__annotations__
                kw = func.__annotations__.keys()
                types_dic = {k: types[k] for k in kw if k != 'return'}
                args_dic = {k: type(v) for k, v in zip(kw, args) if not isinstance(v, type(clss))}
                final_args_dic = {**args_dic, **kwargs}
                for k1, k2 in zip(types_dic.keys(), final_args_dic.keys()):
                    rtype = types_dic[k1]
                    atype = type(final_args_dic[k1])
                    if rtype == atype:
                        continue
                    else:
                        raise TypeError('{} should be of type {} instead of {}'.format(k1, rtype, atype))
                return func(*args, **kwargs)
            return check

        for key, val in clss.__dict__.items():
            if hasattr(val, '__call__') and not key.startswith('__') and not key.endswith('__'):
                setattr(clss, key, typec(val))
        return clss
