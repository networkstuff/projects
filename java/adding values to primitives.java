package academy.learnprogramming.;

public class Main {

    //Author: Ivan V
    //purpose: for educational/presentation purposes ONLY!

    public static void main(String[] args) {

      byte one = 12;

        short two = 5;

        int three = 10;

        long six = 5000L * 10 + (one + two + three);

        // ------------OR-----------

        // or long six = (5000L * 10 + one + two + three);

        // ------------OR-----------


        // --first line-- short test = (short) (1000 + 10 *
        // --second line -- (one + two + three));
        // byte, short and int value changed to 10,20,50

        System.out.println(six);

    }
}
