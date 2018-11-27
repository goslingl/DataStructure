import sys

try:
    xrange # python2
except NameError:
    xrange = range # python3

class Heap(object):
    ''' 数据结构-堆的实现,以最大堆为例
    '''
    def __init__(self, A):
        self.H = A[:] # 堆使用数组存储，从第一个元素开始
        self.size = len(A)
        self.build_heap(self.size)

    def _heap(self, size, idx):
        ''' 维护最大堆指定节点为根节点的子堆
        '''
        if size <= 1 or int(size/2) <= idx: return
        left = 2 * idx + 1
        right =2 * idx + 2
        max_idx = idx
        max_idx = left if left < size and self.H[left] > self.H[max_idx] else max_idx
        max_idx = right if right < size and self.H[right] > self.H[max_idx] else max_idx
        if max_idx != idx:
            #(self.H[idx], self.H[max_idx]) = (self.H[max_idx], self.H[idx])
            self.H[idx], self.H[max_idx] = self.H[max_idx], self.H[idx]
            self._heap(size, max_idx) # 递归调用

    def build_heap(self, size):
        '''使用数组H的前size个元素构建最大堆
        '''
        for idx in xrange(int(size/2)-1, 0-1, -1):
            self._heap(size, idx)
            print(idx, self.H)

    def sort(self):
        ''' 利用最大堆排序
        '''
        size = len(self.H)
        if size <= 1: return
        for idx in xrange(0, size):
            self.H[0], self.H[size-1-idx] = self.H[size-1-idx], self.H[0]
            self.build_heap(size-1-idx)
            print('sort', idx, self.H)

    # TODO 使用堆实现优先队列

if __name__ == '__main__':
    A = [ 1, 3, 5, 2, 4, 8, 6, 7, 9, 0, 8]
    print(A)
    heap = Heap(A)
    print(heap.H)
    heap.sort()
    print(heap.H)
