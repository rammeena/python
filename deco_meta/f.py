#f.py
# coding: utf-8
""" A descriptor works only in class.

Storing attributes data directly in descriptor
means sharing between instances.
"""
class DescriptorClassStorage:
    """Descriptor storing data in class"""
    def __init__(self, default=None):
        self.value = default

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value


if __name__ == '__main__':
    class StoreClass:
        """All instances will share attr"""
        attr = DescriptorClassStorage(10)

    store1 = StoreClass()
    store2 = StoreClass()
    print('store1', store1.attr)
    print('store2', store2.attr)
    print('Setting store1 only.')
    store1.attr = 100
    print('store1', store1.attr)
    print('store2', store2.attr)

