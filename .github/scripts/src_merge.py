# https://github.com/Celeter/SourceGo
# Created by Celeter
# 书源合并脚本
import os, time, json, datetime


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


def update_readme(dir):
    src_list = json.loads(read_file(os.path.join(dir, 'all.json')))
    text_list_1 = []
    text_list_2 = []
    index = 1
    for src in src_list:
        text_list_1.append(
            f'| {index} | {src["bookSourceName"]} | {src["bookSourceUrl"]}	| {time_format(src["lastUpdateTime"])} | {src["bookSourceGroup"]} | <a href="https://celeter.github.io/SourceGo/book_source/{src["bookSourceGroup"]}/{src["bookSourceName"]}.json">点击</a>')
        text_list_2.append(f'''
<tr>
    <td>{index}</td>
    <td><a href='https://celeter.github.io/SourceGo/book_source/{src["bookSourceGroup"]}/{src["bookSourceName"]}.json' rel="nofollow" target="_blank">{src["bookSourceName"]}</a></td>
    <td><a href="{src['bookSourceUrl']}" rel="nofollow" target="_blank">{src["bookSourceUrl"]}</a></td>
    <td>{time_format(src["lastUpdateTime"])}</td>
    <td>{src["bookSourceGroup"]}</td>
    <td><a href='yuedu://booksource/importonline?src=https://celeter.github.io/SourceGo/book_source/{src["bookSourceGroup"]}/{src["bookSourceName"]}.json' rel="nofollow">点击</a></td>
</tr>'''
                           )
        index += 1
    text_1 = '\n'.join(text_list_1)
    text_2 = '\n'.join(text_list_2)
    log = f'''
### **「阅读」APP 精品书源** 

## 3.0 书源链接

- 书源：`{len(src_list)}个书源`
- 复制下面链接，在阅读里`网络导入`
- <a href='yuedu://booksource/importonline?src=https://celeter.github.io/SourceGo/book_source/all.json'>https://celeter.github.io/SourceGo/book_source/all.json</a>
- 更新日期：{time_format(get_timestamp())}

## 导入方案

### 方案一
- 先点击左下角把阅读内所有书源全选，再点击右下角的删除，最后复制本站书源链接，在网络导入里面导入！(推荐此方法，省时又省力！)。

### 方案二
- 点击左下角全选，再点击右下角那三个点选择校验所选，将校验失效的删除，通过网络导入导入本站书源进行覆盖！)


## 导入教程

> 复制“书源链接”，打开阅读，点击右下角“我的”，然后选择“书源管理”，点击右上角三个点，选择“网络导入”，粘贴链接，确定即可。

##  书源列表

|序号 | 书源名称  | 书源地址  | 更新时间 | 书源分组  | 导入 |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
{text_1}


##  请选择扶贫方式

<table><tr>
    <td><img src="https://cdn.jsdelivr.net/gh/Celeter/SourceGo/.github/scripts/alipay.jpg" width="300px"></td>
    <td><img src="https://cdn.jsdelivr.net/gh/Celeter/SourceGo/.github/scripts/wechatpay.png" width="300px"></td>
    <td><img src="https://cdn.jsdelivr.net/gh/Celeter/SourceGo/.github/scripts/qqpay.png" width="300px"></td>
</tr></table>

------------

## 温馨提示

- 有任何问题可以在最底部评论区留言交流。
- 防止失联，可将本贴加入收藏或书签，更新书源快人一步！
- 本站所有内容仅供书友交流学习，勿做商用。
    '''
    with open(os.path.join(dir, '..', 'README.md'), 'w', encoding='utf-8') as f:
        f.write(log)

    html = f'''
<!DOCTYPE html>
<html>
<head>
  <meta charset='UTF-8' />
  <meta name='viewport' content='width=device-width initial-scale=1' />
  <link rel="icon" href="https://gitee.com/alanskycn/yuedu/raw/master/JS/icon.jpg" />
  <title>精品源</title>
  <!--<link href='https://fonts.loli.net/css?family=Open+Sans:400italic,700italic,700,400&subset=latin,latin-ext' rel='stylesheet' type='text/css' />-->
  <link rel="stylesheet" type="text/css" href="index.css" />
</head>
<body class='typora-export os-windows'>
  <div id='write' class=''>
    <h3><a name="阅读app-精品书源" class="md-header-anchor" id="阅读app-精品书源"></a><strong><span>「阅读」APP 精品书源</span></strong> <span></span></h3>
    <h2><a name="30-书源链接" class="md-header-anchor" id="30-书源链接"></a><span>3.0 书源链接</span></h2>
    <ul>
      <li><span>书源：</span><code>{len(src_list)}个书源</code></li>
      <li><span>复制下面链接，在阅读里<code>网络导入</code>或直接点击自动导入</span></li>
      <li><a href='yuedu://booksource/importonline?src=https://celeter.github.io/SourceGo/book_source/all.json'>https://celeter.github.io/SourceGo/book_source/all.json</a></li>
      <li><span>更新日期：{time_format(get_timestamp())}</span></li>
    </ul>
    <h2><a name="导入方案" class="md-header-anchor" id="导入方案"></a><span>导入方案</span></h2>
    <h3><a name="方案一" class="md-header-anchor" id="方案一"></a><span>方案一</span></h3>
    <ul>
      <li><span>先点击左下角把阅读内所有书源全选，再点击右下角的删除，最后复制本站书源链接，在网络导入里面导入！(推荐此方法，省时又省力！)。</span></li>
    </ul>
    <h3><a name="方案二" class="md-header-anchor" id="方案二"></a><span>方案二</span></h3>
    <ul>
      <li><span>点击左下角全选，再点击右下角那三个点选择校验所选，将校验失效的删除，通过网络导入导入本站书源进行覆盖！)</span></li>
    </ul>
    <h2><a name="导入教程" class="md-header-anchor" id="导入教程"></a><span>导入教程</span></h2>
    <blockquote>
      <p><span>1.复制“书源链接”，打开阅读，点击右下角“我的”，然后选择“书源管理”，点击右上角三个点，选择“网络导入”，粘贴链接，确定即可。</span></p>
      <p><span>2.直接点击自动导入</span></p>
    </blockquote>
    <h2><a name="书源列表" class="md-header-anchor" id="书源列表"></a><span>书源列表</span></h2>
<table>
<thead>
<tr>
<th>序号</th>
<th>书源名称</th>
<th>书源地址</th>
<th>更新时间</th>
<th>书源分组</th>
<th>导入</th>
</tr>
</thead>
<tbody>
{text_2}
</tbody>
</table>
<hr />
<h2><span>请选择扶贫方式</span></h2>
<table><tr>
    <td><img src="https://cdn.jsdelivr.net/gh/Celeter/SourceGo/.github/scripts/alipay.jpg" style="width:300px;"></td>
    <td><img src="https://cdn.jsdelivr.net/gh/Celeter/SourceGo/.github/scripts/wechatpay.png" style="width:300px;"></td>
    <td><img src="https://cdn.jsdelivr.net/gh/Celeter/SourceGo/.github/scripts/qqpay.png" style="width:300px;"></td>
</tr></table>
<h2><span>温馨提示</span></h2>
<ul>
<li><span>有任何问题可以在最底部评论区留言交流。</span></li>
<li><span>防止失联，可将本贴加入收藏或书签，更新书源快人一步！</span></li>
<li><span>本站所有内容仅供书友交流学习，勿做商用。</span></li>
</ul></div>
</body>
</html>
'''
    with open(os.path.join(dir, '..', 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)


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


# 获取文件夹的路径列表
def get_folder_list(folder_dir: str):
    dir_list = os.listdir(folder_dir)
    fold_list = []
    for d in dir_list:
        sub_dir = os.path.join(folder_dir, d)
        if os.path.isdir(sub_dir):
            fold_list.append(sub_dir)
    return fold_list


# 获取文件的名称列表
def get_file_list(folder_dir: str):
    dir_list = os.listdir(folder_dir)
    f_list = []
    for d in dir_list:
        sub_dir = os.path.join(folder_dir, d)
        if os.path.isfile(sub_dir):
            f_list.append(d)
    return f_list


# 保存子分类
def save_file_group(file_dir):
    dir_list = get_file_list(file_dir)
    sort_list = []
    for d in dir_list:
        if d == 'sub.json' or (not d.endswith('.json') and not d.endswith('.txt')):
            continue
        sub_dir = os.path.join(file_dir, d)
        if os.path.isfile(sub_dir):
            j = json.loads(read_file(sub_dir))
            sort_list.extend(j)
    sub_path = os.path.join(file_dir, 'sub.json')
    write_file(sub_path, sort_list)
    print(f'子分类更新完成:{sub_path}')


def merge(path, src_list):
    i = 1
    for src in src_list:
        src['bookSourceComment'] = 'https://celeter.github.io/SourceGo'
        src['customOrder'] = i
        i += 1
    all_path = os.path.join(path, 'all.json')
    write_file(all_path, src_list)
    print(f'所有源更新完成:{all_path}')


def get_all_src(folder_list):
    print('开始获取全部书源')
    src_list = []
    for folder in folder_list:
        save_file_group(folder)
        if folder.find('失效') > -1:
            print('排除文件夹:{}'.format(folder))
            continue
        file_list = get_file_list(folder)
        for file in file_list:
            if file == 'sub.json' or (not file.endswith('.json') and not file.endswith('.txt')):
                print('排除文件: {}'.format(os.path.join(folder, file)))
            else:
                file_path = os.path.join(folder, file)
                src = json.loads(read_file(file_path))
                for s in src:
                    if s['bookSourceGroup'].find('失效') > -1:
                        print('失效源: {}\t{}'.format(s['bookSourceName'], s['bookSourceUrl']))
                    else:
                        src_list.append(s)
    print(f'获取完成，有效源共{len(src_list)}个')
    return src_list


if __name__ == '__main__':
    work_space = os.environ.get('GITHUB_WORKSPACE')
    source_path = os.path.join(work_space, 'book_source')
    if os.path.exists(source_path):
        folder_list = get_folder_list(source_path)
        src_list = get_all_src(folder_list)
        merge(source_path, src_list)
    update_readme(source_path)
