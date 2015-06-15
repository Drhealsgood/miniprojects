import java.util.Iterator;
public interface IDictionary<K, V>
{
    /**
     * Adds a new entry to the dictionary.
     * In the case the entry already exists in the dictionary 
     * replaces the value with the new value.
     * @param key      object search key of new entry
     * @param value    object related to the key
     * @return null if entry was added to the dictionary; otherwise, value replaced.
     */
    public V add(K key, V value);

    /**
     * Removes anentry from the dictionary.
     * @param key      an object search key of the  entry to be removed
     * @return null if no such object exists or value related to the key ebing removed.
     */
    public V remove(K key);

    /**
     * Retrieves value associated with key passed
     * @param key     key that will be searched for for retrieval of associated value
     * @return value associated with the key.
     */
    public V getValue(K key);

    /**
     * Check whether a specific entry is in the dictionary.
     * @param key    an object search key of the desired entry
     * @return true  if key is associated with an entry in the dictonary.
     */
    public boolean contains(K key);

    /**
     * Check whether the dictionary is empty
     * @return true  if there are no entries in the table
     */
    public boolean isEmpty();

    /**
     * Check whether the dictionary is full
     * @return true  if there is no space remaining in the table.
     */
    public boolean isFull();

    /**
     * Returns the size of the dictionary
     * @return int   the number of entries currently in dictionary
     */
    public int getSize();

    /**
     * Returns the max size of the dictionary
     * @return int   the maximum amount of entries able to be held by the dictionary
     */
    public int getMaxSize();

    /**
     * Returns an iterator of the keys in the dictionary
     * @return Iterator  provifding sequential access to the search keys
     */
    public Iterator<K> getKeyIterator();

    /**
     * Returns an iterator of the values in the dictionary
     * @return Iterator  providing sequential access to the values
     */
    public Iterator<V> getValueIterator();
    /**
     * Removes all entries from the dictionary
     */
    public void clear();
}