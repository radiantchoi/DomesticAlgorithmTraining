import Foundation

guard let input = readLine(),
      let n = Int(input) else {
    exit(1)
}

var occurences = Array(repeating: 0, count: 10001)

for _ in 0..<n {
    guard let input = readLine(),
          let number = Int(input) else {
        continue
    }

    occurences[number] += 1
}

var out = ""

for i in 1...10000 {
    out += String(repeating: "\(i)\n", count: occurences[i])
}

print(out)
