const std = @import("std");

pub fn add(x: i32, y: i32) i32 {
    defer {
        const temp = 1;
    }
    return x + y;
}
