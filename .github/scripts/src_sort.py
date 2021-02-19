# https://github.com/Celeter/SourceGo
# Created by Celeter
# 书源分类脚本
import os, time, json, datetime

work_space = os.path.join(os.environ.get('GITHUB_WORKSPACE'), 'book_source')


def get_timestamp():
    t = time.time()
    # 秒级时间戳
    # timestamp = int(t)
    # 毫秒级时间戳
    timestamp = int(round(t * 1000))
    return timestamp


def time_format(timestamp):
    # 毫秒级时间戳
    if timestamp > 9999999999:
        timestamp = int(timestamp / 1000)
    # localtime = time.localtime(timestamp)
    # str_time = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
    utc_time = datetime.datetime.utcfromtimestamp(timestamp)
    str_time = utc_time + datetime.timedelta(hours=8)
    return str_time


def read_file(path):
    with open(path, encoding='utf-8') as f:
        result = f.read()
    return result


def write_file(path, src):
    data = json.dumps(src, indent=2, ensure_ascii=False)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)


def create_dir(name):
    if not os.path.exists(name):
        os.makedirs(name)


def json_group(src_list):
    # 源分组
    for src in src_list:
        if str(src['bookSourceGroup']).find('失效') > -1:
            src['bookSourceGroup'] = '❌失效'
        if str(src['bookSourceComment']).find('https://celeter.github.io/SourceGo') > -1:
            pass
        else:
            src['bookSourceComment'] = 'https://celeter.github.io/SourceGo\n' + src['bookSourceComment']
        if src.get('lastUpdateTime') is None:
            src['lastUpdateTime'] = get_timestamp()
        if src.get('loginUrl') is not None and not str(src['loginUrl']).startswith('http'):
            del src['loginUrl']
        create_dir(os.path.join(work_space, src['bookSourceGroup']))
        write_file(os.path.join(work_space, src['bookSourceGroup'], f"{src['bookSourceName']}.json"), [src])
    # 失效源
    error_list = [src for src in src_list if src['bookSourceGroup'] == '❌失效']
    error_len = len(error_list)
    print('共有源{}个，失效{}个'.format(len(src_list), error_len))
    for e in error_list:
        print('失效源: {}\t{}'.format(e['bookSourceName'], e['bookSourceUrl']))


def get_folder_list(folder_dir):
    dir_list = os.listdir(folder_dir)
    fold_list = []
    for d in dir_list:
        sub_dir = os.path.join(folder_dir, d)
        if os.path.isdir(sub_dir):
            fold_list.append(sub_dir)
    return fold_list


if __name__ == '__main__':
    import_file = os.path.join(work_space, '..', '.history', 'bookSource.json')
    if os.path.exists(import_file):
        source_list = json.loads(read_file(import_file))
        json_group(source_list)

    # 保存源长度至环境变量
    # os.system('echo "::set-env name=SRC_LEN::{}"'.format(1))
