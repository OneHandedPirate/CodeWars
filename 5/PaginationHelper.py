# For this exercise you will be strengthening your page-fu mastery. You will
# complete the PaginationHelper class, which is a utility class helpful for
# querying paging information related to an array.
#
# The class is designed to take in an array of values and an integer indicating
# how many items will be allowed per each page. The types of values contained
# within the collection/array are not relevant.
#
# The following are some examples of how this class is used:
#
# helper = PaginationHelper(['a','b','c','d','e','f'], 4)
# helper.page_count() # should == 2
# helper.item_count() # should == 6
# helper.page_item_count(0) # should == 4
# helper.page_item_count(1) # last page - should == 2
# helper.page_item_count(2) # should == -1 since the page is invalid
#
# # page_index takes an item index and returns the page that it belongs on
# helper.page_index(5) # should == 1 (zero based index)
# helper.page_index(2) # should == 0
# helper.page_index(20) # should == -1
# helper.page_index(-10) # should == -1 because negative indexes are invalid


class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self._item_count = len(collection)
        self.page = items_per_page

    def item_count(self):
        return self._item_count

    def page_count(self):
        div = self._item_count // self.page
        return div if not self._item_count % self.page else div + 1

    def page_item_count(self, page_index):
        return min(self.page, self._item_count - page_index * self.page) \
            if 0 <= page_index < self.page_count() else -1

    def page_index(self, item_index):
        if self._item_count <= item_index or item_index < 0 or not self._item_count:
            return -1
        return item_index // self.page
