"""
My little Stack
"""
from typing import Any

my_stack = []

def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    my_stack.append(elem)



def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """
    if my_stack:
        last_elem = my_stack.pop()
        return last_elem




def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    if 0 <= ind < len(my_stack):
        return my_stack[-1 - ind]




def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    my_stack.clear()

if __name__ == '__main__':
    push(1)
    print(my_stack)
    push(2)
    print(my_stack)