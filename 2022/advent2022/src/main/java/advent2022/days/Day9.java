package advent2022.days;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

import org.javatuples.Pair;

public class Day9 extends Day
{
    private Pair<Integer, Integer> moveHead(String direction, Pair<Integer, Integer> headKnot) {
        if (direction.equals("R"))
            headKnot = headKnot.setAt0(headKnot.getValue0() + 1); // weird syntax here... '.setAt0' does not change the object it's called on, just returns a new object
        else if (direction.equals("L"))
            headKnot = headKnot.setAt0(headKnot.getValue0() - 1);
        else if (direction.equals("U"))
            headKnot = headKnot.setAt1(headKnot.getValue1() + 1);
        else if (direction.equals("D"))
            headKnot = headKnot.setAt1(headKnot.getValue1() - 1);

        return headKnot;
    }

    private Pair<Integer, Integer> moveTailTowardsHead(Pair<Integer, Integer> tailXY, Pair<Integer, Integer> headXY) {
        if (headXY.getValue1() > tailXY.getValue1())
            tailXY = tailXY.setAt1(tailXY.getValue1() + 1);
        else if (headXY.getValue1() < tailXY.getValue1())
            tailXY = tailXY.setAt1(tailXY.getValue1() - 1);

        if (headXY.getValue0() > tailXY.getValue0())
            tailXY = tailXY.setAt0(tailXY.getValue0() + 1);
        else if (headXY.getValue0() < tailXY.getValue0())
            tailXY = tailXY.setAt0(tailXY.getValue0() - 1);

        return tailXY;
    }

    private boolean isTwoAway(Pair<Integer, Integer> tailXY, Pair<Integer, Integer> nextHeadXY) 
    {
        return Math.abs(nextHeadXY.getValue0() - tailXY.getValue0()) == 2 
            || Math.abs(nextHeadXY.getValue1() - tailXY.getValue1()) == 2;
    }

    public String getPart1Answer()
    {
        ArrayList<String> lines = getLinesFromFile(getInputFile(false, "9"));

        Pair<Integer, Integer> headKnot = new Pair<Integer, Integer>(0, 0);
        Pair<Integer, Integer> tailKnot = new Pair<Integer, Integer>(0, 0);
        Set<Pair<Integer, Integer>> tailSet = new HashSet<Pair<Integer, Integer>>();
        tailSet.add(tailKnot);

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
                    tailSet.add(tailKnot);
                }
            }
        }

        return Integer.toString(tailSet.size());
    }

    public String getPart2Answer()
    {
        ArrayList<String> lines = getLinesFromFile(getInputFile(false, "9"));

        Pair<Integer, Integer> headKnot = new Pair<Integer, Integer>(0, 0);
        ArrayList<Pair<Integer, Integer>> tailKnots = new ArrayList<>();
        for (int i = 0; i < 9; i++)
        {
            tailKnots.add(new Pair<Integer, Integer>(0, 0));
        }

        Set<Pair<Integer, Integer>> tailSet = new HashSet<Pair<Integer, Integer>>();
        tailSet.add(tailKnots.get(tailKnots.size() - 1));

        for (String line : lines)
        {
            String direction = line.split(" ")[0];
            int distance = Integer.parseInt(line.split(" ")[1]);

            for (int i = 0; i < distance; i++)
            {
                headKnot = moveHead(direction, headKnot);
                Pair<Integer, Integer> tempknot = headKnot;

                for (int j = 0; j < tailKnots.size(); j++)
                {
                    if (isTwoAway(tempknot, tailKnots.get(j)))
                    {
                        tailKnots.set(j, moveTailTowardsHead(tailKnots.get(j), tempknot));
                    }
                    tempknot = tailKnots.get(j);
                }
                tailSet.add(tailKnots.get(tailKnots.size() - 1));
            }
        }

        return Integer.toString(tailSet.size());
    }
}
