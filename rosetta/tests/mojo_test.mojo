@parameter
fn process(inout x: Int) -> Int {
    let y = 10;
    x = x + y;
    return x;
}

struct Point {
    var x: Float;
    var y: Float;
}
