FROM ubuntu:24.04
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential scons pkg-config libx11-dev libxcursor-dev libxinerama-dev libgl1-mesa-dev libglu1-mesa-dev libasound2-dev libpulse-dev libudev-dev libxi-dev libxrandr-dev libwayland-dev 'software-properties-common' git

RUN apt-add-repository 'ppa:dotnet/backports'
RUN apt-get install -y 'dotnet-sdk-9.0'

RUN dotnet workload install wasm-tools

WORKDIR /opt
RUN git clone 'https://github.com/emscripten-core/emsdk.git'
WORKDIR /opt/emsdk
RUN ./emsdk install 3.1.56
RUN ./emsdk activate 3.1.56
ENV PATH="/opt/emsdk/emsdk:/opt/emsdk/node/22.16.0_64bit/bin:/opt/emsdk/upstream/emscripten:$PATH"

WORKDIR /
RUN git clone 'https://github.com/Quadtree/godot.git' && cd /godot && git checkout '136da1c54cc895d8276f4bef620bcab29cf388e0'

WORKDIR /godot
RUN scons platform=linuxbsd tools=yes module_mono_enabled=yes
RUN "bin/godot.linuxbsd.editor.x86_64.mono" '--headless' '--generate-mono-glue' 'modules/mono/glue'

RUN 'modules/mono/build_scripts/build_assemblies.py' '--godot-output-dir=bin' '--push-nupkgs-local' "/var/lib/local/godot_nuget"
RUN scons platform=linuxbsd tools=yes module_mono_enabled=yes mono_glue=yes

WORKDIR /godot
RUN scons tools=no platform=web module_mono_enabled=yes module_regex_enabled=yes target=template_debug threads=no
RUN scons tools=no platform=web module_mono_enabled=yes module_regex_enabled=yes target=template_release threads=no

ADD export_presets.cfg /usr/local/etc/export_presets.cfg
