#[derive(Debug, Clone)]
struct Node {
    elem: i32,
    next: Option<Box<Node>>,
    
}

struct LinkedList {
    head: Option<Box<Node>>,
    tail: Option<Box<Node>>,
    size: usize,
}

impl LinkedList {
    fn new() -> Self {
        Self { head: None, tail: None, size: 0 }
    }

    fn empty(&self) -> bool {
        self.size == 0
    }

    fn size(&self) -> usize {
        self.size
    }

    fn value_at(&self, index: usize) -> Option<i32> {
        if index >= self.size {
            return None;
        }
        let mut current = self.head.as_ref().unwrap();
        for _ in 0..index {
            current = current.next.as_ref().unwrap();
        }
        Some(current.elem)
    }

    fn push_front(&mut self, elem: i32) {
        let new_node = Box::new(Node { elem, next: self.head.take() });
        self.head = Some(new_node);
        if self.tail.is_none() {
            self.tail = self.head.clone();
        }
        self.size += 1;
    }

    fn pop_front(&mut self) -> Option<i32> {
        self.head.take().map(|node| {
            self.head = node.next;
            if self.head.is_none() {
                self.tail = None;
            }
            self.size -= 1;
            node.elem
        })
    }

    fn push_back(&mut self, elem: i32) {
        let new_node = Box::new(Node { elem, next: None });
        if self.tail.is_none() {
            self.head = Some(new_node.clone());
            self.tail = Some(new_node);
        } else {
            self.tail.as_mut().unwrap().next = Some(new_node.clone());
            self.tail = Some(new_node);
        }
        self.size += 1;
    }

    fn pop_back(&mut self) -> Option<i32> {
        self.tail.take().map(|node| {
            if self.head.is_none() {
                self.tail = None;
            } else {
                let mut current = self.head.as_mut().unwrap();
                while current.next.is_some() {
                    if current.next.as_ref().unwrap().next.is_none() {
                        current.next = None;
                        self.tail = Some(current.clone());
                        break;
                    }
                    current = current.next.as_mut().unwrap();
                }
            }
            self.size -= 1;
            node.elem
        })
    }

    fn front(&self) -> Option<i32> {
        self.head.as_ref().map(|node| node.elem)
    }

    fn back(&self) -> Option<i32> {
        self.tail.as_ref().map(|node| node.elem)
    }

    fn insert(&mut self, index: usize, elem: i32) {
        if index > self.size {
            return;
        }
        if index == 0 {
            self.push_front(elem);
            return;
        }
        if index == self.size {
            self.push_back(elem);
            return;
        }
        let mut current = self.head.as_mut().unwrap();
        for _ in 0..(index - 1) {
            current = current.next.as_mut().unwrap();
        }
        let new_node = Box::new(Node { elem, next: current.next.take() });
        current.next = Some(new_node);
        self.size += 1;
    }

    fn erase(&mut self, index: usize) {
        if index >= self.size {
            return;
        }
        if index == 0 {
            self.pop_front();
            return;
        }
        if index == self.size - 1 {
            self.pop_back();
            return;
        }
        let mut current = self.head.as_mut().unwrap();
        for _ in 0..(index - 1) {
            current = current.next.as_mut().unwrap();
        }
        current.next = current.next.as_mut().unwrap().next.take();
        self.size -= 1;
    }

    fn value_n_from_end(&self, n: usize) -> Option<i32> {
        if n >= self.size {
            return None;
        }
        let mut current = self.head.as_ref().unwrap();
        let mut runner = self.head.as_ref().unwrap();
        for _ in 0..n {
            runner = runner.next.as_ref().unwrap();
        }
        while runner.next.is_some() {
            current = current.next.as_ref().unwrap();
            runner = runner.next.as_ref().unwrap();
        }
        Some(current.elem)
    }

    fn reverse(&mut self) {
        let mut current = self.head.take();
        let mut new_head = None;
        while let Some(mut boxed_node) = current.take() {
            current = boxed_node.next.take();
            boxed_node.next = new_head.take();
            new_head = Some(boxed_node);
        }
        self.head = new_head;
        self.tail = None;
        let mut current = self.head.as_mut().unwrap();
        while current.next.is_some() {
            current = current.next.as_mut().unwrap();
        }
        self.tail = Some(current.clone());
    }

    fn remove_value(&mut self, value: i32) {
        let mut current = self.head.take();
        let mut new_head = None;
        while let Some(mut boxed_node) = current.take() {
            current = boxed_node.next.take();
            if boxed_node.elem != value {
                boxed_node.next = new_head.take();
                new_head = Some(boxed_node);
            } else {
                self.size -= 1;
            }
        }
        self.head = new_head;
        self.tail = None;
        let mut current = self.head.as_mut().unwrap();
        while current.next.is_some() {
            current = current.next.as_mut().unwrap();
        }
        self.tail = Some(current.clone());
    }
    
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_push_front() {
        let mut list = LinkedList::new();
        list.push_front(1);
        assert_eq!(list.front(), Some(1));
        list.push_front(2);
        assert_eq!(list.front(), Some(2));
    }

    #[test]
    fn test_pop_front() {
        let mut list = LinkedList::new();
        list.push_front(1);
        list.push_front(2);
        assert_eq!(list.pop_front(), Some(2));
        assert_eq!(list.pop_front(), Some(1));
        assert_eq!(list.pop_front(), None);
    }
}