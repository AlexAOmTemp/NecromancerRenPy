init python:

    def init_items_list():
        return (set ([x['name'] for x in item_list]) )

    logging ("items")
    items_by_names = init_items_list()
    # for id, val in enumerate(items_by_names):
    #     logging ("%d %s"%(id, val))
