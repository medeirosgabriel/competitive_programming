package dijkstra;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Dijkstra {
	
	private int nNodes;
	private int nEdges;
	private ArrayList<int[]>[] adjacencyList;
	
	public Dijkstra(int nNodes) {
		this.nNodes = nNodes;
		this.adjacencyList = (ArrayList<int[]>[]) new ArrayList[this.nNodes + 1];
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
			adjacencyList[l1] = (adjacencyList[l1] == null) ? new ArrayList<int[]>() : adjacencyList[l1];
			adjacencyList[l2] = (adjacencyList[l2] == null) ? new ArrayList<int[]>() : adjacencyList[l2];
			adjacencyList[l1].add(new int[]{l2, dist});
			adjacencyList[l2].add(new int[]{l1, dist});
		}
		sc.close();
	}
	
	public void shortestDistance (int startNode) {
		
		PriorityQueue<int[]> pQueue = new PriorityQueue<>(this.nEdges, new PQComparator());
		boolean[] visitedNodes = new boolean[this.nNodes + 1];
		int[] distance = new int[this.nNodes + 1];
		Arrays.fill(distance, Integer.MAX_VALUE);
		distance[startNode] = 0;
		pQueue.add(new int[]{0, startNode});
		
		while (!pQueue.isEmpty()) {
			int[] pqe = pQueue.poll();
			int node = pqe[1];
			visitedNodes[node] = true;
			for (int[] e : this.adjacencyList[node]) {
				int nodeNeight = e[0], distStreet = e[1];
				if (!visitedNodes[nodeNeight] && 
						distance[nodeNeight] > distance[node] + distStreet) {
					distance[nodeNeight] = distance[node] + distStreet;
					pQueue.add(new int[]{distance[nodeNeight], nodeNeight});
				}
			}
		}
		
		for (int i = 0; i <= this.nNodes; i++) {
			System.out.println(String.format("%d to %d: %d", startNode, i, distance[i]));
		}
	}
}
