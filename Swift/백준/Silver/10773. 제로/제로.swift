let n = Int(readLine()!)!
var storage = [Int]()

for _ in 0..<n {
    let number = Int(readLine()!)!
    if number > 0 {
        storage.append(number)
    } else {
        storage.removeLast()
    }
}

print(storage.reduce(0, +))