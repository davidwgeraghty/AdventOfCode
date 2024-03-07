package advent2022.days;

import java.util.ArrayList;
import java.util.List;

import advent2022.helpers.Node;

public class Day7 extends Day
{
    public enum Command {
        CHANGE_DIRECTORY("cd "),
        LIST_CONTENTS("ls"),
        DIRECTORY("dir ");

        public final String command;
    
        private Command(String command) {
            this.command = command;
        }
    }

    private Node getTreeFromLines(ArrayList<String> lines) 
    {
        Node rootNode = new Node();
        Node currentNode = rootNode;

        for (int i = 1; i < lines.size(); i++)
        {
            String line = lines.get(i);
            if (line.indexOf("$") >= 0)
            {
                if (line.indexOf(Command.CHANGE_DIRECTORY.command) >= 0)
                {
                    String argument = line.split(Command.CHANGE_DIRECTORY.command)[1];
                    if (argument.equals("/"))
                    {
                        currentNode = rootNode;
                    }
                    else if(argument.equals(".."))
                    {
                        currentNode = currentNode.getParent();
                    }
                    else
                    {
                        currentNode = getOrCreateDirectory(currentNode, argument);
                    }
                }
                else if (line.indexOf(Command.LIST_CONTENTS.command) >= 0)
                {
                    // do nothing
                }
            }
            else if (line.indexOf(Command.DIRECTORY.command) >= 0)
            {
                String name = line.split(Command.DIRECTORY.command)[1];
                currentNode.addChild(getOrCreateDirectory(currentNode, name));
            }
            else
            {
                int fileSize = Integer.parseInt(line.split(" ")[0]);
                String name = line.split(" ")[1];
                currentNode.addChild(new Node(currentNode, name, fileSize));
            }
        }
        return rootNode;
    }

    private Node getOrCreateDirectory(Node currentNode, String name) {
        for (Node node : currentNode.getChildren())
        {
            if (node.isDirectory() && node.getName().equals(name))
            {
                return node;
            }
        }
        // create directory if it doesn't exist
        return new Node(currentNode, name);
    }

    private void populateDirectorySizes(Node current) 
    {
        if (current.isDirectory())
        {
            int total = 0;
            for (Node child : current.getChildren())
            {
                if (child.isDirectory())
                {
                    populateDirectorySizes(child);
                    total += child.getSize();
                }
                else
                {
                    total += child.getSize();
                }
            }
            current.setSize(total);
        }
    }

    private ArrayList<Node> getFlattenedDirectories(Node node) {
        ArrayList<Node> tempNodes = new ArrayList<>();
        
        for (Node child : node.getChildren())
        {
            if (child.isDirectory())
            {
                tempNodes.addAll(getFlattenedDirectories(child));
            }
        }
        if (node.isDirectory())
        {
            tempNodes.add(node);
        }

        return tempNodes;
    }

    private Node getDirectoryToDelete(List<Node> directories, int minSize) 
    {
        Node tempNode = null;

        for (Node node : directories)
        {
            if (node.getSize() >= minSize)
            {
                if (tempNode == null || node.getSize() < tempNode.getSize())
                {
                    tempNode = node;
                }
            }
        }
        return tempNode;
    }

    public String getPart1Answer()
    {
        ArrayList<String> lines = getLinesFromFile(getInputFile(false, "7"));
        Node rootNode = getTreeFromLines(lines);
        populateDirectorySizes(rootNode);
        List<Node> directories = getFlattenedDirectories(rootNode);
        
        List<Node> smallDirectories = directories.stream().filter(o -> o.getSize() < 100000).toList();
        return Integer.toString(smallDirectories.stream().map(o -> o.getSize()).reduce(Integer::sum).get());
    }

    public String getPart2Answer()
    {
        ArrayList<String> lines = getLinesFromFile(getInputFile(false, "7"));
        Node rootNode = getTreeFromLines(lines);
        populateDirectorySizes(rootNode);
        List<Node> directories = getFlattenedDirectories(rootNode);
        
        int minSize = 30000000 - (70000000 - rootNode.getSize());
        Node directory = getDirectoryToDelete(directories, minSize);

        return Integer.toString(directory.getSize());
    }
}
