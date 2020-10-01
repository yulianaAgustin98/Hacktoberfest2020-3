class prime {
    public static boolean isPrime(int x) {
        if (x == 1)
            return false;
        if (x < 4)
            return true;
        for (int i = 2; i <= (int) Math.sqrt(x); i++) {
            if (x % i == 0)
                return false;
        }
        return true;
    }

    public static void main(String args[]) {
        int n = 19;
        if (isPrime(n))
            System.out.println("It is a Prime number");
        else
            System.out.println("It is NOT a Prime number");
    }
}
