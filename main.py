import pyxel

WIDTH, HEIGHT = 128, 128
TRANSPARENT_COLOR = 12
SCENE_TITLE = 0
SCENE_GAME = 1
SCENE_RESULT = 2

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT)
        pyxel.load("./scene.pyxres")
        self.scene = SCENE_GAME
        self.game_settings()

    def game_settings(self):
        pyxel.run(self.update, self.draw)

    def update_title_scene(self):
        pass

    def update_game_scene(self):
        pass

    def update_result(self):
        pass

    def update(self):
        if self.scene == SCENE_TITLE:
            self.update_title_scene()
        elif self.scene == SCENE_GAME:
            self.update_game_scene()
        elif self.scene == SCENE_RESULT:
            self.update_result()

    def draw_title_scene(self):
        pass

    def draw_game_scene(self):
        pyxel.bltm(0, 0, 0, 0, 0, WIDTH, HEIGHT)

    def draw_result(self):
        pass

    def draw(self):
        pyxel.cls(0)
        if self.scene == SCENE_TITLE:
            self.draw_title_scene()
        elif self.scene == SCENE_GAME:
            self.draw_game_scene()
        elif self.scene == SCENE_RESULT:
            self.draw_result()

App()