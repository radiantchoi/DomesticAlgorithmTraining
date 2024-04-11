import Foundation

let n = Int(readLine()!)!

var possibilities = [String]()
var base = (1...9).map { String($0) }

func makePossibilities(_ length: Int,  _ current: String, _ table: [String], _ p: inout [String]) {
    guard length < 3 else {
        p.append(current)
        return
    }
    
    for letter in table {
        let newTable = table.filter { $0 != letter }
        makePossibilities(length + 1, current + letter, newTable, &p)
    }
}

makePossibilities(0, "", base, &possibilities)

for _ in 0..<n {
    let attempt = readLine()!.components(separatedBy: " ")
    let challenge = attempt[0]
    let strike = Int(attempt[1])!
    let ball = Int(attempt[2])!
    let accurates = strike + ball
    
    possibilities = possibilities.filter { possibility in
        return common(challenge, possibility) == accurates
        && commonLocation(challenge, possibility) == strike
    }
}

func common(_ s1: String, _ s2: String) -> Int {
    var result = 0
    
    for letter in s1 {
        if s2.contains(letter) {
            result += 1
        }
    }
    
    return result
}

func commonLocation(_ s1: String, _ s2: String) -> Int {
    guard s1.count == s2.count else {
        return 0
    }
    
    var result = 0
    var a1 = Array(s1)
    var a2 = Array(s2)
    
    for i in 0..<a1.count {
        if a1[i] == a2[i] {
            result += 1
        }
    }
    
    return result
}

print(possibilities.count)
