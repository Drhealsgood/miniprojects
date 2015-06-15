import java.util.Stack;

public class Graph
{
    private final int MAX_VERTS = 20;
    private Vertex _vertexList[]; // array of verts
    private int _adjMat[][]; // adjacency matrix to represent connections
    private int _numVerts;
    private Stack<Integer> _vertStack; // to keep track of verticies

    public Graph()
    {
	this._vertexList = new Vertex[MAX_VERTS];
	
	this._adjMat = new int[MAX_VERTS][MAX_VERTS];
	this._numVerts = 0;
	this._vertStack = new Stack<Integer>();
	// adj matrix values should already be 0 but in case maybe should insert here

    }

    public void addVertex(char label)
    {
	this._vertexList[this._numVerts++] = new Vertex(label);
    }

    public void addEdge(int start, int end)
    {
	// toggle the bits in the adj matrix to represent a connection
	this._adjMat[start][end] = 1;
	this._adjMat[end][start] = 1;
    }

    public void displayVertex(int v)
    {
	System.out.print(this._vertexList[v].getLabel());
    }

    public void dfs() // depthfirstsearch
    {
	// begin at source vertex and mark it as visited
	this._vertexList[0].setWasVisited(true); 
	this.displayVertex(0);
	this._vertStack.push(0);
	
	while (!this._vertStack.isEmpty()) 
	    {
		// get an unvisited vertex adjacent to the vertex on top of the stack
		int n = this.getAdjUnvisitedVertex(this._vertStack.peek());
		if (n == -1) // if there are no unvisited verticies
		    {
			this._vertStack.pop();
		    }
		else         // we found an unvisited vertex
		    {
			this._vertexList[n].setWasVisited(true); // visited the vertex
			this.displayVertex(n);
			this._vertStack.push(n);
		    }
	    }

	// stack is now empty so we can reset all the visited flags
	for (int i=0; i<this._numVerts; i++)
	    {
		this._vertexList[i].setWasVisited(false);
	    }
    }

    /**
     * Returns the vertices adjacent which are currently unvisited
     * otherwise returns -1 if no verticies are found
     */
    public int getAdjUnvisitedVertex(int v)
    {
	for (int i=0; i<this._numVerts; i++)
	    {
		if(this._adjMat[v][i]==1 && this._vertexList[i].getWasVisited()==false)
		    {
			return i;
		    }
	    }
	return -1;
    }
}