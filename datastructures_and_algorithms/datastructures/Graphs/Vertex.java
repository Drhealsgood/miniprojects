public class Vertex
{
    private char _label; // identifier - e.g. 'A'
    private boolean _wasVisited; // have we checked this vertex

    public Vertex(char label)
    {
	this._label = label;
	this._wasVisited = false;
    }

    public char getLabel()
    {
	return this._label;
    }

    public void setLabel(char label)
    {
	this._label = label;
    }

    public boolean getWasVisited()
    {
	return this._wasVisited;
    }

    public void setWasVisited(boolean wasVisited)
    {
	this._wasVisited = wasVisited;
    }

}