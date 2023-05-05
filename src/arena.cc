#include "types.h"
#include "arena.h"

Arena *arena_new() {
  Arena *a = (Arena *)malloc(sizeof(Arena));
  a->window = SDL_CreateWindow(APP_TITLE,
                                SDL_WINDOWPOS_CENTERED,
                                SDL_WINDOWPOS_CENTERED,
                                ARENA_WIDTH,
                                ARENA_HEIGHT,
                                SDL_WINDOW_SHOWN
                                );

  if (a->window == NULL) {
    free(a);
    a = NULL;
  } else {
    a->canvas = SDL_GetWindowSurface(a->window);
    if (a->canvas == NULL) {
      SDL_DestroyWindow(a->window);
      free(a);
      a = NULL;
    } else {
      SDL_Surface *image = IMG_Load("assets/images/default-bg.png");
      a->background = SDL_ConvertSurface(image, a->canvas->format, 0);
      if (a->background == NULL) {
        fprintf(stderr, "Error loading background\n");
      }
      SDL_FreeSurface(image);
      SDL_BlitSurface(a->background, NULL, a->canvas, NULL);
      SDL_UpdateWindowSurface(a->window);
      // TODO:
      SDL_SetWindowFullscreen(a->window, SDL_WINDOW_FULLSCREEN);
    }
  }
  return a;
}

void arena_close(Arena *a) {
  SDL_FreeSurface(a->canvas);
  SDL_FreeSurface(a->background);
  SDL_DestroyWindow(a->window);
  free(a);
  SDL_Quit();
}
