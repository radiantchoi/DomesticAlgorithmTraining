let n = Int(readLine()!)!

var fibo = Array(repeating: 0, count: 41)
fibo[1] = 1

for _ in 0..<n {
    var zeroes = 0
    var ones = 0
    let number = Int(readLine()!)!
    
    if number == 0 {
        print("1 0")
    } else if number == 1 {
        print("0 1")
    } else {
        for i in 2...number {
            if fibo[i] == 0 {
                fibo[i] = fibo[i-1] + fibo[i-2]
            }
        }
        
        print("\(fibo[number-1]) \(fibo[number])")
    }
}