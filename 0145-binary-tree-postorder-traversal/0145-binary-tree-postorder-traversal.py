class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        
        stack, res = [root], []
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return res[::-1] 
