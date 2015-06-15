import java.util.Iterator;
import java.util.NoSuchElementException;
import java.io.Serializable;

public class Dictionary<K, V> implements IDictionary<K, V>, Serializable
{
    private Entry<K, V>[] _table; // entries
    private int _numberOfEntries;
    private static final int DEFAULT_SIZE = 1001; // prime for table size always
    private static final double MAX_LOAD_FACTOR = 0.5; // how full before we expand table

    public Dictionary()
	{
	    this(DEFAULT_SIZE); // construct with default size if no param passed
	}

    public Dictionary(int tableSize)
	{
	    // table size must be a prime
	    int nextPrime = this.getNextPrime(tableSize);
	    // construct table and set object variables
	    this._table = (Entry<K,V>[])new Object[nextPrime];
	    this._numberOfEntries = 0;
	    
	} // END CONSTRUCTOR

    public V getValue(K key)
    {
	V result = null;

	int index = this.getHashKey(key);
	index = this.locate(index, key);

	if (index != -1)
	    {
		result = this._table[index].getValue();
	    }
	return result;
    }

    public boolean contains(K key)
    {
	int index = this.getHashKey(key);
	index = this.locate(index, key);

	return index >= 0; // -1 if not found
    }

    public boolean isEmpty()
    {
	return this._numberOfEntries == 0;
    }

    public boolean isFull()
    {
	return this._numberOfEntries == this._table.length;
    }

    public V remove(K key)
    {
	V removedValue = null; // assume no value has been removed
	int index = this.getHashKey(key);  // get original insertion point for entry
	index = this.locate(index, key); // probe until found

	if (index != -1)
	    {
		// get the value to be removed and then remove value from dictionary
		removedValue = this._table[index].getValue();
		this.setToRemoved(index);
		this._numberOfEntries--; // reduce amount of entries
	    }
	// return removedValue as null or value being removed
	return removedValue;
    }
    
    /**
     * Supporter function for removing an entry from the dictionary
     * @param index     The index to remove from the dictionary
     */
    private void setToRemoved(int index)
    {
	this._table[index] = null;
    }

    private int getHashKey(K value)
    {
	return 0;
    }

    /** 
     * Suporter function for methods searching for a value in the dictionary.
     * @param index      Current index searching from
     * @param key        searching for
     * @returns index    of value if found otherwise -1 if not in dictionary.
     */
    private int locate(int index, K key)
    {
	boolean found = false;
	int result = -1; // assume not in table here for tidier code
	// search until key is found 
	while (!found && (this._table[index] != null))
	       {
		   if (key.equals(this._table[index].getKey()) )
		       {
			   found = true;
		       }
		   else
		       {
			   // probe to next location
			   index = this._linearProbe(index) % this._table.length;
		       }
	       }
	       // either key is found or null is found at index location
	       if(found)
		   result = index;
	       return result;
    }

    private int getNextPrime(int tableSize)
    {
	int a = 0, i, j;
	for (j = a+1; ; j++) // go until return
	    {
		for (i = 2; i < j; i++)
		    {
			if (j % i == 0)
			    break;
		    }
		if (i == j)
		    {
			return j;
		    }
	    }
    }

    public int getMaxSize()
    {
	return this._table.length;
    }

    public Iterator<K> getKeyIterator()
    {
	// TODO (need to make iterator class still)
	return null;
    }

    public Iterator<V> getValueIterator()
    {
	return null;
    }

    public void clear()
    {
	for (int i=0; i<this._table.length; i++)
	    {
		this.setToRemoved(i);
	    }
	this._numberOfEntries = 0;
    }

}