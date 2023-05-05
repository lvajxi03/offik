CC := g++
CFLAGS := -std=c++11 -Iinclude
CPPFLAGS :=
LDFLAGS := -lSDL2 -lSDL2_image -lSDL2_ttf

OBJS := obj/main.o obj/arena.o
TARGET := offik

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) -o $@ $? $(LDFLAGS)

obj/%.o: src/%.cc obj
	$(CC) -c $< -o $@ $(CFLAGS)

obj:
	mkdir -p obj

.phony: clean

clean:
	rm -rf obj $(TARGET)
