TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt

QMAKE_CFLAGS -=
QMAKE_CFLAGS += -pthread
QMAKE_CXXFLAGS -=
QMAKE_CXXFLAGS += -pthread -std=c++0x
QMAKE_LFLAGS -= -Wl,-O1,--sort-common,--as-needed,-z,relro
QMAKE_LFLAGS += -pthread

QMAKE_CFLAGS_RELEASE -= -O2 -march=x86-64 -mtune=generic -fstack-protector --param=ssp-buffer-size=4
QMAKE_CFLAGS_RELEASE += -O3 -march=native -flto -fuse-linker-plugin -DNDEBUG
QMAKE_CXXFLAGS_RELEASE -= -O2 -march=x86-64 -mtune=generic -fstack-protector --param=ssp-buffer-size=4
QMAKE_CXXFLAGS_RELEASE += -O3 -march=native -flto -fuse-linker-plugin -DNDEBUG
QMAKE_LFLAGS_RELEASE -= -Wl,-O1
QMAKE_LFLAGS_RELEASE += -Wl,-O3 -O3 -march=native -flto -fuse-linker-plugin

pg {
	QMAKE_CFLAGS += -pg
	QMAKE_CXXFLAGS += -pg
	QMAKE_LFLAGS += -pg
}

SOURCES += main.cpp \
	2048.cpp \
	Minimax.cpp \
	JS_Minimax.cpp

HEADERS += \
	2048.h \
	Minimax.h

