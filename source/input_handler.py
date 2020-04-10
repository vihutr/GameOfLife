import tcod as libtcod

def handle_keys(key):
        key_char = chr(key.c)

        # Movement keys
        if key.vk == libtcod.KEY_UP:
            return {'move': (0, -1)}
        elif key.vk == libtcod.KEY_DOWN:
            return {'move': (0, 1)}
        elif key.vk == libtcod.KEY_LEFT:
            return {'move': (-1, 0)}
        elif key.vk == libtcod.KEY_RIGHT:
            return {'move': (1, 0)}
        elif key_char == 'w':
            return {'move': (0, -1)}
        elif key_char == 's':
            return {'move': (0, 1)}
        elif key_char == 'a':
            return {'move': (-1, 0)}
        elif key_char == 'd':
            return {'move': (1, 0)}

        if key.vk == libtcod.KEY_SPACE:
            return {'next': True}

        if key.vk == libtcod.KEY_ENTER and (key.lalt or key.ralt):
            # Alt+Enter: toggle full screen
            return {'fullscreen': True}
        elif key.vk == libtcod.KEY_ESCAPE:
            # Exit the game
            return {'exit': True}
                
        # No key was pressed
        return {}