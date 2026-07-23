FROM ubuntu:26.04@sha256:7c2884fd32770fc6c173b78e0dc2278a2851d89f5447919edbc45475ac55dd6a

RUN apt update -y && apt upgrade -y
RUN apt install wget libgl1-mesa-dev ffmpeg libsm6 libxext6 libfuse2t64 pipewire xvfb python3 -y

RUN wget https://github.com/musescore/MuseScore/releases/download/v4.7.4/MuseScore-Studio-4.7.4.260706075-x86_64.AppImage
RUN wget https://github.com/musescore/MuseScore/releases/download/v4.7.4/checksums.sha256.txt
RUN sha256sum --check --ignore-missing checksums.sha256.txt

RUN chmod +x MuseScore-Studio-4.7.4.260706075-x86_64.AppImage
RUN mkdir /app
ADD MS4_Exporter /app

ADD entrypoint.sh /
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/bin/bash","entrypoint.sh"]