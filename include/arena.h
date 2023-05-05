#ifndef __ARENA_H__
#define __ARENA_H__

#include "defs.h"
#include "types.h"

Arena *arena_new();

void arena_close(Arena *a);

#endif /* __ARENA_H__ */
