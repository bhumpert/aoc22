#! /usr/bin/env python
from dataclasses import dataclass, field
from typing import Union


@dataclass
class Node:
    children: dict[str, Union['Node',  int]] = field(default_factory=dict)
    parent: Union['Node', None] = None
    size: Union[int, None] = None

    def make_size(self) -> None:
        self.size = 0
        for child in self.children.values():
            if isinstance(child, Node):
                child.make_size()
                self.size += child.size
            else:
                self.size += child


def apply_command(curr_node: Node, cmd: str) -> Node:
    if cmd[:4] == '$ cd':
        *_, name = cmd.split(' ')
        if name == '..':
            return curr_node.parent
        return curr_node.children[name]
    elif cmd[:4] == '$ ls':
        return curr_node
    else:  # file listing from ls
        info, name = cmd.split(' ')
        if info == 'dir':
            curr_node.children[name] = Node(parent=curr_node)
            return curr_node
        curr_node.children[name] = int(info)
        return curr_node


def sum_small_dirs(node: Node, lim: int) -> int:
    s = node.size if node.size <= lim else 0
    for child in node.children.values():
        if isinstance(child, Node):
            s += sum_small_dirs(child, lim)
    return s


def find_smallest_dir(node: Node, lim: int) -> Union[int, None]:
    values = []
    for child in node.children.values():
        if isinstance(child, Node):
            if (val := find_smallest_dir(child, lim)) is not None:
                values.append(val)
    if len(values) == 0:
        if node.size < lim:
            return None
        return node.size
    return sorted(values)[0]


def main():
    base_node = Node()
    curr_node = base_node
    with open('day7.txt', 'r') as f:
        f.readline()
        for line in f:
            curr_node = apply_command(curr_node, line.strip('\n'))

    base_node.make_size()
    print(f"Part 1: {sum_small_dirs(base_node, 100000)}")

    FS_SIZE = 70000000
    UPDATE_SIZE = 30000000
    free_space = FS_SIZE - base_node.size
    space_needed = UPDATE_SIZE - free_space
    print(f"Part 2: {find_smallest_dir(base_node, space_needed)}")


if __name__ == "__main__":
    main()
