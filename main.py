import tomllib
import json
from pydantic import BaseModel

class DataModel(BaseModel):
    name: str
    age: int
    values: list[int]


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)

        elif value > node.value:
            node.right = self._insert(node.right, value)

        return node

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return []

        return (
            self._inorder(node.left)
            + [node.value]
            + self._inorder(node.right)
        )


with open("data.toml", "rb") as file:
    toml_data = tomllib.load(file)


data = DataModel(**toml_data)
tree = BinaryTree()

for value in data.values:
    tree.insert(value)


sorted_values = tree.inorder()

result = {
    "name": data.name,
    "age": data.age,
    "values": sorted_values
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=4)

print(result)