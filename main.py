import pyxel

WIDTH, HEIGHT = 128, 128
TRANSPARENT_COLOR = 12
SCENE_TITLE = 0
SCENE_GAME = 1
SCENE_RESULT = 2
BOY_STATUS_LIVE = 0
BOY_STATUS_DEAD = 1


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT)
        pyxel.load("./scene.pyxres")
        self.scene = SCENE_GAME
        # BGM
        pyxel.sounds[0].set(
            "e3 e3 e3 c3 e3 g3 g2 "
            "c3 g2 e2 a2 b2 a#2 a2 g2 e3 g3 a3 f3 g3 e3 c3 d3 b2 ",
            "p",
            "6",
            "vffn fnff vffs vfnn",
            25,
        )
        pyxel.sounds[1].set(
            "c3 c4 a2 a3 a#2 a3 g2 e3 g3 a3 f3 g3 e3 c3 d3 b2 "
            "c3 g2 e2 a2 b2 a#2 a2 g2 e3 g3 a3 f3 g3 e3 c3 d3 b2 ",
            "s",
            "6",
            "nnff vfff vvvv vfff svff vfff vvvv svnn",
            25,
        )
        pyxel.sounds[2].set(
            "f0ra4r f0ra4r f0ra4r f0f0a4r", "n", "6622 6622 6622 6422", "f", 25
        )
        # コイン獲得時の効果音
        pyxel.sounds[3].set("c3e3g3e4g4", "t", "6", "f", 5)
        # ゲームオーバー時の効果音
        pyxel.sounds[4].set("g2f2e2d2c2", "t", "76543", "fffnn", 10)
        # 成功時の効果音
        pyxel.sounds[5].set("c3e3g3c4e4", "p", "66443", "nnffn", 10)
        # 失敗時の効果音
        pyxel.sounds[6].set("g2f2e2d2c2", "t", "76543", "fffnn", 10)
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
