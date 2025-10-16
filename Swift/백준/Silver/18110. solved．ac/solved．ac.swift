import Foundation

let n = Int(readLine()!)!
var opinions = [Int]()

for _ in 0..<n {
    opinions.append(Int(readLine()!)!)
}

func clippedAverage(for arr: [Int], cnt: Int) -> Int {
    if cnt <= 0 {
        return 0
    }
    
    let arr = arr.sorted()
    let clip = Int(round(Double(cnt) * 0.15))
    let clippedArray = arr[clip..<(cnt-clip)]
    
    return Int(round(Double(clippedArray.reduce(0, +)) / Double(clippedArray.count)))
}

print(clippedAverage(for: opinions, cnt: n))
