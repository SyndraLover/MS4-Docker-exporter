FROM ubuntu:26.04@sha256:9c17d26897bad0a168dee2f03da949e26458e1eba3228190ac0022d3513498a2

RUN apt update -y && apt upgrade -y
RUN apt install wget libgl1-mesa-dev ffmpeg libsm6 libxext6 libfuse2t64 pipewire xvfb python3 -y

RUN wget https://github.com/musescore/MuseScore/releases/download/v4.7.4/MuseScore-Studio-4.7.4.260706075-aarch64.AppImage
RUN wget https://github.com/musescore/MuseScore/releases/download/v4.7.4/checksums.sha256.txt
RUN sha256sum --check --ignore-missing checksums.sha256.txt

RUN chmod +x MuseScore-Studio-4.7.4.260706075-aarch64.AppImage
RUN mkdir /app
ADD MS4_Exporter /app

ADD entrypoint.sh /
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/bin/bash","entrypoint.sh"]