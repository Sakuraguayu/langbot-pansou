# LangBot pansou

网盘资源搜索的LangBot插件,new!


## 使用方法

本插件使用docker部署，其中`docker-compose.yml`文件中包含了插件的配置项，用户可以根据自己的需求进行修改

更多详细内容参考官方盘搜API：[https://github.com/sheetung/pansou](https://github.com/sheetung/pansou)

```bash
# 下载配置文件
curl -o docker-compose.yml  https://raw.githubusercontent.com/fish2018/pansou/refs/heads/main/docker-compose.yml

# 启动服务
docker-compose up -d

# 访问服务
http://localhost:8888
```

配置页面选择相关配置，自行调试最快的请求渠道

私聊中输入关键词触发，触发方式：

盘搜<关键词>

例如：搜蜡笔小新

![](./assets/cfg1.png)

## 规划


## 问题反馈及功能开发

[![QQ群](https://img.shields.io/badge/QQ群-965312424-green)](https://qm.qq.com/cgi-bin/qm/qr?k=en97YqjfYaLpebd9Nn8gbSvxVrGdIXy2&jump_from=webapi&authKey=41BmkEjbGeJ81jJNdv7Bf5EDlmW8EHZeH7/nktkXYdLGpZ3ISOS7Ur4MKWXC7xIx)