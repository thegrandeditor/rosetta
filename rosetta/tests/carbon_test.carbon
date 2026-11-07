package Geometry api;

interface Shape {
    fn area() -> Float {
    }
}

class Circle {
    var radius: Float;
}

impl Circle as Shape {
    fn area() -> Float {
        let pi: Float = 3;
        return pi;
    }
}

fn test_match(x: Int) -> Int {
    match (x) {
        case 1 => return 10;
        case 2 => return 20;
    }
    return 0;
}
