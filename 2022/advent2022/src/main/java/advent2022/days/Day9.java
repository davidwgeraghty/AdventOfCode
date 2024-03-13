package advent2022.days;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class Day9 extends Day
{
    private int[] moveHead(String direction, int[] headKnot) {
        if (direction.equals("R"))
            headKnot[0] = headKnot[0] + 1;
        else if (direction.equals("L"))
            headKnot[0] = headKnot[0] - 1;
        else if (direction.equals("U"))
            headKnot[1] = headKnot[1] + 1;
        else if (direction.equals("D"))
            headKnot[1] = headKnot[1] - 1;

        return headKnot;
    }

    private int[] moveTailTowardsHead(int[] tailXY, int[] headXY) {
        if (headXY[1] > tailXY[1])
            tailXY[1] = tailXY[1] + 1;
        else if (headXY[1] < tailXY[1])
            tailXY[1] = tailXY[1] - 1;

        if (headXY[0] > tailXY[0])
            tailXY[0] = tailXY[0] + 1;
        else if (headXY[0] < tailXY[0])
            tailXY[0] = tailXY[0] - 1;

        return tailXY;
    }

    private boolean isTwoAway(int[] tailXY, int[] nextHeadXY) 
    {
        return Math.abs(nextHeadXY[0] - tailXY[0]) == 2 
            || Math.abs(nextHeadXY[1] - tailXY[1]) == 2;
    }

    // need to convert so that we can use the tailSet to track where we've been
    private List<Integer> convertPrimitiveToList(int[] tailKnot) {
        return Arrays.stream(tailKnot).boxed().collect(Collectors.toList());
    }

    public String getPart1Answer()
    {
        ArrayList<String> lines = getLinesFromFile(getInputFile(false, "9"));

        int[] headKnot = {0, 0};
        int[] tailKnot = {0, 0};
        Set<List<Integer>> tailSet = new HashSet<List<Integer>>();
        tailSet.add(convertPrimitiveToList(tailKnot));

        for (String line : lines)
        {
            String direction = line.split(" ")[0];
            int distance = Integer.parseInt(line.split(" ")[1]);
            for (int i = 0; i < distance; i++)
            {
                headKnot = moveHead(direction, headKnot);

                if (isTwoAway(headKnot, tailKnot))
                {
                    tailKnot = moveTailTowardsHead(tailKnot, headKnot);
                    tailSet.add(convertPrimitiveToList(tailKnot));
                }
            }
        }

        return Integer.toString(tailSet.size());
    }

    public String getPart2Answer()
    {
        ArrayList<String> lines = getLinesFromFile(getInputFile(false, "9"));

        int[] headKnot = {0, 0};
        ArrayList<int[]> tailKnots = new ArrayList<>();
        for (int i = 0; i < 9; i++)
        {
            tailKnots.add(new int[]{0, 0});
        }

        Set<List<Integer>> tailSet = new HashSet<List<Integer>>();
        tailSet.add(convertPrimitiveToList(tailKnots.get(tailKnots.size() - 1)));

        for (String line : lines)
        {
            String direction = line.split(" ")[0];
            int distance = Integer.parseInt(line.split(" ")[1]);

            for (int i = 0; i < distance; i++)
            {
                headKnot = moveHead(direction, headKnot);
                int[] tempknot = headKnot;

                for (int j = 0; j < tailKnots.size(); j++)
                {
                    if (isTwoAway(tempknot, tailKnots.get(j)))
                    {
                        tailKnots.set(j, moveTailTowardsHead(tailKnots.get(j), tempknot));
                    }
                    tempknot = tailKnots.get(j);
                }
                tailSet.add(convertPrimitiveToList(tailKnots.get(tailKnots.size() - 1)));
            }
        }

        return Integer.toString(tailSet.size());
    }
}
