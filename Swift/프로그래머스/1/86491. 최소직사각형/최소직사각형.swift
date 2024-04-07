import Foundation

func solution(_ sizes:[[Int]]) -> Int {
    var maximumLong = 0
    var maximumShort = 0
    
    for size in sizes {
        let width = size[0]
        let height = size[1]
        
        if width >= height {
            maximumLong = max(maximumLong, width)
            maximumShort = max(maximumShort, height)
        } else {
            maximumLong = max(maximumLong, height)
            maximumShort = max(maximumShort, width)
        }
    }
    
    return maximumLong * maximumShort
}