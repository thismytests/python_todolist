from todolist.todolyst import TodoList


def test_create_item():
    """Should create item in store"""
    inst = TodoList()
    assert len(inst.get_all_items()) == 0

    inst.create_item()
    print(inst.get_all_items())
    assert len(inst.get_all_items()) == 1


def test_create_item_1():
    """Should return id of created item"""
    inst = TodoList()
    id = inst.create_item()
    assert id != 0


def test_get_item_by_id_positive():
    """Should return item from store by id"""
    inst = TodoList()
    created_item_id = inst.create_item()
    result = inst.get_all_items()
    assert len(result) == 1

    found_item_by_id = inst.get_item_by_id(created_item_id)
    assert created_item_id == found_item_by_id.id


def test_delete_item_positive():
    """Should delete item if it exists in the store"""
    inst = TodoList()
    item_id = inst.create_item()
    assert len(inst.get_all_items()) == 1
    deleted_id = inst.delete_item_by_id(item_id)
    assert len(inst.get_all_items()) == 0
    assert deleted_id is not None


def test_delete_item_negative():
    """Should return None if item with id doesn't exist in the store"""
    inst = TodoList()
    inst.create_item()
    some_not_exist_id = 'some_not_exist_id'
    assert len(inst.get_all_items()) == 1
    deleted_id = inst.delete_item_by_id(some_not_exist_id)
    assert len(inst.get_all_items()) == 1
    assert deleted_id is None
