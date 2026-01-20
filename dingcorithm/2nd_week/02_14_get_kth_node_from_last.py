class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        # 1. 모든 linkedList의 길이를 구한다.
        # 2. linkedList의 길이에서 k만큼 빼고, 그만큼 이동시킨다.
        # 3. 그 노드를 반환한다.
        length = 0
        cur = self.head
        while cur is not None:
            length += 1
            cur = cur.next

        answerIndex = length - k
        cur = self.head
        for index in range(answerIndex):
            cur = cur.next
        return cur

        # 1. k만큼의 길이가 떨어진 포인터 두 개를 이용한다.
        fast = self.head
        slow = self.head

        for i in range(k):
            if fast.next is not None:
                fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(12)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!