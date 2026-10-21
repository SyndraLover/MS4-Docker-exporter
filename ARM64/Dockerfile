FROM debian:trixie-slim@sha256:a66b19aa552f595b4ab276c6b4f9b24fa4546632c5ecd88cccdced4a6866323a
LABEL org.opencontainers.image.description="Musescore-Exporter"
LABEL org.opencontainers.image.source=https://github.com/SyndraLover/MS4-Docker-exporter
LABEL org.opencontainers.image.description="Exports Musescore Compositions to MP3/PDF/MXL inside of a docker container"
LABEL org.opencontainers.image.licenses=CC-BY-NC-SA-4.0

RUN apt update -y && apt upgrade -y
RUN apt install wget libgl1-mesa-dev ffmpeg libsm6 libxext6 libfuse2t64 pipewire xvfb python3 -y

RUN wget https://github.com/musescore/MuseScore/releases/download/v4.7.5/MuseScore-Studio-4.7.5.260831071-aarch64.AppImage
RUN wget https://github.com/musescore/MuseScore/releases/download/v4.7.5/checksums.sha256.txt
RUN sha256sum --check --ignore-missing checksums.sha256.txt

RUN chmod +x MuseScore-Studio-4.7.5.260831071-aarch64.AppImage
RUN mkdir /app
ADD MS4_Exporter /app

ADD entrypoint.sh /
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/bin/bash","entrypoint.sh"]