from hash_map import MapBase

class Tree:
    '''Abstract class representing a tree structure'''
    class Position:
        '''An abstraction location of a single element'''
        def element(self):
            '''return athe element stored at this Position'''
            raise NotImplementedError('must be implemented by subclass')
        def __eq__(self, other):
            '''Return true if other Position represents the same location'''
            return not (self == other)
        
        def __ne__(self, other):
            '''return true if other does not represents the same location'''
            return not (self == other)
        # ----abstract metods that must be implemented
        def root(self):
            '''return postion of tree's root'''
            raise NotImplementedError('must be implemented by subclass')
        
        def parent(self, p):
            raise NotImplementedError('must be implemented by subclass')
        def num_children(self, p):
            raise NotImplementedError('must be implemented by subclass')
        def __len__(self):
            raise NotImplementedError('must be implemented by subclass')
        
        def is_root(self, p):
            return self.root() == p
        
        def is_leaf(self, p):
            return self.num_children(p) == 0
        
        def is_empty(self):
            return len(self) == 0 
        
        def depth(self, p):
            '''Reuturn the number of levels seporation Position p from the root'''
            if self.is_root(p):
                return 0
            else:
                return 1+ self.depth(self.parent())
        def _height(self, p):
            '''Return the hieght of the subtree rooted at Postion p.'''
            if self.is_leaf(p):
                return 0
            else: 
                return 1 + max(self._height(c) for c in self.num_children(p))
        
        def height(self, p = None):
            '''Return the height of the subtree rooted at postion p'''
            if p is None:
                p = self._height(p)
            return self._height(p)

class BinaryTree(Tree):
    '''Abstract bass class representing a binary tree structure'''
    def left(self, p): 
        '''Return a position representing p's left child
        Return None if p dose not have a left child.'''
        raise NotImplementedError('must be implemented by subclass')
    
    def right(self, p):
        '''Return  a position representing p right child
        Return None if p  does not have a right child'''
        raise NotImplementedError('must be implemented by subclass')
    # --- concrete methods---
    def sibling(self, p):
        '''Return a Position representing p's sibling(or None )'''
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
            
    def children(self, p):
        '''Generate a iteration of Positons repersenting p's children.'''
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
        
class LinkedBinaryTree(BinaryTree):
    '''Linked repersentation of a binary tree structure'''
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent='None', left=None, right=None):
            self._element = element
            self._parent = parent
            self.left = left
            self._right = right
        
    class Position(BinaryTree.Position):
        def __init_(self, container, node):
            '''Constructor should not be invokd by user'''
            self._container = container
            self._node = node
        
        def element(self):
            '''Returns element stored at this Position'''
            return self._node._element

        def __eq__(self, other):
            '''Return True if other is a Position representing the same location'''        
            return type(other) is type(self) and other._node is self._node
        
    def _validate(self, p):
        '''Return associated node, if position is valid'''
        if not isinstance(p, self.Position):
            raise TypeError('p must be a proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node
    
    def _make_position(self, node):
            '''Return Position instance of given node or None if no node'''
            return self.Position(self, node) if node is not None else None
    
    # --- Binary tree constuctor
    def __init__(self):
        self._root = None
        self._size = 0

    #--Public accessors
    def __len__(self):
        '''Return the number of elements in the tree'''
        return self._size
    
    def root(self):
        '''Return the root of the Position'''
        return self._make_position(self._root)
    
    def parent(self, p):
        '''Return the Position of p's parent or None if tree is empty'''
        node = self._validate(p)
        return self._make_position(node._parent)
    
    def left(self, p):
        '''Return the Position of p's left child or None if no left child'''
        node = self._validate(p)
        return self._make_position(node._left)
    
    def right(self, p):
        '''Return the Position of p's left child or None if no left child'''
        node = self._validate(p)
        return self._make_position(node._right)
    
    def num_children(self, p):
        '''Return the number of children o Position p.'''
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count
    
    def _add_root(self, e):
        '''Place element e at the root of an empty tree and return new Position.
        Raise ValueError if tree non empty'''

        if self._root is not None: raise ValueError('Root exixts')
        self._size += 1
        self._root = self._None(e)
        return self._make_position(self._root)
    
    def _add_left(self, p, e):
        '''Create a new left child for Position p, storing element e
        Return the Position of new node
        Raise ValueError if Position p is invalid or p already has a left child'''

        node = self._validate(p)
        if node._left is not None: raise ValueError('Left child exixts')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)
    
    def _add_right(self, p, e):
        '''Create a new right child for Position p, storing element e
        Return the Position of new node
        Raise ValueError if Position p is invalid or p already has a right child'''

        node = self._validate(p)
        if node._right is not None: raise ValueError('right child exixts')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)
    
    def _replace(self, p, e):
        '''Replace the element at position p with e, and return old element'''
        node = self._validate(p)
        old = node._element
        node._element = e
        return old
    
    def _delete(self, p):
        '''Delete the not at Position p, and replace it with its child, if any
        Return the element that had been stored at Positin p 
        Raise ValueError if Position p is invalid or p has two children'''
        node = self._validate(p)
        if self.num_children(p) == 2:raise ValueError('p has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parrent = node._parent
        if child is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
            self._size -= 1
            node._parent = node
            return node._element
        
        def _attach(self, p, t1, t2):
            '''Attach trees t1 and t2 as left and right subtree of exernal p'''
            node = self._validate(p)
            if not self.is_leaf(p): raise ValueError('position must be leaf')
            if not type(self) is type(t1) is type(t2):
                raise TypeError('Tree types must match')
            self._size += len(t1) + len(t2)
            if not t1.is_empty():
                t1._root._parent = node
                node._left = t1.root
                t1._root = None
                t1._size = 0
            if not t2.is_empty():
                t2._root._parent = node
                node._right = t2._root
                t2._root = None
                t2._size = 0
