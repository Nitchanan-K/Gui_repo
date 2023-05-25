def clear_tree_func(self):
    self.tree_view_show_data.delete(*self.tree_view_show_data.get_children())