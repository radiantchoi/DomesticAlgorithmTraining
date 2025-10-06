import Foundation

func solution(_ n:Int) -> [[Int]] {
    var result = [[Int]]()
    hanoi(n, 1, 2, 3, &result)
    return result
}

func hanoi(_ n: Int, _ starting: Int, _ passing: Int, _ ending: Int, _ answer: inout [[Int]]) {
    if n == 1 {
        answer.append([starting, ending])
        return
    }
    
    hanoi(n - 1, starting, ending, passing, &answer)
    answer.append([starting, ending])
    hanoi(n - 1, passing, starting, ending, &answer)
}