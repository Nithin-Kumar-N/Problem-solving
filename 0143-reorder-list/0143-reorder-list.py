class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return head
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second_half=slow.next
        slow.next=None
        prev=None
        while second_half:
            temp=second_half.next
            second_half.next=prev
            prev=second_half
            second_half=temp
        first_half=head
        while prev:
            temp1=first_half.next
            temp2=prev.next
            first_half.next=prev
            prev.next=temp1
            first_half=temp1
            prev=temp2
        return head
        