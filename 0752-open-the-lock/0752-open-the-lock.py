class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1

        queue = deque([('0000', 0)])
        visited = set(['0000'])

        while queue:
            current, turns = queue.popleft()

            if current == target:
                return turns

            for i in range(4):
                for delta in (-1, 1):
                    new_digit = (int(current[i]) + delta) % 10
                    new_state = current[:i] + str(new_digit) + current[i+1:]

                    if new_state not in visited and new_state not in deadends:
                        visited.add(new_state)
                        queue.append((new_state, turns + 1))

        return -1