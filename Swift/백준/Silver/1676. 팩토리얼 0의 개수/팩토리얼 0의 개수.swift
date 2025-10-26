import Foundation

let n = Int(readLine()!)!

var zeroes = 0
var stack = [Int]()

if n > 2 {
    for i in 1...n {
        var i = i
        
        while i % 10 == 0 {
            zeroes += 1
            i /= 10
        }
        
        while i % 2 == 0 {
            if !stack.isEmpty,
               stack[stack.endIndex - 1] == 5 {
                stack.removeLast()
                zeroes += 1
                i /= 2
            } else {
                stack.append(2)
                i /= 2
            }
        }
        
        while i % 5 == 0 {
            if !stack.isEmpty,
               stack[stack.endIndex - 1] == 2 {
                stack.removeLast()
                zeroes += 1
                i /= 5
            } else {
                stack.append(5)
                i /= 2
            }
        }
    }
}

print(zeroes)
