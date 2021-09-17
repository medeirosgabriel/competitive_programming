package kruskal;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Kruskal {
	
	private int nNodes;
	private int nEdges;
	private ArrayList<int[]> edges;
	private int[] parent;
	
	public Kruskal(int nNodes) {
		this.nNodes = nNodes;
		this.edges = new ArrayList<int[]>();
		this.parent = new int[this.nNodes + 1];
		for (int i = 0; i < this.parent.length; i++) {
			this.parent[i] = i;
		}
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
			this.edges.add(new int[] {l1, l2, dist});
		}
		Collections.sort(this.edges, new PQComparator());
		sc.close();
	}
	
	private int find(int node) {
		if (this.parent[node] == node) {
			return node;
		}
		this.parent[node] = find(this.parent[node]);
		return this.parent[node];
	}
	
	private void join(int node1, int node2) {
		if (this.parent[node1] != this.parent[node2]) {
			this.parent[node1] = this.parent[node2];
		}
	}
	
	public void generateTree () {
		int sum_cost = 0;
		for (int[] edge: this.edges) {
			int parentCity1 = this.find(edge[0]);
			int parentCity2 = this.find(edge[1]);
			if (parentCity1 != parentCity2) {
				sum_cost += edge[2];
				join(parentCity1, parentCity2);
			}
		}
		System.out.println(String.format("Cost: %d", sum_cost));
		for (int i = 0; i < this.parent.length; i++) {
			System.out.println(String.format("Node: %d Parent: %d", i, this.parent[i]));
		}
	}
}
