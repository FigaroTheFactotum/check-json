extern crate serde_json;

use std::io::Read;
use serde_json::Value;

fn main() {
    let mut buffer = String::new();
    ::std::io::stdin().read_to_string(&mut buffer).unwrap();

    let v: Value = serde_json::from_str(&buffer).unwrap();

    let text = v.to_string();

    print!("{}", text);
}
