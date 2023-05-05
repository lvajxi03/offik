package main

import (
	"github.com/hajimehoshi/ebiten/v2"
	"github.com/lvajxi03/offik/arena"
	"github.com/lvajxi03/offik/core"
	"math/rand"
	"os"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())
	arena.Init()
	ebiten.SetWindowSize(core.ARENA_WIDTH, core.ARENA_HEIGHT)
	ebiten.SetWindowTitle(core.APP_TITLE)
	ebiten.SetWindowDecorated(false)
	ebiten.SetFullscreen(true)
	app := arena.NewArena()

	if err := ebiten.RunGame(app); err != nil {
		os.Exit(0)
	}
}
