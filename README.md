# Evan_Li_IDS706_Hwk15

	docker buildx create --use &&\
	docker buildx build --platform linux/amd64,linux/arm64 \
	-t bionicotaku/ids706_individual --push .

当你使用 --platform linux/amd64,linux/arm64 参数时:
Docker buildx 会自动为指定的每个平台构建镜像
所有架构的镜像会被打上相同的标签 (在这里是 bionicotaku/ids706_individual)
Docker Hub 会将它们作为同一个镜像的不同架构版本存储
当用户拉取镜像时，Docker 会自动选择匹配其系统架构的版本
你可以在 Docker Hub 上看到这个镜像支持多个架构。比如在网页界面上会显示:
linux/amd64
linux/arm64
当其他人使用 docker pull bionicotaku/ids706_individual 时:
在 Intel/AMD 处理器的机器上会自动拉取 amd64 版本
在 ARM 处理器(如 M1/M2 Mac)上会自动拉取 arm64 版本