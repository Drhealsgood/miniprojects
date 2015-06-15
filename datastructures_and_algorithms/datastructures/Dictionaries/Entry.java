public class Entry<K, V> implements IEntry<K,V>, Serializable
{
    private K _key;
    private V _value;

    public Entry(K key)
	{
	    this(key, (V)key);
	}

    public Entry(K key, V value)
	{
	    this._key = key;
	    this._value = value;
	}


    public K getKey()
    {
	return this._key;
    }

    public V getValue()
    {
	return this._value;
    }

    public void setKey(K key)
    {
	this._key = key;
    }

    public void setValue(V value)
    {
	this._value = value;	
    }
}