import time
from RBtree import *
from AVLtree import *


p = list(map(int, input("Enter piles: ").split(' ')))
h = int(input("Enter H(H >= pils.length): "))

timer = time.time()

# ------------------------- RED-BLACK Tree logic -----------------------------


piles = RBTree()

for x in p:
    piles.insert(x)


def calculate():
    if len(p) > h:
        return -1
    elif len(p) == h:
        return piles.get_max(piles)
    else:
        return piles.calculate(h)


print(f"value - {calculate()}")

print("\n------------------ time for test -------------\n")

print(f"time - {time.time() - timer}")



# ----------------------------- Array logic -----------------------------


# p.sort()
# 
# def calculate():
#     if len(p) > h:
#         return -1
#     elif len(p) == h:
#         return p[-1]
#     else:
#         for x in range(1, p[-1]):
#             sum = 0
#             for y in p:
#                 sum += int(-1 * y // x * -1)
#             if sum <= h:
#                 return x


# ------------------------- AVL Tree logic -----------------------------

# piles = AVL_Tree()

# root = None

# for x in p:
#     root = piles.insert(root, x)


# def calculate():
#     if len(p) > h:
#         return -1
#     elif len(p) == h:
#         return piles.get_max(root)
#     else:
#         return piles.calculate(root, h)

# print(calculate())

# print("\n------------------ time for test -------------\n")

# print(f"time - {time.time() - timer}")