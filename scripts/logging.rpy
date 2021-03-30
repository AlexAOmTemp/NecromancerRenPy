
init -6 python:
    import codecs
    def logging (string_to_log):
        with open(renpy.loader.transfn('resources/log.txt'),"a+") as fh:
            print(string_to_log, file=fh)
            fh.close()

    def clear_log ():
        with open(renpy.loader.transfn('resources/log.txt'),"w+") as fh:
            fh.close()

    clear_log()
    logging ("log")
