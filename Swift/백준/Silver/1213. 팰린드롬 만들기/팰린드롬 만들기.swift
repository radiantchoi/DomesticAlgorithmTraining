import Foundation

let letters = Array(readLine()!).map { String($0) }
var occurences = [String: Int]()

for letter in letters {
    if occurences[letter] != nil {
        occurences[letter]! += 1
    } else {
        occurences[letter] = 1
    }
}

var odds = 0
for value in occurences.values {
    if value % 2 == 1 {
        odds += 1
    }
    
    if odds > 1 {
        break
    }
}

if odds > 1 {
    print("I'm Sorry Hansoo")
} else {
    let materials = occurences.keys.sorted()
    var amounts = materials.map { occurences[$0]! }
    let gross = letters.count
    var result = Array(repeating: String(), count: gross)
    
    var starting = 0
    var ending = gross - 1
    for i in 0..<materials.count {
        let material = materials[i]
        
        while amounts[i] > 0 {
            if amounts[i] == 1 {
                let mid = gross / 2
                result[mid] = material
                amounts[i] -= 1
            } else {
                amounts[i] -= 2
                result[starting] = material
                result[ending] = material
                starting += 1
                ending -= 1
            }
        }
    }
    
    print(result.joined())
}
