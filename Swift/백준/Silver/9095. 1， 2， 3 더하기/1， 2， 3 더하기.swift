let n = Int(readLine()!)!
var table = Array(repeating: 0, count: 11)
// 0을 나타내는 경우는 아무 숫자도 선택하지 않는 1가지!
table[0] = 1

for i in 1..<table.endIndex {
    for j in [1, 2, 3] {
        if i >= j {
            table[i] += table[i - j]
        }
    }
}

for _ in 0..<n {
    let m = Int(readLine()!)!
    print(table[m])
}
