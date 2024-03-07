package advent2022.days;

import java.util.ArrayList;

public class Day8 extends Day
{
    private ArrayList<ArrayList<Integer>> getIntLinesFromLines(ArrayList<String> lines) 
    {
        ArrayList<ArrayList<Integer>> intLines = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i < lines.size(); i++)
        {
            String line = lines.get(i);
            ArrayList<Integer> intLine = new ArrayList<Integer>();
            for (int j = 0; j < line.length(); j++)
            {
                intLine.add(Character.getNumericValue(line.charAt(j)));
            }
            intLines.add(intLine);
        }
        return intLines;
    }

    public String getPart1Answer()
    {
        ArrayList<String> lines = getLinesFromFile(getInputFile(false, "8"));
        ArrayList<ArrayList<Integer>> intLines = getIntLinesFromLines(lines);
        
        // start the count with perimeter trees
        int visibleTreeCount = 2 * (intLines.size() + intLines.get(0).size() - 2);
        for (int i = 1; i < intLines.size() - 1; i++)
        {
            ArrayList<Integer> intLine = intLines.get(i);
            for (int j = 1; j < intLine.size() - 1; j++)
            {
                boolean leftClear = true;
                for (int k = j - 1; k >= 0; k--)
                {
                    if(intLine.get(j) <= intLine.get(k))
                    {
                        leftClear = false;
                        break;
                    }
                }

                boolean rightClear = true;
                for (int k = j + 1; k < intLine.size(); k++)
                {
                    if(intLine.get(j) <= intLine.get(k))
                    {
                        rightClear = false;
                        break;
                    }
                }

                boolean topClear = true;
                for (int k = i - 1; k >= 0; k--)
                {
                    if(intLine.get(j) <= intLines.get(k).get(j))
                    {
                        topClear = false;
                        break;
                    }
                }
                boolean bottomClear = true;
                for (int k = i + 1; k < intLines.size(); k++)
                {
                    if(intLine.get(j) <= intLines.get(k).get(j))
                    {
                        bottomClear = false;
                        break;
                    }
                }

                if (leftClear || rightClear || topClear || bottomClear)
                {
                    visibleTreeCount++;
                }
            }
        }

        return Integer.toString(visibleTreeCount);
    }

    public String getPart2Answer()
    {
        ArrayList<String> lines = getLinesFromFile(getInputFile(false, "8"));
        ArrayList<ArrayList<Integer>> intLines = getIntLinesFromLines(lines);
        
        int scenicScore = 1;
        for (int i = 1; i < intLines.size() - 1; i++)
        {
            ArrayList<Integer> intLine = intLines.get(i);
            for (int j = 1; j < intLine.size() - 1; j++)
            {
                // default value assumes clear view to edge
                int leftScore = j;
                for (int k = j - 1; k >= 0; k--)
                {
                    if(intLine.get(j) <= intLine.get(k))
                    {
                        // overwrite if something blocks the view
                        leftScore = Math.abs(k - j);
                        break;
                    }
                }

                int rightScore = intLine.size() - 1 - j;
                for (int k = j + 1; k < intLine.size(); k++)
                {
                    if(intLine.get(j) <= intLine.get(k))
                    {
                        rightScore = Math.abs(k - j);
                        break;
                    }
                }

                int topScore = i;
                for (int k = i - 1; k >= 0; k--)
                {
                    if(intLine.get(j) <= intLines.get(k).get(j))
                    {
                        topScore = Math.abs(i - k);
                        break;
                    }
                }
                int bottomScore = intLines.size() - 1 - i;
                for (int k = i + 1; k < intLines.size(); k++)
                {
                    if(intLine.get(j) <= intLines.get(k).get(j))
                    {
                        bottomScore = Math.abs(i - k);
                        break;
                    }
                }

                int tempScenicScore = leftScore * rightScore * topScore * bottomScore;
                if (tempScenicScore > scenicScore)
                {
                    scenicScore = tempScenicScore;
                }
            }
        }

        return Integer.toString(scenicScore);
    }
}
