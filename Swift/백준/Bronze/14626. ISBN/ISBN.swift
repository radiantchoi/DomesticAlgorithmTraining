import Foundation

guard let input = readLine() else {
    exit(1)
}

let digits = input.map { String($0) }

var result = 0
var lost = -1

for (index, letter) in digits.enumerated() {
    if index == 12 {
        guard let m = Int(letter),
              lost >= 0 else {
            continue
        }
        
        for x in 0...9 {
            let missing = lost % 2 == 0 ? x : 3 * x
            
            if (result + missing) % 10 == (10 - m) % 10 {
                print(x)
            }
        }
        
        break
    }
    
    if let value = Int(letter) {
        result += index % 2 == 0 ? value : 3 * value
        result %= 10
    } else {
        lost = index
    }
}
