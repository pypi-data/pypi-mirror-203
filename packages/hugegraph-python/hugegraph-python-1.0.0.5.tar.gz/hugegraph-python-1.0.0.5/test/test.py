from hugegraph import PyHugeGraph

if __name__ == '__main__':
    client = PyHugeGraph("xxxx", "8080", user="admin", pwd="admin", graph="hugegraph")

    """system"""
    res = client.get_graphinfo()
    print(res)

    res = client.get_all_graphs()
    print(res)

    res = client.get_version()
    print(res)

    res = client.get_graph_config()
    print(res)

    """schema"""
    schema = client.schema()
    res = schema.getVertexLabels()
    print(res)

    """graph"""
    g = client.graph()
    res = g.getVertexById("1:tom").label
    # g.removeVertexById("1:vadas")
    print(res)
    g.close()

    """gremlin"""
    gremlin = client.gremlin()
    res = gremlin.exec("g.E('S1:josh>2>>L1').outV().inE().outV()")
    print(res)

