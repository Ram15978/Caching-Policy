### Git Note

本文件记录有关git的所有使用过的命令和报错解决方法

#### 查看已暂存的更改

```shell
git diff --cached
```

#### 如何删除git所有提交历史，如何在不删除本地仓库文件的情况下删除远程仓库文件

https://www.cnblogs.com/raiuny/p/15856085.html

#### 版本回退

> https://zhuanlan.zhihu.com/p/56843134
>
> https://blog.csdn.net/fareast_mzh/article/details/93709734

##### 本地分支版本回退

回退到上一版本

```shell
git reset --hard HEAD^ 
```

回退到n次提交之前（3代表往前回退3个版本）

```shell
git reset --hard HEAD~3
```

回退到指定版本（0bfafd就是你要回退的版本的commit id的前面几位）

```shell
git reflog
git reset --hard Obfafd
```

##### 远程分支版本回退

在本地分支版本回退之后，紧接着强制推送到远程分支

```shell
git push -f
```

#### 列出本地仓库跟踪的所有文件

```shell
git ls-files
```

#### 撤销commit

##### 不改动工作区间的代码

```shell
git reset --soft HEAD^
```

##### 改动工作区间的代码

```shell
git reset --hard HEAD^
```

#### 查看commit信息

```shell
git log
```

#### 查看add信息

```shell
git status 
```

#### 查看修改

```shell
git log
git show commitId
git show commitId --stat 查看详细文件列表
```

#### `git diff`

1. 查看已暂存文件与上次提交的差异

```shell
git diff --cached
```

2. 查看还未暂存（未执行git add）的文件的差异

```shell
git diff
```

3. 比较上一次提交（HEAD^表示上一次提交的引用）和当前HEAD的状态（也就是最近一次提交的状态）

```shell
git diff HEAD^ HEAD
```

#### 修改用户名和邮箱
```shell
git config --global user.name <username>
git config --global user.email <email>
```

#### `git push`报错

##### fatal: unable to access 'https://github.com/Ram15978/Caching-Policy.git/': Failed to connect to github.com port 443: Connection refused

关闭VPN

```shell
git config --global --unset http.proxy
git config --global --unset https.proxy
```

##### Failed to connect to github.com port 443: Connection refused

https://blog.csdn.net/weixin_44442186/article/details/124979085

##### Total 608 (delta 342), reused 0 (delta 0), pack-reused 0 error: RPC failed； HTTP 401 curl 22 The req

```c++
git config --global credential.helper store
git push -u origin master
```

#### 更新gitignore后如何使其生效

```shell
git rm -r --cached . // 删除本地缓存
git add . // 添加要提交的文件
git commit -m 'update .gitignore' // 更新本地的缓存
```

#### open错误码

https://blog.csdn.net/qq_33907392/article/details/105725454
