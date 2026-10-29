class MyThread implements Runnable{
    public void run()
    {
        for(int i=0;i<5;i++)
        {
            try{
            IO.println("Amitava running thread is "+Thread.currentThread().getName());
            Thread.sleep(2000);
            }
            catch(InterruptedException e)
            {
                IO.print(e);
            }

        }
        IO.println("Amitava running thread is OVER!!!! "+Thread.currentThread().getName());
    }    
}

class Demo
{
    public static void main(String[] args) {
        MyThread m=new MyThread();
        Thread t1=new Thread(m, "amitava1");
         Thread t2=new Thread(m, "amitava2");
          Thread t3=new Thread(m, "amitava3");

        t1.start();
        t2.start();
        t3.start();
    
         for(int i=0;i<8;i++)
        {
            try{
            IO.println("main running thread is ......"+Thread.currentThread().getName());
            Thread.sleep(1000);
            }
            catch(InterruptedException e)
            {
                IO.println(e);
            }
        }
        IO.println("MAIN running thread is OVER!!!! "+Thread.currentThread().getName());
        
    }
}