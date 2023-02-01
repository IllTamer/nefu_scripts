# NEFU-SCRIPTS

> LICENSE: AGPLv3

## About

本项目旨在实现一些便于同学们使用的操作，如：访问课表，快速抢课等。同时作为练习项目，与大家分享。

本项目中使用的其他开源库如下：

- Django
- imgkit

### 管理账户

项目自带默认管理员账号

- admin
- 123456

> 您也可以使用 `python manage.py createsuperuser` 命令创建系统管理员，或访问 `http://127.0.0.1:8000/admin/auth/user/` 手动创建。

## Thanks for

- [论如何优雅的将自己的服务接入学校的 CAS 统一认证系统](https://cloud.tencent.com/developer/article/2141155)

## Q & A

- 使用时出现 `no wkhtmltoimage executable found: "command not found"`

    安装 [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) 工具包

- 使用时出现 `error while loading shared libraries: libssl.so.1.1`

    安装 openssl-1.1