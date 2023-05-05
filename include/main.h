#ifndef __MAIN_H__
#define __MAIN_H__

#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>

#include "defs.h"
#include "arena.h"

bool init();

int main(int argc, char **argv);

void event_loop(Arena *a);

#endif /* __MAIN_H__ */
