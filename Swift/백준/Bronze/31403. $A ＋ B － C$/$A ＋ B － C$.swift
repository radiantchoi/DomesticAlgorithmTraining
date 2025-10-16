var words = [String]()

for _ in 0...2 {
    words.append(readLine()!)
}

let number = Int(words[0])! + Int(words[1])! - Int(words[2])!
let quote = Int(words[0] + words[1])! - Int(words[2])!

print(number)
print(quote)