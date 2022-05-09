from pathlib import Path
import yaml
from typing import Optional, Iterable


class PermissionChecker:

    # todo

    def __init__(self, plugin_name, permission_file_path):
        self.plugin_name = plugin_name
        self.permissions = {}
        self.load_yml(permission_file_path)

    def load_yml(self, permission_file_path):
        return self

    def has(self):
        return self.permissions

    def check(self):
        pass

    def add(self):
        pass

    def remove(self):
        pass

    def __call__(self):
        return self.permissions

    def __and__(self, other):
        raise RuntimeError("And operation between PermissionsCheckers is not allowed. "
                           "Use or to combine two PermissionCheckers.")

    def __or__(self, other: Optional["PermissionChecker", Iterable]) -> "PermissionChecker":
        if other is None:
            return self
        elif isinstance(other, PermissionChecker):
            self.permissions = self.permissions | other.permissions
            return self
        else:
            self.permissions = self.permissions | set(other)
            return self
