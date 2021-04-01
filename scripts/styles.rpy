# {color=#f00}Red{/color}, {color=#00ff00}Green{/color}, {color=#0000ffff}Blue{/color}
# Black	 	#000
# White	 	#ffffff
# Medium Gray	#808080
# Aqua	 	#008080
# Navy Blue	#000080
# Green	 	#00ff00
# Orange	 	#ffa500
# Yellow	 	#ffff00
# red         #f00


define gui.text_color = '#000000'
define gui.interface_text_color = '#000000'
define gui.text_font = fonts_list[0]
define gui.interface_text_font = fonts_list[0]

image main_menu_image  = im.FactorScale("gui/main_menu.png", scaling)
image game_menu_image = im.FactorScale("gui/game_menu.png", scaling)
$gui.main_menu_background = main_menu_image
$gui.game_menu_background = main_menu_image
init python:
    gui.text_size = int(40*scaling)
    gui.name_text_size = int(40*scaling)
    gui.interface_text_size = int(40*scaling)
    gui.label_text_size = int(40*scaling)
    gui.notify_text_size = int(40*scaling)
    gui.title_text_size = int(50*scaling)
    gui.choice_button_text_size = int(40*scaling)
    gui.choice_text_size = int(40*scaling)

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120
    # background "gui/overlay/game_menu.png"
    background "game_menu_image"
style main_menu_frame:
    variant "small"
    # background "gui/phone/overlay/main_menu.png"
    background "main_menu_image"
style game_menu_outer_frame:
    variant "small"
    background "main_menu_image"
    # background "gui/phone/overlay/game_menu.png"

# define e = Character("Eileen", kind=nvl)
# define narrator = nvl_narrator
# define gui.nvl_name_xpos = 0.5
# define gui.nvl_text_xpos = 0.5
# define gui.nvl_name_xalign = 0.5
# define gui.nvl_text_xalign = 0.5
# define gui.nvl_thought_xalign = 0.5
# define gui.nvl_name_width = 740
# define gui.nvl_text_width = 740
# define gui.nvl_thought_width = 740

# define gui.nvl_thought_xpos = 0.5
# define menu = nvl_menu
#
# define gui.nvl_borders = Borders(0, 15, 0, 30)
# #The borders around the background of the NVL-mode. Since the background is not a frame, this is only used to pad out the NVL-mode to prevent it from pressing up against the sides of the screen.
#
# define gui.nvl_height = 173
# #The height of a single NVL-mode entry. Setting this to a fixed height makes it possible to have NVL-mode without paging, showing a fixed number of entries at once. Setting this to None allows entries to be of a variable size.
#
# define gui.nvl_spacing = 15
# #The spacing between entries when gui.nvl_height is None, and the spacing between NVL-mode menu buttons.
#
# define gui.nvl_name_xpos = 0.5
# define gui.nvl_text_xpos = 0.5
# define gui.nvl_thought_xpos = 0.5
# #The positioning of character names, dialogue text, and thought/narration text, relative to the left side of the entry. This can be a number of pixels, or 0.5 to represent the center of the entry.
#
# define gui.nvl_name_xalign = 0.5
# define gui.nvl_text_xalign = 0.5
# define gui.nvl_thought_xalign = 0.5
# #The alignment of the text. This controls both the alignment of the text, and the side of the text that is placed at xpos. This can be 0.0 for left, 0.5 for center, and 1.0 for right.
#
# define gui.nvl_name_ypos = 0
# define gui.nvl_text_ypos = 60
# define gui.nvl_thought_ypos = 0
# #The position of character names, dialogue text, and thought/narration text, relative to the top of the entry. This should be a number of pixels from the top.
#
# define gui.nvl_name_width = 740
# define gui.nvl_text_width = 740
# define gui.nvl_thought_width = 740
# #The width of each kind of text, in pixels.
#
# define gui.nvl_button_xpos = 0.5
# define gui.nvl_button_xalign = 0.5
# #The position and alignment of NVL-mode menu buttons.
