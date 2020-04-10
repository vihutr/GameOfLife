import tcod as libtcod

from input_handler import handle_keys
from life import Life


def main():

    grid = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1],
            [1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1],
            [1,1,1,1,1,1,2,2,1,1,1,2,2,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,2,2,2,1,1,2,2,1,2,2,1,1,2,2,2,1,1],
            [1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1],
            [1,1,1,1,1,1,2,2,1,1,1,2,2,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,2,2,1,1,1,2,2,1,1,1,1,1,1],
            [1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1],
            [1,1,2,2,2,1,1,2,2,1,2,2,1,1,2,2,2,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,2,2,1,1,1,2,2,1,1,1,1,1,1],
            [1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1],
            [1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]

    screen_height = 17
    screen_width = 19
    rows = 17
    columns = 19
    window_title = "Conaway's Game of Life in Python w/ tcod"

    libtcod.console_set_custom_font('./textures/terminal8x8_gs_asx4.png', libtcod.FONT_LAYOUT_ASCII_INROW)
    libtcod.console_init_root(screen_width, screen_height, window_title, False)

    # map dead symbol to 1 and live symbol to 2
    libtcod.console_map_ascii_codes_to_font(1, 2, 1, 0)
    con = libtcod.console_new(screen_width, screen_height)
    #libtcod.console_set_default_background(con, libtcod.black)

    key = libtcod.Key()
    mouse = libtcod.Mouse()
    cursor = True

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        render_all(con, cursor, grid, rows, columns)
        libtcod.console_flush()
        action = handle_keys(key)

        move = action.get('move')
        next = action.get('next')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            # add moving highlight char here
            pass

        if next:
            Life(grid, rows, columns)
            pass

        if exit:
            return True
        
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen)

def render_all(con, cursor, grid, rows, columns):
    for x in range(columns):
        for y in range(rows):
            if(int(grid[y][x]) == 1):
                libtcod.console_set_default_foreground(0, libtcod.white)
                libtcod.console_put_char(0, x, y, 1, libtcod.BKGND_NONE)
            elif(int(grid[y][x]) == 2):
                libtcod.console_set_default_foreground(0, libtcod.white)
                libtcod.console_put_char(0, x, y, 2, libtcod.BKGND_NONE)
                
if __name__ == '__main__':
    main()