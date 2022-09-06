class Node():
    def __init__(self, key):
        self.key = key  # holds the key
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1  # 1  Red, 0  Black


class RedBlackTree():
    def __init__(self):     #empty tree
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL


    def __search_tree_helper(self, node, key):
        if  key == node.key:
            return 1
        if node == self.TNULL:
            return 0

        if key < node.key:
            return self.__search_tree_helper(node.left, key)
        return self.__search_tree_helper(node.right, key)



    def searchTree(self, k):
        return self.__search_tree_helper(self.root, k)


    def __fix_delete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    # case 3.1
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    # case 3.2
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        # case 3.3
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    # case 3.4
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    # case 3.1
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.left.color == 0 and s.right.color == 0:
                    # case 3.2
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        # case 3.3
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left

                        # case 3.4
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def __delete_node_helper(self, node, key):
        # find the node containing key
        z = self.TNULL
        while node != self.TNULL:
            if node.key == key:
                z = node

            if node.key <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.__fix_delete(x)


    def delete_node(self, key):
        self.__delete_node_helper(self.root, key)



    def __count_node_helper(self, node, key):
        cnt = 0
        while node != self.TNULL:

            if node.key >= key and node.left.key>=key:
                break


            if node.key < key and node.right.key>=key:
                node = node.left
                cnt=cnt+1

            if node.key <= key and node.right.key<=key:
                cnt=cnt+self.__count_node_helper(node.right, key)
                node=node.left
                cnt=cnt+1

            else:
                pass

        return cnt

    def node_count(self, key):
        return self.__count_node_helper(self.root, key)
    

    def __fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # uncle
                if u.color == 1:
                    # case 3.1
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # case 3.2.2
                        k = k.parent
                        self.right_rotate(k)
                    # case 3.2.1
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # uncle

                if u.color == 1:
                    # mirror case 3.1
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        # mirror case 3.2.2
                        k = k.parent
                        self.left_rotate(k)
                    # mirror case 3.2.1
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0



    # rotate left at node x
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # rotate right at node x
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y


    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.key = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1  # new node declared red

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.parent = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        # if new node is a root node, return
        if node.parent == None:
            node.color = 0
            return

        # if the grandparent is None, return
        if node.parent.parent == None:
            return

        self.__fix_insert(node)





rbt = RedBlackTree()


with open("input.txt", 'r') as fin:
    for line in fin:
        m = line.split()
        print(int(m[0]))
        break

with open('input.txt', 'r') as fin:
    next(fin)
    for line in fin:
        x = line.split()
        if(int(x[0])==0):
            if (rbt.searchTree(int(x[1]))) == 1:
                rbt.delete_node(int(x[1]))
                print(x[0] + ' ' + x[1] + ' 1')
            else:
                print(x[0] + ' ' + x[1] + ' 0')


        elif(int(x[0])==1):
            if(rbt.searchTree(int(x[1])))==0:
                rbt.insert(int(x[1]))
                print(x[0] + ' ' + x[1] + ' 1')
            else:
                print(x[0] + ' ' + x[1] + ' 0')



        elif(int(x[0])==2):
            print(x[0]+' '+x[1]+' '+ str(rbt.searchTree(int(x[1]))))

        elif(int(x[0])==3):
            print(x[0]+' '+x[1]+' '+str(rbt.node_count(int(x[1]))))

        else:
            pass





