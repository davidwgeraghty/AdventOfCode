package advent2022.helpers;

import java.util.ArrayList;

public class Node 
{
    private Node parent;
    private ArrayList<Node> children = new ArrayList<Node>();
    private String name;
    private int size = 0;
    private boolean isDirectory = false;

    public Node()
    {
        this.parent = this;
        this.name = "/";
        this.isDirectory = true;
    }

    public Node(Node parent, String name)
    {
        this.parent = parent;
        this.name = name;
        this.isDirectory = true;
    }

    public Node(Node parent, String name, int size)
    {
        this.parent = parent;
        this.name = name;
        this.size = size;
    }

    public ArrayList<Node> getChildren()
    {
        return this.children;
    }

    public int getSize()
    {
        return this.size;
    }

    public String getName()
    {
        return this.name;
    }

    public Node getParent()
    {
        return this.parent;
    }

    public void addChild(Node newChild)
    {
        for (Node child : children)
        {
            if (child.getName().equals(newChild.getName()) && child.isDirectory == newChild.isDirectory)
                return;
        }
        children.add(newChild);
    }

    public void setSize(int size)
    {
        this.size = size;
    }

    public boolean isRoot()
    {
        return this == this.parent;
    }

    public boolean isDirectory()
    {
        return this.isDirectory;
    }
}
