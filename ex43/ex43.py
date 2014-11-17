class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
        print scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('2')


        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class FristLevel(object):

    def enter(self):
	pass

class SecondLevel(object):

    def enter(self):
	pass

class Map(object):

    scenes = {'1' : FristLevel(),
    '2' : SecondLevel()}
    print scenes

    def __init__(self, start_scene):
    	self.start_scene = start_scene



    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('1')
a_game = Engine(a_map)
a_game.play()