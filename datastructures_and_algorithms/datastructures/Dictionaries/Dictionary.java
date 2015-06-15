import java.util.Iterator;
import java.util.NoSuchElementException;
import java.io.serializable;

public class Dictionary<K, V> implements IDictionary<K, V>, Serializable
{
    private Entry<K, V>[] _table; // entries
    private int _numberOfEntries;
    private static final int DEFAULT_SIZE = 1001; // prime for table size always
    private static final int MAX_LOAD_FACTOR = 0.5; // how full before we expand table

    public Dictionary()
	{
	    this(DEFAULT_SIZE); // construct with default size if no param passed
	}

    public Dictionary(int tableSize)
	{
	    // table size must be a prime
	    int nextPrime = this.getNextPrime(tableSize);
	    // construct table and set object variables
	    this._table = newEntry[nextPrime];
	    this._numberOfEntries = 0;
	    
	} // END CONSTRUCTOR

    

}