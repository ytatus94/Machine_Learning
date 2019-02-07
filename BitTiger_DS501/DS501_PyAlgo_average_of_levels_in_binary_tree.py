class Solution():
    def averageOfLevels(self, root):
        queue = [root]
        answers = []

        while True:
            size = len(queue)

            if size == 0:
                break

            total = 0

            for i in range(size):
                node = queue.pop(0)
                total += node.val

                # BFS
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            answers.append(float(total) / size)
        return answers
