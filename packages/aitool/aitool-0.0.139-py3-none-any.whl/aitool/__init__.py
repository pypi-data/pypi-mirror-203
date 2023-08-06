# in-package data path
from aitool.datasets import PATH as DATAPATH
# web data path
from aitool.datasets import WEB as WEBPATH

# BASIC FUNCTION
from aitool.basic_function.basic import split_dict
from aitool.basic_function.basic import replace_char
from aitool.basic_function.basic import split_char
from aitool.basic_function.basic import split_punctuation
from aitool.basic_function.basic import is_appear

from aitool.basic_function.string import find_all_position
from aitool.basic_function.string import get_ngram
from aitool.basic_function.string import token_hit

from aitool.basic_function.security import encrypt_md5

from aitool.basic_function.deduplication import Deduplication
from aitool.basic_function.deduplication import deduplicate

from aitool.basic_function.path import get_user_root_path as get_user_root_path

from aitool.basic_function.random import random_base64 as random_base64

from aitool.basic_function.file import is_writable as is_writable
from aitool.basic_function.file import file_exist as file_exist
from aitool.basic_function.file import is_file_exist as is_file_exist
from aitool.basic_function.file import is_file as is_file
from aitool.basic_function.file import is_folder as is_folder
from aitool.basic_function.file import make_dir as make_dir
from aitool.basic_function.file import is_file_hidden as is_file_hidden
from aitool.basic_function.file import get_file as get_file
from aitool.basic_function.file import add_python_path as add_python_path

from aitool.basic_function.file import dump_json as dump_json
from aitool.basic_function.file import load_json as load_json
from aitool.basic_function.file import dump_pickle as dump_pickle
from aitool.basic_function.file import load_pickle as load_pickle
from aitool.basic_function.file import dump_lines as dump_lines
from aitool.basic_function.file import load_big_data as load_big_data
from aitool.basic_function.file import load_line as load_line
from aitool.basic_function.file import load_lines as load_lines
from aitool.basic_function.file import dump_excel as dump_excel
from aitool.basic_function.file import load_excel as load_excel
from aitool.basic_function.file import dump_csv as dump_csv
from aitool.basic_function.file import load_csv as load_csv

from aitool.basic_function.file import zip as zip
from aitool.basic_function.file import unzip as unzip
from aitool.basic_function.file import split_path as split_path


from aitool.basic_function.download.download import download_file as download_file
from aitool.basic_function.download.download import get_download_dir as get_download_dir
from aitool.basic_function.download.download import get_aitool_data_path as get_aitool_data_path
from aitool.basic_function.download.download import prepare_data as prepare_data


from aitool.basic_function.format_data import flatten as flatten
from aitool.basic_function.format_data import html2text as html2text
from aitool.basic_function.format_data import content2text as content2text
from aitool.basic_function.format_data import split_part as split_part
from aitool.basic_function.format_data import get_pair as get_pair
from aitool.basic_function.format_data import np2list as np2list
from aitool.basic_function.format_data import get_most_item as get_most_item

from aitool.basic_function.singleton import singleton as singleton
from aitool.basic_function.exe_time import exe_time as exe_time
from aitool.basic_function.retry import retry
from aitool.basic_function.time import timeout
from aitool.basic_function.time import timestamp

# cache 管理工具
from aitool.basic_function.cache import cache  # 装饰器
from aitool.basic_function.cache import get_cache
from aitool.basic_function.cache import Cache

# 多进程
from aitool.basic_function.multi import pool_map
from aitool.basic_function.multi import pool_starmap
from aitool.basic_function.multi import multi_map
from aitool.basic_function.multi import get_functions
from aitool.basic_function.multi import multi

from aitool.task_customized.ip_enhance.filter import has_family_name
from aitool.task_customized.ip_enhance.filter import is_common_word
from aitool.task_customized.ip_enhance.filter import is_stop_word
from aitool.task_customized.ip_enhance.filter import is_relationship_title
from aitool.task_customized.ip_enhance.filter import is_contains_english
from aitool.task_customized.ip_enhance.filter import cut_until_char
from aitool.task_customized.ip_enhance.filter import delete_char
from aitool.task_customized.ip_enhance.filter import is_nick_name
from aitool.task_customized.ip_enhance.filter import is_contains_figure
from aitool.task_customized.ip_enhance.filter import delete_age_describe
from aitool.task_customized.ip_enhance.filter import is_contains_chinese
from aitool.task_customized.ip_enhance.filter import is_all_chinese
from aitool.task_customized.ip_enhance.filter import is_black_name
from aitool.task_customized.ip_enhance.filter import clean_role
from aitool.task_customized.ip_enhance.filter import clean_alias
from aitool.task_customized.ip_enhance.filter import delete_nested_text
from aitool.task_customized.ip_enhance.filter import select_nested_text
from aitool.task_customized.ip_enhance.filter import is_sub_ip
from aitool.task_customized.ip_enhance.filter import get_core_ip
from aitool.task_customized.keyword_mining.keyword import get_keyword_graph
from aitool.task_customized.keyword_mining.keyword import get_keyword_graph4panda
from aitool.task_customized.keyword_mining.keyword import get_keyword
from aitool.task_customized.keyword_mining.keyword import SentenceKeyword


# NLP FUNCTION
from aitool.nlp.basic.split_sentence import split_sentence
from aitool.nlp.sentiment_analysis.dict_match import Sentiment

from aitool.nlp.basic.conditional_probability import conditional_probability
