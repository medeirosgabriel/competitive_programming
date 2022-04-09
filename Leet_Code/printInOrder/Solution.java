import java.util.concurrent.Semaphore;

// https://leetcode.com/problems/print-in-order/

class Solution {

    private Semaphore first;
    private Semaphore second;
    
    public Foo() {
        this.first = new Semaphore(0);
        this.second = new Semaphore(0);
    }

    public void first(Runnable printFirst) throws InterruptedException {
        
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        first.release();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        first.acquire();
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        second.release();
    }

    public void third(Runnable printThird) throws InterruptedException {
        second.acquire();
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}
