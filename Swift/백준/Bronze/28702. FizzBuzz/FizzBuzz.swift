import Foundation

var quotes = [String]()

for _ in 0...2 {
    quotes.append(readLine()!)
}

let fizzBuzz: [String] = Array(1...18).map { number in
    let calculatingNumber = number > 15 ? number - 15: number
    
    if calculatingNumber % 5 == 0 && calculatingNumber % 3 == 0 {
        return "FizzBuzz"
    } else if calculatingNumber % 3 == 0 {
        return "Fizz"
    } else if calculatingNumber % 5 == 0 {
        return "Buzz"
    } else {
        return String(calculatingNumber)
    }
}

var div = 0

for quote in quotes {
    if let number = Int(quote) {
        div = number / 15
    }
}

let window: [String] = quotes.map { quote in
    if let number = Int(quote) {
        return String(number % 15)
    } else {
        return quote
    }
}

for i in 0..<15 {
    if window[0] == fizzBuzz[i] && window[1] == fizzBuzz[i+1] && window[2] == fizzBuzz[i+2] {
        let div = window[2] == "FizzBuzz" ? div + 1 : div
        
        if let number = Int(fizzBuzz[i+3]) {
            print(number + 15 * div)
        } else {
            print(fizzBuzz[i+3])
        }
    }
}
