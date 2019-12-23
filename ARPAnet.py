# -*- coding: utf-8 -*-
__author__ = 'Mage'

class NetTable:
    def __init__(self,table):
        super().__init__()
        self.dict=table
    def append(self,index,dist):
        self.dict[index]=dist

class NetNode:
    def __init__(self, index, neibourNodes):
        self.index = index
        self.table = {}
        self.pretable = {}
        self.neibourNodes = neibourNodes
        self.count = 0
        self.cost = 0
    def updateTable(self,table):
        self.count += 1
        if table == self.table:
            stable = True
        else:
            stable = False
            self.cost = self.count
        self.pretable = self.table
        self.table = table
        return stable

    def clearCount(self):
        self.count = 0

    def timeCost(self):
        return self.cost

class Net:
    def __init__(self, nodes):  
        self.nodes = {}
        for node in nodes:
            self.nodes[node.index] = node
    def setDest(self,index):
        self.destNode = index
        self.nodes[index].table[index] = 0
    def disconnectNode(self,node1,node2):
        if node2 in self.nodes[node1].neibourNodes:
            self.nodes[node1].neibourNodes[node2] = float("inf")
        if node1 in self.nodes[node2].neibourNodes:
            self.nodes[node2].neibourNodes[node1] = float("inf")
    def updateTable(self):
        for node in self.nodes.values():
            node.clearCount()
        while True:
            stable = True
            for node in self.nodes.values():
                if node.index == self.destNode:
                    continue
                table = {}
                for nnode in node.neibourNodes:
                    if len(self.nodes[nnode].table) != 0:
                        table[nnode]=node.neibourNodes[nnode] + min(dist for dist in self.nodes[nnode].table.values())
        
                stable = stable & node.updateTable(table)
            if stable:
                break
    def printTable(self):
        for node in self.nodes.values():
            if node.index == self.destNode:
                continue
            print("P{},table:{},耗时:{}".format(node.index,node.table,node.timeCost()))
            


if __name__ == "__main__":
    node1 = NetNode(1,{2:4,3:5})
    node2 = NetNode(2,{1:4,3:3,4:1})
    node3 = NetNode(3,{1:5,2:3,4:2,5:20})
    node4 = NetNode(4,{2:1,3:2,5:2})
    node5 = NetNode(5,{3:20,4:2})

    net = Net([node1,node2,node3,node4,node5])
    net.setDest(5)
    net.updateTable()
    net.printTable()
    net.disconnectNode(4,5)
    net.updateTable()
    net.printTable()