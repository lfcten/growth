class TrieNode:
    def __init__(self):
        self.flag = False
        self.next = [None] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        def helper(idx, word, root):
            if idx == len(word):
                root.flag = True
                return
            c = word[idx]
            ind = ord(c) - ord("a")
            if root.next[ind] is None:
                root.next[ind] = TrieNode()

            helper(idx + 1, word, root.next[ind])

        helper(0, word, self.root)


def find_words(root, board, x, y):
    m, n = len(board), len(board[0])
    dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    def helper(root, board, x, y, indices, all_indices):
        if x >= m or x < 0 or y >= n or y < 0 or board[x][y] == "#":
            return
        c = board[x][y]
        idx = ord(c) - ord("a")
        if root.next[idx] is None:
            return
        root = root.next[idx]
        indices.append((x, y))
        if root.flag:
            all_indices.append(indices)

        board[x][y] = "#"
        for dir in dirs:
            x_new, y_new = x + dir[0], y + dir[1]
            helper(root, board, x_new, y_new, indices, all_indices)
        board[x][y] = c
        indices.pop()

    all_indices = []
    indices = []
    helper(root, board, x, y, indices, all_indices)
    return all_indices


def boggle_game(board, word_dict):
    m, n = len(board), len(board[0])
    trie = Trie()
    for word in word_dict:
        trie.insert(word)

    def dfs(board, pos):
        if pos == m * n:
            return []
        max_res = []
        for p in range(pos, m * n):
            x, y = p // n, p % n
            all_indices = find_words(trie.root, board, x, y)
            for indices in all_indices:
                w_list = []
                for i, j in indices:
                    w_list.append(board[i][j])
                    board[i][j] = "#"
                res = dfs(board, pos + 1)
                if len(res) + 1 > len(max_res):
                    max_res = ["".join(w_list)] + res
                for k, c in enumerate(w_list):
                    i, j = indices[k]
                    board[i][j] = c
        return max_res
    return dfs(board, 0)
