import Foundation

let n = Int(readLine()!)!
var storage = [[Int]]()

for _ in 0..<n {
    let volume = readLine()!.components(separatedBy: " ").compactMap { Int($0) }
    storage.append(volume)
}

var rates = Array(repeating: storage.count, count: storage.count)
for i in 0..<storage.count {
    let rate = storage.filter { $0[0] > storage[i][0] && $0[1] > storage[i][1] }.count + 1
    rates[i] = rate
}

print(rates.map { String($0) }.joined(separator: " "))