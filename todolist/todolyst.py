from todolist.item import Item


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

        return None

    def update_item(self):
        pass

    def get_all_items(self):
        return self.__store
