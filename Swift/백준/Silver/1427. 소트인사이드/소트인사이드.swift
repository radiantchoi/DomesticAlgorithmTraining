let numbers = Array(readLine()!).map { String($0) }.sorted { $0 > $1 }
print(numbers.joined())