while true {
    let number = Int(readLine()!)!
    if number == -1 {
        break
    }

    var result = Array(1..<number).filter { number % $0 == 0 }
    if result.reduce(0, +) == number {
        let formula = result.map { String($0) }.joined(separator: " + ")
        print("\(number) = \(formula)")
    } else {
        print("\(number) is NOT perfect.")
    }
}

