import Foundation

let n = Int(readLine()!)!

for _ in 0..<n {
    let data = readLine()!.components(separatedBy: " ").compactMap { Int($0) }
    var field = Array(repeating: Array(repeating: 0, count: data[1]), count: data[0])
    
    for _ in 0..<data[2] {
        let coordinate = readLine()!.components(separatedBy: " ").compactMap { Int($0) }
        field[coordinate[0]][coordinate[1]] = 1
    }
    
    var result = 0
    for r in 0..<field.count {
        for c in 0..<field[r].count {
            var isIsland = false
            traverse(&field, r, c, &isIsland)
            
            if isIsland {
                result += 1
            }
        }
    }
    
    print(result)
}

func traverse(_ grid: inout [[Int]], _ row: Int, _ col: Int, _ isIsland: inout Bool) {
    guard (0..<grid.count) ~= row && (0..<grid[0].count) ~= col else {
        return
    }
    
    guard grid[row][col] == 1 else {
        return
    }
    
    grid[row][col] = 0
    isIsland = true
    
    traverse(&grid, row+1, col, &isIsland)
    traverse(&grid, row-1, col, &isIsland)
    traverse(&grid, row, col+1, &isIsland)
    traverse(&grid, row, col-1, &isIsland)
}
