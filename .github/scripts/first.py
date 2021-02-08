import os
import json


def read_file(path='source.json'):
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


def json_group(path, src_list):
    i = 0
    for src in src_list:
        src['bookSourceComment'] = ''
        src['customOrder'] = i
        create_dir(os.path.join(path, src['bookSourceGroup']))
        one_list = [src]
        write_file(os.path.join(path, src['bookSourceGroup'], src['bookSourceName'] + '.json'),
                   one_list)
        i += 1
    write_file(os.path.join(path, 'all.json'), src_list)


if __name__ == '__main__':
    work_space = os.path.join(os.environ.get('GITHUB_WORKSPACE'), 'book_source')
    source_path = os.path.join(work_space, '.history', 'bookSource.json')
    if os.path.exists(source_path):
        source_list = json.loads(read_file(source_path))
        json_group(work_space, source_list)
