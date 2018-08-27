# repeater_analyzer

基于 qqbot 的Q群复读机分析器。An analyzer of repeaters in QQ groups based on qqbot.

Blog: [idkidknow](https://idkidknow.com/2018/08/27/%E4%B8%8D%E5%8A%A1%E6%AD%A3%E4%B8%9A-%E6%AF%AB%E6%97%A0%E6%8A%80%E6%9C%AF%E5%90%AB%E9%87%8F%E7%9A%84q%E7%BE%A4%E5%A4%8D%E8%AF%BB%E6%9C%BA%E5%88%86%E6%9E%90%E5%99%A8/)

## 如何使用

1. 安装 qqbot: https://github.com/pandolia/qqbot
2. 将 repeater_analyzer.py 放入 ~/.qqbot-tmp/plugins/ 目录
3. 配置 Repeater Analyzer (见章节「配置」)
4. 启动 qqbot 并登录，在其他终端输入 qq plug repeater_analyzer, 提示成功后则本程序开始记录消息
- Q群中发送消息 --list repeaters 查看当前的复读机名称及其复读次数
- Q群中发送消息 --list sentences 查看已被复读的语录及其被复读次数
- Q群中发送消息 --clean 清空已有数据 (默认只有自己可以使用)

## 配置

1. 使用任意文本编辑器打开 repeater_analzyer.py
2. 修改 _permitted_names 中的 TheGroupName 为你所要分析的群名称，**确保该群名称在你加入的所有群中唯一**
3. (可选)在 _admin_names 中加入群成员的名字，使该成员也拥有执行 --clean 的权限。然而由于 smartqq 的无力性，任何人都可以通过更换同名群名片的方式获得该权限，**因此不推荐使用**
4. (可选)对过滤器 message_filter 进行编程，对于不需要进行分析的消息返回 True
