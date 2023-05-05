#include "main.h"

#include <stdio.h>

bool init() {
  bool result = true;
  if (SDL_Init(SDL_INIT_VIDEO) < 0) {
    result = false;
  } else {
    if (!IMG_Init(IMG_INIT_PNG) & IMG_INIT_PNG) {
      result = false;
    }
  }
  return result;
}

void event_loop(Arena *a) {
  Uint32 waittime = 1000.0f/FPS;
  Uint32 framestart = 0;
  Sint32 delaytime;
  SDL_Event event;
  bool done = false;
  while ((!done) && (SDL_WaitEvent(&event))) {
    switch (event.type) {
    case SDL_QUIT:
      done = true;
      break;
    default:
      break;
    }
    if (!done) {
      delaytime = waittime - (SDL_GetTicks() - framestart);
      if (delaytime > 0) {
        SDL_Delay((Uint32)delaytime);
      }
    }
  }
}

int main(int argc, char **argv) {
  int result = ERROR_SUCCESS;
  if (!init()) {
    result = ERROR_FAILURE;
    fprintf(stderr, "Error initializing SDL2\n");
  }
  Arena *a = arena_new();
  event_loop(a);
  arena_close(a);
  return result;
}
