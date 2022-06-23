from todolist.item import Item


def test_id_1():
    """Should be created id"""
    inst = Item()
    assert inst.id != ''
def test_id_2():
    """id should be uniq for all instances"""
    inst1 = Item()
    inst2 = Item()
    assert inst1.id != inst2.id

def test_title_1():
    """title should be empty when item is created"""
    inst = Item()
    assert inst.title == ''
def test_title_1():
    """item should be available  to change title"""
    inst = Item()
    title_text = 'titleText'
    inst.title = title_text
    assert inst.title == title_text

def test_status_1():
    """status should be unselected when item is created"""
    inst = Item()
    assert inst.status == False
def test_status_2():
    """item should be available to get selected or unselected state"""
    inst = Item()
    inst.setItemSelected()
    assert inst.status == True

    inst.setItemUnSelected()
    assert inst.status == False