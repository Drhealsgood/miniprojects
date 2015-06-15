import java.io.Serializable;

public interface IEntry<K, V>
{
    /**
     * retrieve the key field of this object
     * @return K    value associated with key field
     */
    public K getKey();


    /**
     * set the key field of this object
     */
    public void setKey(K key);


    /**
     * get the value field of this object
     * @return V    value associated with value field
     */
    public V getValue();

    /**
     * set the value field of this object
     */
    public void setValue(V value);

}