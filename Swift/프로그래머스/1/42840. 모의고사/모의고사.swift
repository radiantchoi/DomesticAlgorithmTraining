import Foundation

func solution(_ answers:[Int]) -> [Int] {
    let firstPaper = [1, 2, 3, 4, 5]
    let secondPaper = [2, 1, 2, 3, 2, 4, 2, 5]
    let thirdPaper = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    var scores = [0, 0, 0]
    for (index, answer) in answers.enumerated() {
        if firstPaper[index % 5] == answer {
            scores[0] += 1
        }
        
        if secondPaper[index % 8] == answer {
            scores[1] += 1
        }
        
        if thirdPaper[index % 10] == answer {
            scores[2] += 1
        }
    }
    
    return scores.enumerated().filter { $0.1 == scores.max()! }.map { $0.0 + 1 }
}
