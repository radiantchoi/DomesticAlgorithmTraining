import Foundation
let numbers = readLine()!.components(separatedBy: " ").compactMap { Int($0) }
let result = Array(1...numbers[0]).filter { numbers[0] % $0 == 0 }
print(result.count >= numbers[1] ? result[numbers[1] - 1] : 0)