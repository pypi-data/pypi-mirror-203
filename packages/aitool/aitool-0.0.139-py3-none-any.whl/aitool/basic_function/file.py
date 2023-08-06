# -*- coding: UTF-8 -*-
# @Time    : 2020/10/29
# @Author  : xiangyuejia@qq.com
import os
import sys
import json
import stat
import fileinput
import warnings
import pickle
from collections import defaultdict
import numpy as np
import pandas as pd
import inspect
import requests
from tqdm import tqdm
import math
import functools
import zipfile
from typing import Any, List, Union, NoReturn, Set, Type, Iterator, Callable, Tuple
from numpy import ndarray
from aitool.basic_function.basic import split_dict
from aitool.basic_function.deduplication import Deduplication


def is_writable(path):
    # Ensure that it exists.
    if not os.path.exists(path):
        return False

    # If we're on a posix system, check its permissions.
    if hasattr(os, "getuid"):
        statdata = os.stat(path)
        perm = stat.S_IMODE(statdata.st_mode)
        # is it world-writable?
        if perm & 0o002:
            return True
        # do we own it?
        elif statdata.st_uid == os.getuid() and (perm & 0o200):
            return True
        # are we in a group that can write to it?
        elif (statdata.st_gid in [os.getgid()] + os.getgroups()) and (perm & 0o020):
            return True
        # otherwise, we can't write to it.
        else:
            return False

    # Otherwise, we'll assume it's writable.
    # [xx] should we do other checks on other platforms?
    return True


def is_file(path: str) -> bool:
    """
    判断是否是个文件，如果是文件夹或不存在则返回False
    :param path:
    :return:
    """
    if os.path.isfile(path):
        return True
    return False


def is_folder(path: str) -> bool:
    """
    判断是否是个文件，如果是文件夹或不存在则返回False
    :param path:
    :return:
    """
    if os.path.isdir(path):
        return True
    return False


def is_file_exist(file: str) -> bool:
    """
    判断文件名是否存在
    :param file: 文件名
    :return: bool
    """
    return os.path.exists(file)


def is_file_hidden(file: str) -> bool:
    """
    TODO 有遗漏
    目前仅能识别以.开始的隐藏文件
    :param file:
    :return:
    """
    path, filename = os.path.split(file)
    if filename[0] == '.':
        return True
    return False


def file_exist(file: str) -> bool:
    """
    判断文件名是否存在
    :param file: 文件名
    :return: bool
    """
    print('out of data, please use is_file_exist')
    warnings.warn("已改名为is_file_exist", DeprecationWarning)
    return is_file_exist(file)


def get_file(
        path: str,
        skip_hidden: bool = True,
        skip_folder: bool = False,
        absolute: bool = False,
) -> Iterator[str]:
    """
    TODO skip_folder 没有实现
    遍历path下的所有文件（不包括文件夹）
    :param path: 待遍历的路径
    :return: 一个返回文件名的迭代器
    """
    for root, ds, fs in os.walk(path):
        for file in fs:
            file_path = os.path.join(root, file)
            if skip_hidden and is_file_hidden(file_path):
                continue
            if absolute:
                yield os.path.abspath(file_path)
            else:
                yield file_path


def add_python_path(
        _path: str,
        recursive: bool = True,
        show: bool = False,
) -> None:
    """
    将某路径下的所有python文件的绝对路径加到python_path

    用于处理ModuleNotFoundError问题
    通常只需要在对应文件开头加上，然后直接应该需要的包，而无需在意其所在的文件路径
    （需要确保项目里没有同名的python文件）
    # _path为从当前文件到项目根目录的相对路径
    >>> add_python_path('../', show=True)

    :param _path: 根路径
    :param recursive: 是否递归添加所有子路径
    :param show: 输出提示信息
    :return:
    """
    python_path = set()
    if show:
        print('DEAL PATH: ', os.path.abspath(_path))

    if recursive:
        name_single = defaultdict(list)
        for abs_path in get_file(_path, absolute=True):
            if abs_path[-3:] == '.py':
                basename = os.path.basename(abs_path)
                name_single[basename].append(abs_path)
                python_path.add(os.path.dirname(abs_path))
        for k in name_single.keys():
            if len(name_single[k]) > 1:
                print('WARNING: name {} presents multiple times {}'.format(k, name_single[k]))
    else:
        python_path.add(os.path.abspath(_path))

    for pth in python_path:
        sys.path.append(pth)
        if show:
            print('ADD PYTHON PATH: ', pth)


def make_dir(file: str, is_dir=False) -> NoReturn:
    """
    创建文件夹
    :param file: 文件名
    :param is_dir: 是否为文件
    :return: NoReturn
    """
    if is_dir:
        path = file
    else:
        path, _ = os.path.split(file)
    if path and not os.path.exists(path):
        os.makedirs(path)


def dump_json(
        obj: Any,
        file: str,
        formatting: bool = False,
        ensure_ascii: bool = False,
        format_postfix: bool = True,
        **kwargs,
) -> NoReturn:
    """
    写入json文件
    :param obj: 任意对象
    :param file: 存入文件
    :param formatting: dump with data-interchange format
    :param ensure_ascii: ensure ascii or not
    :param format_postfix: rename file name with tail .json
    :param kwargs: dict-formatted parameters
    :return: NoReturn
    """
    if format_postfix:
        if file[-5:] != '.json':
            print('rename file name with tail .json')
            file = file + '.json'
    make_dir(file)
    kwargs['ensure_ascii'] = ensure_ascii
    if formatting:
        kwargs['sort_keys'] = True
        kwargs['indent'] = 4
        kwargs['separators'] = (',', ':')
    with open(file, 'w', encoding='utf-8') as fw:
        json.dump(obj, fw, **kwargs)


def load_json(file: str, **kwargs,) -> Any:
    if not os.path.isfile(file):
        print('incorrect file path')
        raise FileExistsError
    with open(file, 'r', encoding='utf-8') as fr:
        return json.load(fr, **kwargs,)


def dump_pickle(
        obj: Any,
        file: str,
        format_postfix: bool = True,
        **kwargs,
) -> NoReturn:
    if format_postfix:
        if file[-4:] != '.pkl':
            print('rename file name with tail .pkl')
            file = file + '.pkl'
    make_dir(file)
    with open(file, 'wb') as fw:
        pickle.dump(obj, fw, **kwargs)


def load_pickle(file: str, **kwargs) -> Any:
    if not os.path.isfile(file):
        print('incorrect file path')
        raise Exception
    with open(file, 'rb') as fr:
        return pickle.load(fr, **kwargs)


def dump_lines(
        data: List[Any],
        file: str,
) -> NoReturn:
    make_dir(file)
    with open(file, 'w', encoding='utf8') as fout:
        for d in data:
            print(d, file=fout)


class Accessor:
    """
    用于打开文件
    """
    def __init__(self, file: str, open_method: str = 'fileinput') -> NoReturn:
        self.file = file
        self.iterator = None
        if open_method == 'open':
            self.iterator = open(self.file, 'r', encoding='utf8')
        if open_method == 'fileinput':
            self.iterator = fileinput.input([self.file])

    def __enter__(self) -> Iterator:
        return self.iterator

    def get_iterator(self) -> Iterator:
        return self.iterator

    def close(self) -> NoReturn:
        if self.iterator:
            self.iterator.close()

    def __exit__(self, exc_type, exc_val, exc_tb) -> NoReturn:
        self.close()


def repeat(item: Any) -> Any:
    """
    原样返回输入，用于作为Callable参数的默认值
    """
    return item


def load_line(
        file: str,
        separator: Union[None, str] = None,
        max_split: int = -1,
        deduplication: bool = False,
        line_processor: Callable = repeat,
        open_method: str = 'open',
        limit: int = -1,
) -> Iterator:
    """
    按行读入文件，会去掉每行末尾的换行符
    :param file: 文件路径
    :param separator: 用separator切分每行内容，None表示不做切分
    :param max_split: 控制separator的切分次数，-1表示不限制次数
    :param line_processor: 一个函数，对separator的结果做处理
    :param deduplication: 若为True，将不输出重复的行
    :param open_method: 指定打开文件的方法
    :param limit: 仅读前limit行
    :return: 文件每行的内容
    """
    cache = Deduplication()

    def inner_line_process(_file_iterator):
        count = 0
        for line in _file_iterator:
            if deduplication and cache.is_duplication(line):
                continue
            item = line.rstrip('\n\r')
            if separator:
                item = item.split(separator, max_split)
            count += 1
            if limit != -1 and count > limit:
                break
            yield line_processor(item)

    with Accessor(file, open_method=open_method) as file_iterator:
        yield from inner_line_process(file_iterator)


def load_big_data(
        file: str,
        separator: Union[None, str] = None,
        max_split: int = -1,
        deduplication: bool = False,
        line_processor: Callable = repeat,
) -> Union[str, List[str], Set[str]]:
    warnings.warn("已合并到load_line，可通过use_open=False调用", DeprecationWarning)
    yield from load_line(
        file=file,
        separator=separator,
        max_split=max_split,
        line_processor=line_processor,
        deduplication=deduplication,
        open_method='fileinput',
    )


def load_byte(
        file: str,
        size: int = 10,
) -> bytes:
    with open(file, 'rb') as file:
        for chunk in iter(lambda: file.read(size), b''):
            yield chunk


def load_lines(
        file: str,
        separator: Union[None, str] = None,
        separator_time: int = -1,
        form: str = None,
        deduplication: bool = False,
) -> Union[list, dict, set]:
    data = []
    cache = Deduplication()
    with open(file, 'r', encoding='utf8') as fin:
        for line in fin.readlines():
            if deduplication and cache.is_duplication(line):
                continue
            item = line.rstrip('\n\r')
            if separator:
                if separator_time == -1:
                    item = item.split(separator)
                else:
                    item = item.split(separator, separator_time)
            data.append(item)
    if form == 'set':
        data = set(data)
    if form == 'dict':
        print('dict格式用每行的第一个元素作为key, 其后的元素的列表作为value。'
              '如果一行中不包含多个元素会报错。'
              '如果有相同的第一个元素会发生覆盖。')
        data = {item[0]: item[1:] if len(item) > 2 else item[1] for item in data}
    return data


MAX_LENGTH_XLSX = 1048576


def dump_panda(
        data: List[Any],
        file: str,
        file_format: str,
        dump_index: bool = False,
        format_postfix: bool = True,
        **kwargs,
) -> NoReturn:
    if format_postfix:
        if file_format == 'excel':
            if file[-5:] != '.xlsx':
                print('rename file name with tail .xlsx')
                file = file + '.xlsx'
        if file_format == 'csv':
            if file[-4:] != '.csv':
                print('rename file name with tail .csv')
                file = file + '.csv'
    make_dir(file)

    if 'index' in kwargs and isinstance(kwargs['index'], bool):
        raise ValueError('The parameter `index` is for pd.DataFrame. '
                         'If want to set the `index` for panda.to_csv/excel please use `dump_index`'
                         'If want to hide the header please use `heade=None`')
    if file_format == 'excel':
        print('WARNING: default set header=False')
        kwargs['header'] = False if 'header' not in kwargs else kwargs['header']
        kwargs['keep_default_na'] = False if 'keep_default_na' not in kwargs else kwargs['keep_default_na']  # no nan

        if len(data) < MAX_LENGTH_XLSX - 100:
            selected_kwargs, _ = split_dict(kwargs, inspect.getfullargspec(pd.DataFrame).args)
            df = pd.DataFrame(data, **selected_kwargs)
            selected_kwargs, _ = split_dict(kwargs, inspect.getfullargspec(df.to_csv).args)
            selected_kwargs['index'] = dump_index
            selected_kwargs['engine'] = 'xlsxwriter' if 'engine' not in selected_kwargs else selected_kwargs['engine']
            df.to_excel(file, **selected_kwargs)
        else:
            piece_num = 0
            while data:
                piece_data = data[:MAX_LENGTH_XLSX - 100]
                piece_file = file + '_piece_' + str(piece_num) + '.xlsx'
                data = data[MAX_LENGTH_XLSX - 100:]
                selected_kwargs, _ = split_dict(kwargs, inspect.getfullargspec(pd.DataFrame).args)
                df = pd.DataFrame(piece_data, **selected_kwargs)
                selected_kwargs, _ = split_dict(kwargs, inspect.getfullargspec(df.to_csv).args)
                selected_kwargs['index'] = dump_index
                selected_kwargs['engine'] = 'xlsxwriter' if 'engine' not in selected_kwargs else selected_kwargs[
                    'engine']
                df.to_excel(piece_file, **selected_kwargs)
                piece_num += 1
    if file_format == 'csv':
        selected_kwargs, _ = split_dict(kwargs, inspect.getfullargspec(pd.DataFrame).args)
        df = pd.DataFrame(data, **selected_kwargs)
        selected_kwargs, _ = split_dict(kwargs, inspect.getfullargspec(df.to_csv).args)
        selected_kwargs['index'] = dump_index
        df.to_csv(file, **selected_kwargs)


dump_csv = functools.partial(dump_panda, file_format='csv')
dump_excel = functools.partial(dump_panda, file_format='excel')


def load_excel(*args, to_list=False, **kwargs) -> Union[ndarray, List]:
    print(args[0])
    if args[0][-4:] == '.xls':
        kwargs['engine'] = 'xlrd' if 'engine' not in kwargs else kwargs['engine']
    else:
        kwargs['engine'] = 'openpyxl' if 'engine' not in kwargs else kwargs['engine']
    kwargs['keep_default_na'] = False if 'keep_default_na' not in kwargs else kwargs['keep_default_na']

    data = np.array([])
    try:
        df = pd.read_excel(*args, **kwargs)
        data = df.values
    except ValueError as err:
        print(err)
    if to_list:
        data_list = data.tolist()
        if not isinstance(data_list, list):
            data_list = [data_list]
        return data_list
    return data


def load_csv(*args, to_list=False, **kwargs) -> Union[ndarray, Any]:
    df = pd.read_csv(*args, **kwargs)
    data = df.values
    if to_list:
        return data.tolist()
    return data


def zip(src: str, tgt: str = '') -> NoReturn:
    """
    zip a file or a director.
    :param src: a file or a director
    :param tgt: Optional, the output file
    :return: NoReturn
    """
    # if tgt is Empty, then name the zipped file with a suffix .zip and save in the same director of src file/dir
    if not tgt:
        src_path, src_name = os.path.split(os.path.normpath(src))
        tgt_file = os.path.join(src_path, src_name+'.zip')
    # if tgt is a director, then name the zipped file with a suffix .zip and save in the director tgt
    _, tgt_name = os.path.split(tgt)
    if '.' not in tgt_name:
        src_path, src_name = os.path.split(os.path.normpath(src))
        tgt = os.path.join(tgt, src_name+'.zip')
    make_dir(tgt)
    z = zipfile.ZipFile(tgt, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_names, file_names in os.walk(src):
        f_path = dir_path.replace(src, '')
        f_path = f_path and f_path + os.sep or ''
        for filename in file_names:
            z.write(os.path.join(dir_path, filename), f_path+filename)
    z.close()


def unzip(src: str, tgt: str = '') -> NoReturn:
    if not tgt:
        tgt, _ = os.path.split(os.path.normpath(src))
    make_dir(tgt)
    r = zipfile.is_zipfile(src)
    if r:
        fz = zipfile.ZipFile(src, 'r')
        for file in fz.namelist():
            fz.extract(file, tgt)
    else:
        print('This is not a zip file')


def split_path(file_path: str) -> Tuple[str, str, Any, Any]:
    dir_name, full_file_name = os.path.split(file_path)
    file_name, file_ext = os.path.splitext(full_file_name)
    return dir_name, full_file_name, file_name, file_ext


if __name__ == '__main__':
    # test_data = [[i] for i in range(26)]
    # test_file = 'tmp.xlsx'
    # dump_excel(test_data, test_file)
    # for text in load_big_data('A.log', separator=' '):
    #     print(text)
    # add_python_path('../', recursive=False, show=True)
    # load_excel('a.xls')
    # print(split_path('./a/b.k.txt'))
    # for l in load_line('/a.txt', limit=5):
    #     print(l)
    for x in load_byte('test_111.txt'):
        print(x)
