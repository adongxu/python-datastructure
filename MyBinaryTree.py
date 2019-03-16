class Node():
    # 节点类
    def __init__(self, val=-1):
        self.val = val
        self.left = None
        self.right = None


class Tree():
    # 树类
    def __init__(self):
        self.root = Node()

    def add(self, data):
        # 为树加入节点
        node = Node(data)
        if self.root.val == -1:  # 如果树为空，就对根节点赋值
            self.root = node
        else:
            myQueue = []
            treeNode = self.root
            myQueue.append(treeNode)
            while myQueue:  # 对已有的节点进行层次遍历
                treeNode = myQueue.pop(0)
                if not treeNode.left:
                    treeNode.left = node
                    return
                elif not treeNode.right:
                    treeNode.right = node
                    return
                else:
                    myQueue.append(treeNode.left)
                    myQueue.append(treeNode.right)

    # 递归实现前序遍历
    def pre_order_recur(self, root):
        if not root:
            return
        print(root.val)
        self.pre_order_recur(root.left)
        self.pre_order_recur(root.right)

    # 栈实现前序遍历
    def pre_order_loop(self, root):
        if not root:
            return
        node = root
        stack = []
        # 栈为空或者到达叶子节点
        while stack or node:
            while node:
                print(node.val)
                stack.append(node)
                node = node.left
            # 左边遍历到根节点后，返回遍历右子树
            node = stack.pop()
            node = node.right

    # 递归实现中序遍历
    def in_order_recur(self, root):
        if not root:
            return
        self.in_order_recur(root.left)
        print(root.val)
        self.in_order_recur(root.right)

    # 栈实现中序遍历
    def in_order_loop(self, root):
        if not root:
            return
        stack = []
        node = root
        while node or stack:
            # 沿着左子树一直找
            while node:
                stack.append(node)
                node = node.left
            # 左子树到头
            node = stack.pop()
            print(node.val)
            node = node.right

    # 递归实现后序遍历
    def post_order_recur(self, root):
        if not root:
            return
        self.post_order_recur(root.left)
        self.post_order_recur(root.right)
        print(root.val)

    # 迭代实现后序遍历(一个栈)
    def post_order_loop(self, root):
        if not root:
            return
        pre = None
        stack = [root]

        while stack:
            # 栈顶的节点
            cur = stack[-1]
            # 左右子树为空或者左右子树均被访问过
            if (not cur.left and not cur.right) or (pre and (pre == cur.left or pre == cur.right)):
                print(cur.val)
                stack.pop()
                pre = cur

            else:
                # 左右子树不为空就入栈 右先左后
                if cur.right:
                    stack.append(cur.right)

                if cur.left:
                    stack.append(cur.left)

    # 迭代实现后序遍历(两个栈)，跟前序相反输出即可
    def post_order_loop_two_stack(self, root):
        if not root:
            return
        stack, res = [], []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                res.append(node)
                node = node.right
            # 左边到底了
            node = stack.pop()
            node = node.left
        for i in range(len(res)-1, -1, -1):
            print(res[i].val)

    # 队列求层次遍历
    def level_order_loop(self, root):
        if not root:
            return
        queue = [root]
        # 队列变空之前
        while queue:
            cur = queue.pop()
            print(cur.val)

            # 左节点入队
            if cur.left:
                queue.insert(0, cur.left)
            # 右节点入队
            if cur.right:
                queue.insert(0, cur.right)

    # 递归求树的深度
    def depth_recur(self, root):
        depth = 0
        if root:
            leftdep = self.depth_recur(root.left)
            rightdep = self.depth_recur(root.right)
            return max(leftdep, rightdep) + 1
        return depth

    # 迭代求树的深度
    def depth_loop(self, root):
        # 用一个队列
        queue = []
        # 当前遍历到第几层
        level = 0
        if not root:
            return 0
        queue.insert(0, root)

        while queue:
            level += 1
            # 当前这一层的节点数
            size = len(queue)
            # 把当前层的所有节点都pop出去
            while size > 0:
                cur = queue.pop()

                if cur.left:
                    queue.insert(0, cur.left)
                if cur.right:
                    queue.insert(0, cur.right)
                size -= 1

        return level

    # 层次遍历-递归（要用到深度） level:要打印的层的编号从根1开始
    def level_order_recur(self, root, level):
        if not root or level < 1:
            return

        if level == 1:
            print(root.val)
            return

        # 打印当前节点
        self.level_order_recur(root.left, level-1)
        self.level_order_recur(root.right, level-1)

    # 遍历所有的层号
    def tra_depth(self, root):
        if not root:
            return
        depth = self.depth_recur(root)
        for i in range(1, depth+1):
            self.level_order_recur(root, i)

if __name__ == '__main__':
    # 主函数
    datas = [i for i in range(18)]
    tree = Tree()  # 新建一个树对象
    for data in datas:
        tree.add(data)  # 逐个加入树的节点

    print('递归实现前序遍历：')
    tree.pre_order_recur(tree.root)

    print('堆栈实现前序遍历')
    tree.pre_order_loop(tree.root)

    print("递归实现中序遍历：")
    tree.in_order_recur(tree.root)

    print("堆栈实现中序遍历：")
    tree.in_order_loop(tree.root)

    print('递归实现后序遍历：')
    tree.post_order_recur(tree.root)

    print('堆栈实现后序遍历：')
    tree.post_order_loop(tree.root)

    print('堆栈实现后序遍历2：')
    tree.post_order_loop_two_stack(tree.root)

    print('队列实现层次遍历：')
    tree.level_order_loop(tree.root)

    print('树的深度（递归）:')
    print(tree.depth_recur(tree.root))

    print('树的深度（非递归）:')
    print(tree.depth_loop(tree.root))
    print('递归实现层次遍历：')
    print(tree.tra_depth(tree.root))