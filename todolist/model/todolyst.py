from todolist.model.item import Item


class TodoList():
    __store = []

    def create_item(self):
        inst = Item()
        self.__store.append(Item())
        return inst.id

    def get_item_by_id(self, uniq_id):
        for item in self.get_all_items():
            if item.id == uniq_id:
                return item

    def delete_item_by_id(self, uniq_id):
        item_in_store = self.get_item_by_id(uniq_id)

        if item_in_store in self.__store:
            self.__store.remove(item_in_store)
            return id

    def update_item(self, uniq_id, updated_item):
        new_store = []
        updated_item_id = False

        for item in self.__store:
            if item.id == uniq_id:
                new_store.append(updated_item)
                updated_item_id = True
            new_store.append(item)

        self.__store = new_store

        return updated_item_id

    def get_all_items(self):
        return self.__store
