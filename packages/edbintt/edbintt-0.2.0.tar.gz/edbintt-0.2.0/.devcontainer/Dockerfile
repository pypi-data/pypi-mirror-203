FROM python:3.10.6

ARG USERNAME=python
ARG PASSWORD=alskdj
ARG DEBIAN_FRONTEND=noninteractive

USER root

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y \
    ca-certificates \
    curl \
    git \
    gnupg \
    sudo \
    vim && \    
    apt-get clean -y

RUN install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    chmod a+r /etc/apt/keyrings/docker.gpg && \
    echo \
    "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
    "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
    tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && \
    apt-get install -y \
    docker-ce \
    docker-ce-cli \
    containerd.io \
    docker-buildx-plugin \
    docker-compose-plugin && \
    apt-get clean -y


RUN useradd \
    -u 1474 \
    -p $(openssl passwd -1 $PASSWORD) \
    -s /usr/bin/bash \
    --create-home \
    ${USERNAME}

RUN usermod -aG sudo ${USERNAME} && \
    echo "${USERNAME}:${PASSWORD}" | chpasswd

COPY .bashrc /home/${USERNAME}

COPY .ssh /home/${USERNAME}/.ssh
RUN chmod 400 /home/${USERNAME}/.ssh/id*

RUN chown -R ${USERNAME}:${USERNAME} /home/${USERNAME}

USER ${USERNAME}
