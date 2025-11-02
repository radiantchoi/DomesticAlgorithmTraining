import Foundation

struct Heap<Element> {
    private var storage: [Element]
    private let areSorted: (Element, Element) -> Bool
    
    var isEmpty: Bool {
        storage.isEmpty
    }
    
    private var isNotEmpty: Bool {
        !isEmpty
    }
    
    init(
        storage: [Element] = [],
        areSorted: @escaping (Element, Element) -> Bool
    ) {
        self.storage = storage
        self.areSorted = areSorted
    }
    
    mutating func push(_ element: Element) {
        storage.append(element)
        siftUp(from: storage.endIndex - 1)
    }
    
    @discardableResult
    mutating func pop() -> Element? {
        guard isNotEmpty else {
            return nil
        }
        
        storage.swapAt(0, storage.endIndex - 1)
        
        let out = storage.removeLast()
        
        if isNotEmpty {
            siftDown(from: 0)
        }

        return out
    }
    
    private mutating func siftUp(from index: Int) {
        var index = index
        
        while index > 0 {
            let parent = (index - 1) >> 1
            
            if areSorted(storage[index], storage[parent]) {
                storage.swapAt(parent, index)
                index = parent
            } else {
                break
            }
        }
    }
    
    private mutating func siftDown(from index: Int) {
        var index = index
        
        while true {
            let left = (index << 1) + 1
            if left >= storage.endIndex {
                break
            }
            
            var child = left
            
            let right = left + 1
            if right < storage.endIndex,
               areSorted(storage[right], storage[left]) {
                child = right
            }
            
            if areSorted(storage[child], storage[index]) {
                storage.swapAt(index, child)
                index = child
            } else {
                break
            }
         }
    }
}

guard let input = readLine(),
      let n = Int(input) else {
    exit(1)
}

var pq = Heap<Int> { lhs, rhs in
    if abs(lhs) != abs(rhs) {
        return abs(lhs) < abs(rhs)
    } else {
        return lhs < rhs
    }
}

for _ in 0..<n {
    guard let command = readLine() else {
        continue
    }
    
    if command == "0" {
        print(pq.pop() ?? 0)
    } else {
        guard let number = Int(command) else {
            continue
        }
        
        pq.push(number)
    }
}
