

class ParseTree:

    def __init__(self, root, children = []):
        self.key = root
        self.children = children or []

    def __repr__(self, level=0):
        ret = "|  " * level + repr(self.key) + "\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret
    
    def addChild(self, child):
        self.children.insert(0, child)

    def addChildren(self, children):
        temp = children.split(" ")
        for child in temp:
            self.children.append(ParseTree(child))

