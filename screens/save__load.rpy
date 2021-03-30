# screen file_picker:
#     #add "img/menu/gmenu2.jpg"
#     use navigation
#     frame:
#         style "file_picker_frame"
#
#         has vbox
#
#         $ columns = 2
#         $ rows = 2
#
#         # Display a grid of file slots.
#         grid columns rows:
#             transpose True
#             xfill True
#             style_group "file_picker"
#
#             # Display ten file slots, numbered 1 - 10.
#             for i in range(1, columns * rows + 1):
#
#                 # Each file slot is a button.
#                 button:
#                     action FileAction(i)
#                     xfill True
#
#                     has hbox
#
#                     # Add the screenshot.
#                     add FileScreenshot(i)
#
#                     $ file_name = FileSlotName(i, columns * rows)
#                     $ file_time = FileTime(i, empty=_("Empty Slot."))
#                     $ save_name = FileSaveName(i)
#
#                     text "[file_name]. [file_time!t]\n[save_name!t]"
#
#                     key "save_delete" action FileDelete(i)
#
#
# screen navigation():
#
#     # The background of the game menu.
#     window:
#         style "gm_root"
#
#     # The various buttons.
#     frame:
#         style_group "gm_nav"
#         xalign .98
#         yalign .98
#
#         has vbox
#
#         textbutton _("Return") action Return()
#         textbutton _("Preferences") action ShowMenu("preferences")
#         textbutton _("Save Game") action ShowMenu("save")
#         textbutton _("Load Game") action ShowMenu("load")
#         textbutton _("Main Menu") action MainMenu()
#         textbutton _("Help") action Help()
#         textbutton _("Quit") action Quit()
#
# init -2:
#
#     # Make all game menu navigation buttons the same size.
#     style gm_nav_button:
#         size_group "gm_nav"
#
# screen main_menu():
#
#     # This ensures that any other menu screen is replaced.
#     tag menu
#     background "main_menu_image"
#     # The background of the main menu.
#     window:
#         style "mm_root"
#
#     # The main menu buttons.
#     frame:
#         style_group "mm"
#         xalign .98
#         yalign .98
#
#         has vbox
#
#         textbutton _("Start Game") action Start()
#         textbutton _("Load Game") action ShowMenu("load")
#         textbutton _("Preferences") action ShowMenu("preferences")
#         textbutton _("Help") action Help()
#         textbutton _("Quit") action Quit(confirm=False)
#
# init -2:
#
#     # Make all the main menu buttons be the same size.
#     style mm_button:
#         size_group "mm"
#
#
#
#
# screen save:
#
#     # This ensures that any other menu screen is replaced.
#     tag menu
#
#     use navigation
#     use file_picker
#
# screen load:
#
#     # This ensures that any other menu screen is replaced.
#     tag menu
#
#     use navigation
#     use file_picker

# screen file_picker():
#
#     frame:
#         xalign 0.5
#         yalign 0.5
#         has vbox
#
#         $ columns = 1
#         $ rows = 6
#
#         grid columns rows:
#
#
#             for i in range(1, columns * rows + 1):
#                 button:
#                     action FileAction(i),logging( "%s" %renpy.current_screen())
#
#                     has hbox
#                     $ file_name = FileSlotName(i, columns * rows)
#                     $ file_time = FileTime(i, empty=_("Empty Slot."))
#                     $ save_name = FileSaveName(i)
#
#                     if save_name:
#                         text "[save_name!t]:  [file_time!t] "
#                     else:
#                         text "[file_time!t] "
#                     key "save_delete" action FileDelete(i)
#


# screen save():
#
#     # This ensures that any other menu screen is replaced.
#     tag menu
#
#     use navigation
#     use file_picker
#
# screen load():
#
#     # This ensures that any other menu screen is replaced.
#     tag menu
#
#     use navigation
#     use file_picker
