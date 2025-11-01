import Foundation

struct Heap<Element> {
    private var storage: [Element]
    private let areSorted: (Element, Element) -> Bool
    
    init(
        storage: [Element] = [],
        areSorted: @escaping (Element, Element) -> Bool
    ) {
        self.storage = storage
        self.areSorted = areSorted
    }
    
    var isEmpty: Bool {
        storage.isEmpty
    }
    
    private var isNotEmpty: Bool {
        !isEmpty
    }
    
    mutating func push(_ element: Element) {
        storage.append(element)
        siftUp(from: storage.endIndex - 1)
    }
    
    @discardableResult
    mutating func pop() -> Element? {
        guard isNotEmpty else { return nil }
        
        storage.swapAt(0, storage.endIndex - 1)
        
        let output = storage.removeLast()
        
        if isNotEmpty {
            siftDown(from: 0)
        }
        
        return output
    }
    
    func peek() -> Element? {
        storage.first
    }
    
    private mutating func siftUp(from index: Int) {
        var index = index
        
        while index > 0 {
            let parent = (index - 1) >> 1
            
            if areSorted(storage[index], storage[parent]) {
                storage.swapAt(index, parent)
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
            
            let right = left + 1
            var child = left
            
            if right < storage.endIndex,
               areSorted(storage[right], storage[left]) {
                child = right
            }
            
            if areSorted(storage[child], storage[index]) {
                storage.swapAt(child, index)
                index = child
            } else {
                break
            }
        }
    }
}

let n = Int(readLine()!)!
var heapq = Heap<Int> { $0 < $1 }

for _ in 0..<n {
    let command = readLine()!
    
    if command == "0" {
        if let output = heapq.pop() {
            print(output)
        } else {
            print(0)
        }
    } else {
        heapq.push(Int(command)!)
    }
}
