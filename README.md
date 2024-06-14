# 国家电网

集成国家电网每日用电等数据，支持多户号，阶梯用电。

## 安装/更新

#### 方法 1: 通过`Samba`或`SFTP`手动安装

下载并复制`custom_components/state_gird`文件夹到 Home Assistant 根目录下的`custom_components`文件夹

#### 方法 2: 通过`SSH`或`Terminal & SSH`加载项执行一键安装命令

```shell
curl -fsSL get.hassbox.cn/state_grid | bash
```

#### 方法 3: 通过`shell_command`服务

1. 复制下面的代码到 Home Assistant 配置文件`configuration.yaml`

   ```yaml
   shell_command:
     install_state_grid: |-
       curl -fsSL get.hassbox.cn/state_grid | bash
   ```

2. 重启 Home Assistant

3. 在 Home Assistant 开发者工具中调用此服务[`service: shell_command.install_state_grid`](https://my.home-assistant.io/redirect/developer_call_service/?service=shell_command.install_state_grid)
