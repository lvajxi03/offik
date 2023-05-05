#ifndef __TYPES_H__
#define __TYPES_H__

#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>

typedef struct {
  SDL_Window *window;
  SDL_Surface *canvas;
  SDL_Surface *background;

} Arena;

#endif /* __TYPES_H__ */
