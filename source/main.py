import tcod as libtcod
import numpy as np

from input_handler import handle_keys
from messages import *
from life import Life


#int zeroes for custom grid width/height ?
def Init(rows, columns):
    return np.zeros ((rows, columns))

def main():
    generation = 0
    
    grid1 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
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

    # this starting configuration will eventually turn into the loop that is 
    # inherently present in the bottom left quarter of the configuration above
    grid2 = [[1,1,1,1,1,1,1],
            [1,2,2,2,1,2,1],
            [1,2,1,1,1,1,1],
            [1,1,2,2,1,2,1],
            [1,1,1,1,2,2,1],
            [1,2,1,2,1,2,1],
            [1,1,1,1,1,1,1]]

    grid = grid2

    #grid0 = Init()
    
    bottom_space = 3
    
    screen_height = len(grid) + bottom_space
    screen_width = len(grid[0])
    
    rows = len(grid)
    columns = len(grid[0])
    
    message_x = 0
    message_width = screen_width
    message_height = 3
    
    window_title = "Conway's Game of Life in Python w/ tcod"

    libtcod.console_set_custom_font('./textures/terminal8x8_gs_asx4.png', libtcod.FONT_LAYOUT_ASCII_INROW)
    libtcod.console_init_root(screen_width, screen_height, window_title, False)

    # map dead symbol to 1 and live symbol to 2, heart symbol to 3 as progressing symbol
    libtcod.console_map_ascii_codes_to_font(1, 3, 1, 0)
    con = libtcod.console_new(screen_width, screen_height)
    bottom = libtcod.console_new(screen_width, bottom_space)
    #libtcod.console_set_default_background(con, libtcod.black)

    message_log = MessageLog(message_x, message_width, message_height)
    
    key = libtcod.Key()
    mouse = libtcod.Mouse()
    cursor = True

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE_PRESS, key, mouse)

        render_all(con, bottom, grid, bottom_space, screen_width, screen_height,  rows, columns, mouse, message_log, generation)
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
            generation += 1
            pass

        if exit:
            return True
        
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

def render_all(con, panel, grid, bottom_space, screen_width, screen_height,  rows, columns, mouse, message_log, generation):
    for x in range(columns):
        for y in range(rows):
            if(int(grid[y][x]) == 1):
                libtcod.console_set_default_foreground(0, libtcod.white)
                libtcod.console_put_char(0, x, y, 1, libtcod.BKGND_NONE)
            elif(int(grid[y][x]) == 2):
                libtcod.console_set_default_foreground(0, libtcod.white)
                libtcod.console_put_char(0, x, y, 2, libtcod.BKGND_NONE)
    libtcod.console_set_default_foreground(0, libtcod.red)
    libtcod.console_put_char(0, (columns // 2), (rows + 1), 3, libtcod.BKGND_NONE)
    libtcod.console_set_default_foreground(0, libtcod.red)
    
    genMessage = Message(str(generation))
    message_log.add_message(genMessage)
    
    y = 0
    for message in message_log.messages:
        libtcod.console_set_default_foreground(panel, message.color)
        libtcod.console_print_ex(panel, message_log.x, y, libtcod.BKGND_NONE, libtcod.LEFT, message.text)
        #y += 1
    
    libtcod.console_set_default_foreground(panel, libtcod.light_gray)
    
    libtcod.console_blit(panel, 0, 0, screen_width, 1, 0, 0, (screen_height-bottom_space))
    
    '''
    if(int(grid[mouse.cy][mouse.cx]) == 1):
        libtcod.console_set_default_foreground(0, libtcod.white)
        libtcod.console_put_char(0, x, y, 2, libtcod.BKGND_NONE)
        grid[mouse.cy][mouse.cx] = 2
    elif(int(grid[mouse.cy][mouse.cx]) == 2):
        libtcod.console_set_default_foreground(0, libtcod.white)
        libtcod.console_put_char(0, x, y, 1, libtcod.BKGND_NONE)
        grid[mouse.cy][mouse.cx] = 1
    '''
    
if __name__ == '__main__':
    main()