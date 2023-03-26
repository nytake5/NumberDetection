class NumberOfBus:
    def __init__() -> None:
        pass

    def __init__(self, filename, xml: size, bndbox):
        self.filename = filename
        self.size = Size(size)
        self.bndbox = BndBox(bndbox)


class Size:
    def __init__(self, xmlNode):
        width = 0
        height = 0
        depth = 0
        for node in xmlNode:
            if node.tag == "width":
                width = int(node.text)
            elif node.tag == "height":
                height = int(node.text)
            elif node.tag == "depth":
                depth = int(node.text)
        self.width = width
        self.height = height
        self.depth  = depth

class BndBox:
    def __init__(self, xmlNode) -> None:
        xmax = 0
        xmin = 0
        ymin = 0
        ymax = 0
        for node in xmlNode:
            if node.tag == "xmax":
                xmax = int(node.text)
            elif node.tag == "xmin":
                xmin = int(node.text)
            elif node.tag == "ymin":
                ymin = int(node.text)
            elif node.tag == "ymax":
                ymax = int(node.text)
        self.xmax = xmax
        self.xmin = xmin
        self.ymin = ymin
        self.ymax = ymax 