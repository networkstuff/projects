package academy.learnprogramming;

// import java.util.function.LongFunction;

public class Main {

    //Author: Ivan V
    //purpose: for educational/presentation purposes ONLY!
    //explanation: Java code to use minimum and maximum value adding 1 to produce an overflow or minus 1 to produce an underflow
    //Primitive Types and sizes

    public static void main(String[] args) {

        // int myValue = 1000;
        // you can also write the value as 1_000 to make it easier to understand if you like
        // below is setting the value of minimum and maximum value allowed in Java by default
        // the wrapper class "Integer" allows us to use the preventive class
        int myMinIntValue = Integer.MIN_VALUE;
        int myMaxIntValue = Integer.MAX_VALUE;
        // below is print out and explanation
        System.out.println("Integer Minimum Value = " + myMinIntValue);
        //below result is of underflow since it passes the minimum value allowed
        System.out.println("busted MIN value = " + (myMinIntValue - 1 ));
        System.out.println("Integer Maximum Value = " + myMaxIntValue);
        //below result is of overflow since it passes the maximum value allowed
        System.out.println("busted MAX value = " + (myMaxIntValue + 1 ));

        //purpose: for educational/presentation purposes ONLY!

        byte myMinByteValue = Byte.MIN_VALUE;
        byte myMAXByteValue = Byte.MAX_VALUE;
        //  underflow in byte
        System.out.println("myMinByteValue = " +  myMinByteValue);
        //  overflow in byte
        System.out.println("myMAXByteValue = " +  myMAXByteValue);

        //purpose: for educational/presentation purposes ONLY!
        //explanation: Java code to Datatype of Short

        short myMinShortValue = Short.MIN_VALUE;
        short myMAXShortValue = Short.MAX_VALUE;
        //  underflow in short
        System.out.println("myMinShortValue = " +  myMinShortValue);
        //  overflow in short
        System.out.println("myMAXShortValue = " +  myMAXShortValue);

        //when using a primitive such as long the number L for Long should be used to allow for a larger number such as Long myLongValue = 100L;
        long myMinLongValue = Long.MIN_VALUE;
        long myMAXLongValue = Long.MAX_VALUE;
        //  underflow in long
        System.out.println("myMinLongValue = " +  myMinLongValue);
        //  overflow in long
        System.out.println("myMAXLongValue = " +  myMAXLongValue);
        //  using long to allow for a large number
        long bigLongLiteralValue = 2_345_543_234L;
        System.out.println(bigLongLiteralValue);

        // if you where to type a number larger than what the integer allow such as short test =  32768; then you would get an error because
        // the number is larger then is permitted so a solution is to use the long integer instead.

        int myTotal = (myMinIntValue / 2 );

        //telling JAVA to treat a value as a byte and not as an Integer

        byte myNewByteValue = (byte) (myMinByteValue / 2);

        //telling JAVA to treat a value as a short and not as an Integer

        short myNewShortValue = (short) (myMinShortValue / 2);


    }
}
