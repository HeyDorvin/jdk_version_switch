# Windows一键切换JDK版本

## 使用说明

如果要切换的`JDK`版本下存在`JRE`路径，则一同进行切换。

- 修改`jdk_dir`变量

  例如`Java8`对应的JDK目录为`D:\Program Files\Java\jdk1.8.0_333`，`Java18`对应的JDK目录为`D:\Program Files\Java\jdk18.0.2`，`jdk_dir`做如下配置：

  ```python
  jdk_dir = {
      'java8': 'D:\\Program Files\\Java\\jdk1.8.0_333\\',
      'java18': 'D:\\Program Files\\Java\\jdk18.0.2'
  }
  ```

- **以管理员身份执行**

  ```
  python main.py
  ```

## 自动化脚本

这里我使用了`conda`，以下命令仅供参考。

```shell
cmd /k "conda activate common && d: && python D:\PycharmProjects\java_version_switch\main.py"
```

## 修改后不生效

- 重新启动命令行

- 查看是否还有其他的环境变量

  ```shell
  where java
  ```

  如果还有其他版本的`JDK`，删除即可。

