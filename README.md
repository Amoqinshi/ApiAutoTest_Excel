# 持续集成的配置
## 一、Jenkins和Docker的安装
Dcoker桌面版安装：
https://www.runoob.com/docker/macos-docker-install.html

Docker版本的Jenkins镜像：
https://hub.docker.com/r/jenkins/jenkins

复制以下命令：
docker pull jenkins/jenkins:lts-jdk11

在终端执行一下命令，进行镜像文件安装：
docker pull jenkins/jenkins:lts-jdk11

加快docker镜像拉取速度
{
  "debug": true,
  "experimental": false,
  "registry-mirrors": [
    "https://e29lwva9.mirror.aliyuncs.com"
  ]
}
![image](https://user-images.githubusercontent.com/87304560/168244983-483e784e-5686-4e6b-bcc3-10e01531eba6.png)

启动命令：
docker run -d -p 80:8080 -p 50000:50000 -v jenkins:/var/jenkins_home -v /etc/localtime:/etc/localtime --name jenkins docker.io/jenkins/jenkins:lts

访问Jenkins：
localhost：80

## 二、Jenkins插件的配置
