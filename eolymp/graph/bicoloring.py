from collections import defaultdict
import sys, threading


def main():
    def bicoloring():
        def dfs(node, curr_color):
            #if node is visited
            if colors[node] != None:
                if colors[node] != curr_color:
                    return False
                return True
            
            colors[node] = curr_color
            for neighbor in graph[node]:
                if not dfs(neighbor, not curr_color):
                    return False
                
            return True
                    
        num_nodes = int(input())
        
        if num_nodes == 0:
            return None
        
        num_edges = int(input())
        
        #build graph
        graph = defaultdict(list)
        for _ in range(num_edges):
            u,v = list(map(int, input().split()))
            graph[u].append(v)
            graph[v].append(u)
            
            
        colors = [None] * (num_nodes + 1)

        for node in graph:
            #if node not visited
            if colors[node] == None:
                if not dfs(node, True):
                    return False
                
        return True

    while True:
        value = bicoloring()
        if value:
            print("BICOLOURABLE.")
        elif value == None:
            pass
        else:
            print("NOT BICOLOURABLE.")
        
        
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()

    
