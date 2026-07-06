class Foo(object):
    def __init__(self):
        self.lock = 0
        pass
    
    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock = 1


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        while self.lock is not 1:
            time.sleep(0.1)

        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.lock = 2
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        
        while self.lock is not 2:
            time.sleep(0.1)
        # printThird() outputs "third". Do not change or remove this line.
        printThird()