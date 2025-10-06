import Foundation

func solution(_ k:Int64, _ room_number:[Int64]) -> [Int64] {
    let roomNumber = room_number
    
    var rooms = [Int64: Int64]()
    var result = [Int64]()
    
    for number in roomNumber {
        var visiteds = [Int64]()
        let current = find(number, &rooms, &visiteds)
        
        result.append(current)
        
        for visited in visiteds {
            rooms[visited] = current + 1
        }
    }
    
    return result
}

func find(_ n: Int64, _ rooms: inout [Int64: Int64], _ visiteds: inout [Int64]) -> Int64 {
    visiteds.append(n)
    
    guard let path = rooms[n] else {
        return n
    }
    
    return find(path, &rooms, &visiteds)
}