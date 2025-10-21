import Foundation

guard let input = readLine(),
      let n = Int(input) else {
    exit(1)
}

var result = 0

for i in 1...n {
    if i + sumOfDigits(i) == n {
        result = i
        break
    }
}

print(result)

func sumOfDigits(_ n: Int) -> Int {
    var n = n
    var result = 0
    
    while n > 0 {
        let (quotient, remainder) = n.quotientAndRemainder(dividingBy: 10)
        result += remainder
        n = quotient
    }
    
    return result
}
