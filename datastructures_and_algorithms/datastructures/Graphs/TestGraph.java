public class TestGraph
{
    public static void main(String[] args)
    {
	Graph g = new Graph();
	// set up locations
	g.addVertex('A'); // 0
	g.addVertex('B'); // 1
	g.addVertex('C'); // 2
	g.addVertex('D'); // 3
	g.addVertex('E'); // 4
	g.addVertex('F'); // 5
	g.addVertex('G'); // 6
	// set up connections
	g.addEdge(0, 1); // AB
	g.addEdge(1, 2); // BC
	g.addEdge(0, 3); // AD
	g.addEdge(3, 4); // DE
	g.addEdge(0, 5); // AF
	g.addEdge(4, 6); // EG

	System.out.println("Visits: ");
	g.dfs();
	System.out.println();
    }

}