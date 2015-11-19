class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.queue1) == 1:
            self.queue1.pop(0)
            return
        if len(self.queue2) == 1:
            self.queue2.pop(0)
            return
        if len(self.queue1) > 1:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.pop(0))
            self.queue1.pop(0)
            return
        if len(self.queue2) > 1:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.pop(0))
            self.queue2.pop(0)
            return
        
    def top(self):
        """
        :rtype: int
        """
        if self.queue1 != []:
            return self.queue1[-1]
        return self.queue2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return self.queue1 == [] and self.queue2 == []