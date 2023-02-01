# API

> Notice: 所有的 API 路径均以 `/api` 为前缀

## register

注册用户

> GET `/register`

- username
- password

## login

登录用户

> GET `/login`

- username

## user

### 默认 / 指定 用户身份

- 如不指定`user_id`，可以`/user`前缀访问服务。当服务器内登录有多个 user 时将自动选取时间最近的登录用户作为执行身份

- 如需指定用户身份，在访问服务时在地址中携带参数`user_id`即可
