import os, time, json

work_space = os.path.join(os.environ.get('GITHUB_WORKSPACE'), 'book_source')


def get_timestamp():
    t = time.time()
    # 秒级时间戳
    # timestamp = int(t)
    # 毫秒级时间戳
    timestamp = int(round(t * 1000))
    return timestamp


def time_format(timestamp):
    # 秒级时间戳
    # localtime = time.localtime(timestamp)
    # 毫秒级时间戳
    localtime = time.localtime(timestamp / 1000)
    str_time = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
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
    all_length = len(src_list)
    # 源分组
    for src in src_list:
        if src['bookSourceGroup'].find('失效') > -1:
            src['bookSourceGroup'] = '❌失效'
        src['bookSourceComment'] = 'https://celeter.github.io/SourceGo'
        src['lastUpdateTime'] = get_timestamp()
        create_dir(os.path.join(work_space, src['bookSourceGroup']))
        write_file(os.path.join(work_space, src['bookSourceGroup'], f"{src['bookSourceName']}.json"), [src])
    # 源去失效
    new_src_list = [src for src in src_list if src['bookSourceGroup'] != '❌失效']
    new_length = len(new_src_list)
    i = 10
    for src in new_src_list:
        src['weight'] = new_length + 10 - i
        src['customOrder'] = i
        i += 1
    write_file(os.path.join(work_space, 'all.json'), new_src_list)
    print('共有源{}个，有效{}个'.format(all_length, new_length))


def get_folder_list():
    folder_dir = work_space
    dir_list = os.listdir(folder_dir)
    fold_list = []
    for d in dir_list:
        sub_dir = os.path.join(folder_dir, d)
        if os.path.isdir(sub_dir):
            fold_list.append(sub_dir)
    return fold_list


def save_file_group(file_dir):
    dir_list = os.listdir(file_dir)
    sort_list = []
    for d in dir_list:
        if d == 'sub.json':
            continue
        sub_dir = os.path.join(file_dir, d)
        if os.path.isfile(sub_dir):
            j = json.loads(read_file(sub_dir))[0]
            sort_list.append(j)
    write_file(os.path.join(file_dir, 'sub.json'), sort_list)


def update_readme():
    src_list = json.loads(read_file(os.path.join(work_space, 'all.json')))
    text_list_1 = []
    text_list_2 = []
    index = 1
    for src in src_list:
        text_list_1.append(
            f'| {index} | {src["bookSourceName"]} | {src["bookSourceUrl"]}	| {time_format(src["lastUpdateTime"])} | {src["bookSourceGroup"]} | <a href="https://celeter.github.io/SourceGo/book_source/{src["bookSourceGroup"]}/{src["bookSourceName"]}.json">导入</a>')
        text_list_2.append(f'''
<tr>
    <td>{index}</td>
    <td>{src["bookSourceName"]}</td>
    <td><a href="{src['bookSourceUrl']}" rel="nofollow">{src["bookSourceUrl"]}</a></td>
    <td>{time_format(src["lastUpdateTime"])}</td>
    <td>{src["bookSourceGroup"]}</td>
    <td><a href='yuedu://booksource/importonline?src=https://celeter.github.io/SourceGo/book_source/{src["bookSourceGroup"]}/{src["bookSourceName"]}.json' rel="nofollow">导入</a></td>
</tr>'''
                           )
        index += 1
    text_1 = '\n'.join(text_list_1)
    text_2 = '\n'.join(text_list_2)
    log = f'''
### **「阅读」APP 精品书源** 

## 3.0 书源链接

- 书源：`{len(src_list)}个书源`
- 复制下面链接，在阅读里`网络导入`。
- <a href='yuedu://booksource/importonline?src=https://celeter.github.io/SourceGo/book_source/all.json'>https://celeter.github.io/SourceGo/book_source/all.json</a>
- 更新日期：{time_format(get_timestamp())}
- 本站书源整理者：`Celeter`

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
    with open(os.path.join(work_space, '..', 'README.md'), 'w', encoding='utf-8') as f:
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
      <li><span>复制下面链接，在阅读里<code>网络导入</code>。</span></li>
      <li><a href='yuedu://booksource/importonline?src=https://celeter.github.io/SourceGo/book_source/all.json'>https://celeter.github.io/SourceGo/book_source/all.json</a></li>
      <li><span>更新日期：{time_format(get_timestamp())}</span></li>
      <li><span>本站书源整理者：</span><code>Celeter</code></li>
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
      <p><span>复制“书源链接”，打开阅读，点击右下角“我的”，然后选择“书源管理”，点击右上角三个点，选择“网络导入”，粘贴链接，确定即可。</span></p>
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
    with open(os.path.join(work_space, '..', 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)


if __name__ == '__main__':
    import_file = os.path.join(work_space, '..', '.history', 'xyz0.json')
    if os.path.exists(import_file):
        source_list = json.loads(read_file(import_file))
        json_group(source_list)

    folder_list = get_folder_list()
    for f in folder_list:
        save_file_group(f)

    update_readme()

    # 保存源长度至环境变量
    # os.system('echo "::set-env name=SRC_LEN::{}"'.format(1))
