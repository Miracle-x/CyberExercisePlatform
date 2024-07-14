# Cyber Exercise Platform

This is a cyber exercise platform built with FastAPI.

在使用本项目之前，你需要安装这三个工具在本地部署 Kubernetes 集群：[Docker](https://docs.docker.com/desktop/install/linux-install/), [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/), [kind](https://kind.sigs.k8s.io/docs/user/quick-start/)

确保你的 config/config.yaml 文件中的 kubernetes 配置指向正确的 kubeconfig 文件路径

# Roadmap

1. 基于模版的环境创建与删除
   1. 使用Kubernetes的命名空间隔离不同训练环境，确保资源和网络的独立性（已完成）
   2. 删除训练环境（已完成）
   3. 基于模版创建计算资源
   4. 基于模版创建网络拓扑
   5. 基于模版在计算资源上部署服务

2. 环境数据采集
   1. 各设备的各类日志的采集与组织

3. 各资源的细致设置
   1. 接入资源本身具有的管理工具
   
4. 大模型（非系统能力要求）
   1. 基于环境数据的分析与告警
   2. 操作各资源管理工具的安全响应