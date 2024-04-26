import Foundation

let info = readLine()!.components(separatedBy: " ").compactMap { Int($0) }
let numbers = readLine()!.components(separatedBy: " ").compactMap { Int($0) }
var partialSum = [0]
for number in numbers {
    partialSum.append(partialSum[partialSum.endIndex - 1] + number)
}

for _ in 0..<info[1] {
    let indices = readLine()!.components(separatedBy: " ").compactMap { Int($0) }
    print(partialSum[indices[1]] - partialSum[indices[0] - 1])
}
