import sys

def hanoi_towers(num_disks: int):
    towers = {'A': list(reversed(range(1, num_disks + 1))), 'B': [], 'C': []}
    print(f'Initial  state: ', towers)
    move_disk(num_disks, 'A', 'B', 'C', towers)
    print(f'Final  state: ', towers)

def move_disk(n, from_rod, to_rod, extra_rod, towers):
    if n == 0:
        return
    move_disk(n - 1, from_rod, extra_rod, to_rod, towers)
    print(f'Current state: ', towers)
    print(f'Moving disk {n} from rod {from_rod} to rod {to_rod}')
    towers[to_rod].append(towers[from_rod].pop())
    move_disk(n - 1, extra_rod, to_rod, from_rod, towers)

if __name__ == '__main__':
    hanoi_towers(int(sys.argv[1]))
