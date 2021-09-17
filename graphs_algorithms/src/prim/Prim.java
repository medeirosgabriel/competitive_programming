package prim;

import java.util.Scanner;

public class Prim {

	private int nNodes;
	private int nEdges;
	private int[][] graph;
	
	public Prim(int nNodes) {
		this.nNodes = nNodes;
		this.graph = new int[this.nNodes + 1][this.nNodes + 1];
		receiveData();
	}
	
	private void receiveData() {
		System.out.println("========== Making Adjacency List ==========");
		Scanner sc = new Scanner(System.in);
		
		System.out.print("How many edges are there? ");
		this.nEdges = sc.nextInt(); sc.nextLine();
		for (int i = 0; i < this.nEdges; i++) {
			String[] line = sc.nextLine().split(" ");
			int l1 = Integer.valueOf(line[0]), l2 = Integer.valueOf(line[1]);
			int dist = Integer.valueOf(line[2]);
			this.graph[l1][l2] = dist;
			this.graph[l2][l1] = dist;
		}
		sc.close();
	}
	
	private int minKey(int key[], Boolean mstSet[]) {
        int min = Integer.MAX_VALUE, min_index = -1;
        for (int v = 1; v < this.nNodes + 1; v++) {
            if (mstSet[v] == false && key[v] < min) {
                min = key[v];
                min_index = v;
            }
        }
        return min_index;
    }
 
    private void printMST(int parent[], int graph[][]) {
        System.out.println("Edge \tWeight");
        for (int i = 2; i < this.nNodes + 1; i++)
            System.out.println(parent[i] + " - " + i + "\t" + this.graph[i][parent[i]]);
    }
 
    public void primMST() {
        int parent[] = new int[this.nNodes + 1];
        int key[] = new int[this.nNodes + 1];
        Boolean mstSet[] = new Boolean[this.nNodes + 1];

        for (int i = 0; i < this.nNodes + 1; i++) {
            key[i] = Integer.MAX_VALUE;
            mstSet[i] = false;
        }
 
        key[1] = 0;
        parent[1] = -1;

        for (int i = 0; i < this.nNodes; i++) {
            int u = minKey(key, mstSet);
            mstSet[u] = true;
            for (int v = 1; v < this.nNodes + 1; v++) {
                if (this.graph[u][v] != 0 && mstSet[v] == false && 
                		this.graph[u][v] < key[v]) {
                    parent[v] = u;
                    key[v] = this.graph[u][v];
                }
            }
        }
        
        printMST(parent, graph);
    }
}
