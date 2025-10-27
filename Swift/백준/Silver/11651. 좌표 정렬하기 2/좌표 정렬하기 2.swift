import Foundation

let n = Int(readLine()!)!

var points = [[Int]]()

for _ in 0..<n {
    let point = readLine()!.components(separatedBy: " ")
        .map { Int($0)! }
    
    points.append(point)
}

points.sort { ($0[1], $0[0]) < ($1[1], $1[0]) }

for point in points {
    print(point.map { String($0) }.joined(separator: " "))
}
