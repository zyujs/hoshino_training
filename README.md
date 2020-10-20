# hoshino_training  

Hoshino调教助手

这是一个满足个人奇怪需求的HoshinoBot插件, 作用是在不破坏星乃??的前提下让星乃的??变成主人的形状.(?????)

说人话: 在不对hoshino文件进行任何修改的情况下, 使用反射特性热替换相关函数, 实现对hoshino某些功能的定制.

本项目地址 https://github.com/zyujs/hoshino_training

## 目前实现的修改

- 移除抽卡禁言

  移除来一井抽卡后的禁言

- rank图快捷修改

  将最新rank图以 `rXX-X-服务器.png` 格式放入 `HoshinoBot\res\img\priconne\quick`文件夹中, 不需要重启hoshino, rank系列命令即可输出最新rank图.

- comic模块下载功能增强

  可以为comic模块的检查更新和漫画下载设置超时时间和代理, 避免满屏幕的comic.py报错刷屏, 详见 `functions/comic.py` 内注释.

## 安装方法

1. 在HoshinoBot的插件目录modules下clone本项目 `git clone https://github.com/zyujs/hoshino_training.git`
1. 在 `config/__bot__.py`的模块列表里加入 `hoshino_training`
1. 重启HoshinoBot

## 许可

本插件以AGPL-v3协议开源
